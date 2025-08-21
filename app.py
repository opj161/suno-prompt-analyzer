# suno-prompt-analyzer/app.py

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Import our custom modules
from data_loader import load_suno_data
from analyzer import prepare_analysis_results, analyze_explorer_styles, format_label
from visualizer import create_ranked_bar_chart, create_association_map

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Suno Prompt Analyzer", layout="wide", initial_sidebar_state="collapsed")

# --- 2. DATA LOADING ---
DATA_FILE_PATH = Path(__file__).parent / "data" / "suno_logic.json"
DEFAULT_STYLES, CO_OCCURRENCE_DATA = load_suno_data(DATA_FILE_PATH)

# --- 3. UI LAYOUT ---
st.title("🎵 Suno Prompt Analyzer")
st.markdown("Enter your Suno style prompt to visualize its underlying stylistic connections and discover its 'gravitational pull'.")
st.divider()

# Initialize session state for persistent prompt text ONCE
if 'prompt_text' not in st.session_state:
    st.session_state.prompt_text = "A powerful acoustic folk ballad in a minor key with a deeply reflective and intimate feel and a slow and deliberate adagio tempo. The primary instrumentation is a clean fingerpicked acoustic guitar playing intricate arpeggiated chords with a mournful cello providing sustained counter-melodies, a subtle atmospheric string section, and a sparse piano adding depth and flowing texture. The production features modern professional mastering with studio-grade fidelity, exceptional warmth and clarity, a natural reverb on the instruments, and a clean mix with no harsh highs. Powerful, increasingly intense and epic. Professional mastering."

tab1, tab2 = st.tabs(["**Prompt Analyzer**", "**Style Explorer**"])

with tab1:
    # --- PROMPT ANALYZER MODE ---
    st.header("Analyze a Full Prompt")

    with st.form(key='prompt_form'):
        prompt_text_input = st.text_area(
            "Enter your prompt here:",
            value=st.session_state.prompt_text,
            height=150,
        )
        negative_prompt_input = st.text_input(
            "Negative Keywords (comma-separated):",
            placeholder="e.g., rock, pop, guitar",
            help="Keywords to exclude and steer the model away from."
        )
        submit_button = st.form_submit_button(label='Analyze Prompt')

    if submit_button:
        st.session_state.prompt_text = prompt_text_input
        if prompt_text_input:
            analysis_results = prepare_analysis_results(
                prompt_text_input, negative_prompt_input, DEFAULT_STYLES, CO_OCCURRENCE_DATA
            )
            st.session_state.analysis_results = analysis_results
        else:
            st.warning("Please enter a prompt to analyze.")
            st.session_state.analysis_results = None

    if 'analysis_results' in st.session_state and st.session_state.analysis_results:
        results = st.session_state.analysis_results
        st.divider()

        if results.get("error"):
            st.error(results["error"])
        else:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.subheader("Interactive Prompt Inspector")
                inspector_css = """
                <style>
                    .highlight-keyword { background-color: rgba(255, 127, 80, 0.3); border-radius: 4px; padding: 2px 4px; position: relative; cursor: pointer; }
                    .highlight-keyword:hover::after { content: attr(data-tooltip); position: absolute; left: 0; top: 120%; z-index: 100; background-color: #222; color: #fff; border: 1px solid #444; border-radius: 5px; padding: 10px; font-family: monospace; font-size: 0.9em; white-space: pre-wrap; min-width: 250px; text-align: left; }
                    .neg-tag { display: inline-block; background-color: #400; color: #f88; padding: 4px 8px; margin: 2px; border-radius: 5px; font-family: monospace; font-size: 0.9em; }
                    .tag { display: inline-block; background-color: #334; color: #afa; padding: 4px 8px; margin: 2px; border-radius: 5px; font-family: monospace; font-size: 0.9em; }
                </style>
                """
                st.markdown(inspector_css + f"<div style='border: 1px solid #333; padding: 10px; border-radius: 5px;'>{results['annotated_html']}</div>", unsafe_allow_html=True)
                
                st.metric(label="Keyword Cohesion Score", value=f"{results['cohesion_score']:.1f} / 100", help="Measures how strongly your keywords are related. Higher is better.")
                score = results['cohesion_score']
                if score >= 75: st.success("✓ Excellent Cohesion")
                elif score >= 40: st.warning("! Moderate Cohesion")
                else: st.error("✗ Low Cohesion")
                
                if results['negative_keywords']:
                    st.markdown("<b>Applied Negative Keywords</b>", unsafe_allow_html=True)
                    neg_keywords_html = "".join([f"<span class='neg-tag'>{kw}</span>" for kw in results['negative_keywords']])
                    st.markdown(neg_keywords_html, unsafe_allow_html=True)
                
                st.divider()
                st.subheader("🤖 Prompt Co-Pilot")
                suggestion = results.get("suggestion")
                if suggestion:
                    with st.expander(f"{suggestion['title']}", expanded=True):
                        body = suggestion.get('body', {})
                        if body.get('intro'): st.write(body['intro'])
                        if body.get('clusters'):
                            for i, cluster in enumerate(body['clusters']):
                                cluster_html = "".join([f"<span class='tag'>{kw}</span>" for kw in cluster])
                                st.markdown(f"**Cluster {i+1}:** {cluster_html}", unsafe_allow_html=True)
                        if body.get('strategies'):
                            for title, points in body['strategies'].items():
                                st.markdown(f"--- \n**{title}**")
                                for point in points: st.markdown(f"- {point}")
                        elif body.get('suggestions'): st.markdown(" ".join(body['suggestions']))

            with col2:
                st.subheader("Stylistic Fingerprint")
                fingerprint_fig = create_ranked_bar_chart(
                    results['fingerprint'], "Top 10 Stylistic Influences", "Normalized Influence Score (log scale)"
                )
                st.plotly_chart(fingerprint_fig, use_container_width=True)

                st.divider()
                st.subheader("Interactive Association Map")
                edge_threshold = st.slider(
                    "Minimum Connection Strength (log scale):", min_value=0.0, max_value=15.0, value=7.0, step=0.5,
                    help="Hides weaker connections to declutter the graph.", key="analyzer_edge_slider"
                )
                filtered_graph_data = results['graph_data'].copy()
                filtered_graph_data['edges'] = [edge for edge in filtered_graph_data['edges'] if edge['value'] >= edge_threshold]
                network_graph = create_association_map(filtered_graph_data)
                html_content = network_graph.generate_html()
                components.html(html_content, height=620, scrolling=True)

with tab2:
    # --- STYLE EXPLORER MODE ---
    st.header("Explore a Single Style")
    st.markdown("Select a single keyword to discover its closest associations, explore its stylistic neighborhood, and get a pre-built prompt starter kit.")

    all_styles_sorted = sorted(list(DEFAULT_STYLES))
    col1_exp, col2_exp = st.columns(2)
    with col1_exp:
        primary_style = st.selectbox(
            "**Primary Style:**",
            options=all_styles_sorted,
            index=None,
            placeholder="Search for a primary style..."
        )
    with col2_exp:
        secondary_style = None
        if primary_style:
            secondary_options = [""] + [s for s in all_styles_sorted if s != primary_style]
            secondary_style = st.selectbox(
                "**Secondary Style (for fusion):**",
                options=secondary_options,
                index=0,
                placeholder="Select a style to blend... (Optional)"
            )
            if secondary_style == "": secondary_style = None

    if primary_style:
        explorer_results = analyze_explorer_styles(primary_style, secondary_style, CO_OCCURRENCE_DATA)
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            chart_title = f"Top Associations for '{format_label(primary_style)}'"
            if secondary_style:
                chart_title += f" & '{format_label(secondary_style)}' Fusion"
            st.subheader(chart_title)
            bar_fig = create_ranked_bar_chart(explorer_results['bar_chart_data'], chart_title, "Normalized Association Strength (log scale)")
            st.plotly_chart(bar_fig, use_container_width=True)

            st.subheader("📝 Prompt Starter Kit")
            st.info("Copy the prompt below as a starting point for your creation.")
            st.code(explorer_results['prompt_starter_text'], language='text')

        with col2:
            st.subheader("Association Constellation")
            explorer_graph = create_association_map(explorer_results['graph_data'])
            html_content = explorer_graph.generate_html()
            components.html(html_content, height=620, scrolling=True)