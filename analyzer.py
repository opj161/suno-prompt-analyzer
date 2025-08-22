# suno-prompt-analyzer/analyzer.py

import math
import logging
import streamlit as st
import re
import networkx as nx

import os
from google import genai
from google.genai import types
from google.genai import errors

from itertools import combinations
from collections import defaultdict
from typing import List, Set, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from style_definitions import STYLE_PERSONALITY_DICT

# --- Constants ---
PRIMARY_NODE_COLOR = "#FF6347"  # Tomato
SECONDARY_NODE_COLOR = "#4682B4"  # SteelBlue
TERTIARY_NODE_COLOR = "#D3D3D3"  # LightGray
NEGATIVE_NODE_COLOR = "#8B0000"  # DarkRed
TAINTED_NODE_COLOR = "#FFA500"  # Orange
BRIDGE_NODE_COLOR = "#32CD32"  # LimeGreen
ACRONYMS = {"r&b", "k-pop", "j-pop", "edm"}  # Styles to be fully uppercased

# --- Prompt Starter Kit Constants (Optimized) ---
MOOD_KEYWORDS = {
    "aggressive",
    "ambient",
    "anthemic",
    "atmospheric",
    "chill",
    "cinematic",
    "dark",
    "dramatic",
    "dreamy",
    "deep",
    "emotional",
    "energetic",
    "epic",
    "ethereal",
    "futuristic",
    "groovy",
    "heartfelt",
    "intense",
    "melancholic",
    "mellow",
    "powerful",
    "psychedelic",
    "romantic",
    "sad",
    "smooth",
    "uplifting",
    "upbeat",
}
INSTRUMENT_KEYWORDS = {"guitar", "piano", "synth", "bass", "drum", "violin", "electric guitar", "acoustic guitar", "orchestral", "flute"} # Complete
VOCAL_KEYWORDS = {"male voice", "female voice", "male vocals", "female vocals", "vocaloid", "female singer", "opera", "gospel"}
PRODUCTION_PROMPT = "The production is modern and clean with studio-grade fidelity and exceptional warmth and clarity and no harsh highs."

GEMINI_SYSTEM_INSTRUCTION = """You are an expert AI music prompt engineer specializing in Suno v4.5+. Your task is to transform a structured creative brief into a perfect, narrative-style prompt for Suno. You must adhere to the following strict rules:

1.  **Narrative First:** Do not list features. Write a cohesive, descriptive paragraph that tells the story of the song. Describe the emotional arc and how the track evolves from beginning to end.

2.  **Punctuation is Code:**
    *   You MUST use periods (`.`) to separate distinct conceptual blocks (e.g., Genre/Feel, Instrumentation, Vocals, Production). A good prompt has 3-5 distinct sentences.
    *   Within a single block, you MUST NOT use commas to separate descriptors. Instead, you MUST connect them with 'and' or 'with' to form a continuous, flowing phrase.

3.  **Creative Synthesis:** When the brief presents emotionally or stylistically contradictory concepts, your primary goal is to find a creative, believable fusion. Propose a narrative or aesthetic that resolves the paradox. For instance, if a brief combines a melancholic mood with an energetic tempo, your role is to invent a scenario that makes sense of this, such as 'a cathartic dance track about overcoming grief' or 'a frantic, driving song with sorrowful lyrics'. Do not simply state the contradiction. For a single style, expand upon its core identity with vivid, evocative language.

4.  **Tag Dilution Strategy:** Your goal is to dilute the tag pool. Incorporate multiple related adjectives and descriptive terms from the brief to give Suno a rich semantic field. This critical strategy prevents the model from over-optimizing on a single, restrictive keyword and encourages it to draw from a wider range of its training data, leading to higher-quality outputs. Ensure all terms fit naturally within the narrative.

5.  **Implicit Structure:** The final prompt should implicitly cover these four key areas in a flowing narrative: 1. Overall Genre and Mood. 2. Key Instrumentation and Texture. 3. Vocal Style and Performance. 4. Production and Mastering.

6.  **Evocative Production Description (Crucial):** The final sentence of your prompt MUST be a detailed, professional description of the audio mastering and production. Your goal is to evoke a high-fidelity listening experience by synthesizing a unique description based on the song's genre and mood. Instead of using a generic phrase, describe the song's sonic qualities from an audio engineer's perspective, using your own vocabulary to cover elements like:
    *   **Sonic Clarity & Frequency Balance:** Describe the quality of the high, mid, and low frequencies. Is the mix clean and modern, or intentionally raw and vintage?
    *   **Low-End Character:** How does the bass and kick drum feel in the mix?
    *   **Stereo Image & Space:** Describe the width and depth of the soundstage and the use of effects like reverb or delay.
    *   **Vocal Production:** Describe how the vocals are treated and placed within the mix to serve the song's emotional intent.

    You MUST generate a novel, descriptive combination of these elements. This is a test of your creative and technical vocabulary.

7.  **Handle Creative Constraints**: When the brief provides a "Creative Goal" to steer away from certain qualities, your task is not simply to omit words. You must actively construct the narrative prompt using contrasting and opposing descriptive language. Use the "Emphasize" list to build the core of your prompt and the "Steer Away From" list as a guide for what sonic textures to describe in opposition.
"""

def generate_polished_prompt_with_gemini(creative_brief: str, api_key: str) -> str:
    """
    Calls the Gemini API to generate a polished Suno prompt, with robust error handling
    and all safety filters disabled as per the application's design.
    """
    try:
        client = genai.Client(api_key=api_key)
        logging.info("Attempting to generate content with Gemini 2.5 Pro.")
        logging.warning("All Gemini API safety filters are being disabled for this call.")

        # CORRECTED: Use snake_case for all parameters in GenerateContentConfig.
        # CORRECTED: Completed the list of safety categories to include all five adjustable filters.
        # This ensures all safety measures are explicitly set to BLOCK_NONE.
        safety_settings = [
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_NONE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY, threshold=types.HarmBlockThreshold.BLOCK_NONE),
        ]

        # CORRECTED: All parameters now use snake_case as required by the Python SDK documentation.
        generation_config = types.GenerateContentConfig(
            system_instruction=GEMINI_SYSTEM_INSTRUCTION,
            temperature=0.7, # Add a little creativity
            safety_settings=safety_settings,
            # This is set correctly to disable tool use, as we only need text generation.
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
        )

        # Add retry logic for 500 errors
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # The model is correctly set to 'gemini-2.5-pro' per the user's instructions.
                response = client.models.generate_content(
                    model="gemini-2.5-pro",
                    contents=creative_brief,
                    config=generation_config,
                )
                break  # Success, exit retry loop
            except errors.ServerError as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    logging.warning(f"Gemini API 500 error (attempt {attempt + 1}/{max_retries}). Retrying in {wait_time}s...")
                    import time
                    time.sleep(wait_time)
                    continue
                else:
                    # Final attempt failed
                    logging.error(f"Gemini API failed after {max_retries} attempts: {e}")
                    return f"ERROR: Gemini API server error after {max_retries} attempts. The service may be temporarily unavailable."
            except errors.BlockedPromptError as e:
                # This handles cases where the response is blocked despite relaxed settings (e.g., core harms)
                logging.error(f"Gemini API call failed: Prompt was blocked. Reason: {e}")
                return f"ERROR: Your prompt was blocked for violating core safety policies which cannot be disabled. Reason: {e}"
            except Exception as e:
                # Non-retriable errors will be raised immediately
                logging.error(f"A non-retriable Gemini API error occurred: {e}", exc_info=True)
                return f"ERROR: A Gemini API error occurred: {str(e)}"

        logging.info(f"Gemini API Response received successfully")

        if not response.candidates:
            logging.error("No candidates in response - unexpected with safety filters disabled")
            return "ERROR: No response candidates generated. Please try modifying your creative brief."
            
        candidate = response.candidates[0]
        
        if candidate.finish_reason.name != "STOP":
            logging.warning(f"Gemini response finished with reason: {candidate.finish_reason.name}")
            return f"ERROR: The AI response was incomplete. Finish Reason: {candidate.finish_reason.name}. Please try again."

        # SIMPLIFIED: Directly use the 'response.text' property as shown in all documentation examples.
        # This is the idiomatic and most reliable way to get the full text output.
        # The SDK handles aggregating the parts for you.
        try:
            return response.text
        except Exception as e:
            logging.error(f"Failed to access response.text: {e}", exc_info=True)
            return f"ERROR: Failed to retrieve response content: {str(e)}"

    except Exception as e:
        logging.error(f"An unexpected error occurred during Gemini client setup or call: {e}", exc_info=True)
        st.exception(e)
        return f"ERROR: An unexpected application error occurred: {str(e)}"

def orchestrate_gemini_prompt_generation(creative_brief: str, api_key: str) -> str:
    """
    Takes a creative brief and an API key, then calls the Gemini API.
    This function isolates the API call from the data analysis.
    """
    if not api_key:
        return "ERROR: Gemini API key not found. Please provide your API key in the app to generate a prompt."
    
    # This function now exclusively handles the API call.
    return generate_polished_prompt_with_gemini(creative_brief, api_key)




# --- Helper Functions ---

def format_label(style: str) -> str:
    return style.upper() if style in ACRONYMS else style.title()

def _get_style_adjectives(styles: List[str]) -> Set[str]:
    """Helper function to retrieve unique adjectives for a list of styles."""
    adjectives = set()
    for style in styles:
        personality = STYLE_PERSONALITY_DICT.get(style, {})
        if "adjectives" in personality:
            adjectives.update(personality["adjectives"])
    return adjectives

def create_annotated_prompt_html(prompt_text: str, recognized_keywords: List[str], co_occurrence_data: Dict) -> str:
    """
    Generates an HTML string of the prompt with keywords highlighted and tooltips.
    """
    sorted_keywords = sorted(recognized_keywords, key=len, reverse=True)
    annotated_html = prompt_text
    
    for keyword in sorted_keywords:
        top_associations = co_occurrence_data.get(keyword, {})
        if top_associations:
            sorted_assocs = sorted(top_associations.items(), key=lambda x: x[1], reverse=True)[:4]
            tooltip_content = "&#10;".join([f"• {format_label(style)}: {weight:,}" for style, weight in sorted_assocs])
        else:
            tooltip_content = "No direct associations found."

        replacement_html = (
            f'<span class="highlight-keyword" data-tooltip="{tooltip_content}">'
            f'{keyword}'
            f'</span>'
        )
        pattern = re.compile(r'\b(' + re.escape(keyword) + r')\b(?![^<]*>)', re.IGNORECASE)
        annotated_html = pattern.sub(replacement_html, annotated_html)
        
    return annotated_html.replace("\n", "<br>")

# --- Core Logic Functions ---
def extract_keywords(prompt_text: str, valid_styles_set: Set[str]) -> List[str]:
    lower_prompt = prompt_text.lower()
    found_keywords = set()
    for style in valid_styles_set:
        # Use regex with word boundaries (\b) for precise matching
        if re.search(r'\b' + re.escape(style) + r'\b', lower_prompt):
            found_keywords.add(style)
    return sorted(list(found_keywords))

def calculate_influence_scores(keywords: List[str], co_occurrence_data: Dict) -> Dict[str, float]:
    influence_scores = defaultdict(float)
    for keyword in keywords:
        if keyword in co_occurrence_data:
            for associated_style, weight in co_occurrence_data[keyword].items():
                influence_scores[associated_style] += float(weight)
    return influence_scores

def calculate_cohesion(keywords: List[str], co_occurrence_data: Dict) -> float:
    if len(keywords) < 2:
        return 100.0
    connected_pairs = 0
    total_pairs = list(combinations(keywords, 2))
    for kw1, kw2 in total_pairs:
        if kw2 in co_occurrence_data.get(kw1, {}) or kw1 in co_occurrence_data.get(kw2, {}):
            connected_pairs += 1
    return (connected_pairs / len(total_pairs)) * 100.0 if total_pairs else 100.0

# --- Suggestion Engine ---
def generate_suggestions(cohesion_score: float, recognized_keywords: List[str], sorted_influences: List, co_occurrence_data: Dict) -> Dict:
    # Return a structured dictionary for richer UI rendering
    suggestion = {"title": "", "type": "info", "body": {}}

    # Scenario A: Low Cohesion - The Mediator & Tutor
    if cohesion_score < 40 and len(recognized_keywords) > 1:
        suggestion["title"] = "Low Cohesion Detected"
        suggestion["type"] = "error"
        
        G = nx.Graph()
        G.add_nodes_from(recognized_keywords)
        for kw1, kw2 in combinations(recognized_keywords, 2):
            if co_occurrence_data.get(kw1, {}).get(kw2): G.add_edge(kw1, kw2)
        factions = sorted(list(nx.connected_components(G)), key=len, reverse=True)

        if len(factions) > 1:
            faction_a, faction_b = factions[0], factions[1]
            
            # Strategy 1: Bridge the Gap
            bridge_candidates = {style for style, score in sorted_influences[:50]}
            bridge_scores = {}
            for candidate in bridge_candidates:
                affinity_a = sum(co_occurrence_data.get(kw, {}).get(candidate, 0) for kw in faction_a)
                affinity_b = sum(co_occurrence_data.get(kw, {}).get(candidate, 0) for kw in faction_b)
                if affinity_a > 0 and affinity_b > 0: bridge_scores[candidate] = affinity_a * affinity_b
            
            top_bridges = sorted(bridge_scores.items(), key=lambda x: x[1], reverse=True)[:3]

            # Strategy 2: Strengthen the Core
            # Identify the keywords in the smaller faction as candidates for removal/replacement
            conflict_keywords = faction_b
            # Suggest replacements by finding keywords related to the main faction
            main_faction_reinforcements = {
                style for kw in faction_a for style in co_occurrence_data.get(kw, {})
                if style not in recognized_keywords
            }
            replacement_suggestions = sorted(main_faction_reinforcements)[:3]

            suggestion["body"] = {
                "intro": f"Your prompt has two distinct stylistic groups:",
                "clusters": [list(faction_a), list(faction_b)],
                "strategies": {
                    "Bridge the Gap (Create a Fusion)": [f"Add `{bridge[0]}` to connect your ideas." for bridge in top_bridges],
                    "Strengthen the Core (Focus)": [f"Consider replacing `{kw}` with terms like `{', '.join(replacement_suggestions)}`." for kw in conflict_keywords]
                }
            }
            return suggestion

    # Scenario B: High Cohesion - The Reinforcer
    elif cohesion_score >= 75:
        suggestion["title"] = "Excellent Cohesion!"
        suggestion["type"] = "success"
        reinforcement_candidates = [style for style, score in sorted_influences[:7]]
        if reinforcement_candidates:
            suggestion["body"] = {
                "intro": "To make your prompt even more focused, consider adding these highly-related keywords:",
                "suggestions": [f"`{r}`" for r in reinforcement_candidates[:3]]
            }
        return suggestion

    # Scenario C: Moderate Cohesion or other cases - The Observer
    else:
        suggestion["title"] = "Moderate Cohesion"
        suggestion["type"] = "warning"
        suggestion["body"] = {
            "intro": "This can lead to unique genre fusions. If the results aren't what you expect, try adding more specific, related terms to guide the AI."
        }
        return suggestion

@st.cache_data
def analyze_explorer_styles(primary_style: str, secondary_style: Optional[str], negative_keywords: Optional[List[str]], creative_direction: Optional[str], co_occurrence_data: Dict) -> Dict:
    """
    Analyzes one or two styles for the Style Explorer mode.
    If a secondary style is provided, it performs a fusion analysis.
    """
    negative_keywords_set = set(negative_keywords) if negative_keywords else set()
    if not secondary_style:
        # --- SINGLE STYLE ANALYSIS (Original Logic) ---
        direct_associations = co_occurrence_data.get(primary_style, {})
        sorted_assocs = sorted(direct_associations.items(), key=lambda x: x[1], reverse=True)
        
        bar_chart_data = {
            style: math.log10(score + 1) for style, score in sorted_assocs[:15]
        }

        nodes, edges, node_ids = [], [], set()
        nodes.append({"id": primary_style, "label": format_label(primary_style), "size": 30, "color": PRIMARY_NODE_COLOR, "title": f"Selected Style: {format_label(primary_style)}"})
        node_ids.add(primary_style)

        first_degree_nodes = sorted_assocs[:7]
        for style, weight in first_degree_nodes:
            if style not in node_ids:
                nodes.append({"id": style, "label": format_label(style), "size": 18, "color": SECONDARY_NODE_COLOR, "title": f"Direct Association Strength: {weight:,}"})
                node_ids.add(style)
            edges.append({"from": primary_style, "to": style, "value": math.log10(weight + 1) * 2, "title": f"Association Strength: {weight:,}"})

        for first_degree_style, _ in first_degree_nodes:
            second_degree_assocs = sorted(co_occurrence_data.get(first_degree_style, {}).items(), key=lambda x: x[1], reverse=True)[:2]
            for second_degree_style, weight in second_degree_assocs:
                if second_degree_style not in node_ids:
                    nodes.append({"id": second_degree_style, "label": format_label(second_degree_style), "size": 10, "color": TERTIARY_NODE_COLOR, "title": f"Second-Degree Association Strength: {weight:,}"})
                    node_ids.add(second_degree_style)
                if second_degree_style in node_ids:
                     edges.append({"from": first_degree_style, "to": second_degree_style, "value": math.log10(weight + 1), "title": f"Association Strength: {weight:,}"})

        graph_data = {"nodes": nodes, "edges": edges}

        # --- PROMPT STARTER KIT (Single Style) - COMPILE ENHANCED BRIEF FOR GEMINI ---
        positive_adjectives = _get_style_adjectives([primary_style])
        
        creative_direction_section = f"\n        **Mandatory Creative Direction:** {creative_direction.strip()}" if creative_direction and creative_direction.strip() else ""

        if negative_keywords_set:
            negative_adjectives = _get_style_adjectives(list(negative_keywords_set))
            creative_brief = f"""
        **Primary Style:** {primary_style}
        **Creative Goal:** To generate a '{primary_style}' prompt that actively avoids the sensibilities of '{', '.join(negative_keywords_set)}'.
        **Emphasize These '{primary_style.title()}' Qualities:** {', '.join(positive_adjectives) or 'N/A'}
        **Steer Away From These Qualities:** {', '.join(negative_adjectives) or 'N/A'}{creative_direction_section}
        **Task:** Based on the data above, write an optimal Suno 4.5+ style prompt. Your primary goal is to find a creative angle that embodies the core '{primary_style}' qualities while actively contrasting with the specified negative qualities. Follow all rules from your system instruction.
            """.strip()
        else:
            # Brief without negative styles
            top_associated_styles = [style for style, score in sorted_assocs[:15]]
            top_moods = [m for m in top_associated_styles if m in MOOD_KEYWORDS][:3]
            top_instruments = [i for i in top_associated_styles if i in INSTRUMENT_KEYWORDS][:3]
            top_vocals = [v for v in top_associated_styles if v in VOCAL_KEYWORDS][:2]
            personality = STYLE_PERSONALITY_DICT.get(primary_style, {})
            
            creative_brief = f"""
        **Primary Style:** {primary_style}
        **Personality:** {personality}
        **Key Associated Moods:** {', '.join(top_moods) or 'N/A'}
        **Key Associated Instruments:** {', '.join(top_instruments) or 'N/A'}
        **Key Associated Vocals:** {', '.join(top_vocals) or 'N/A'}{creative_direction_section}
        **Task:** Based on the data above, write an optimal Suno 4.5+ style prompt. Your goal is to expand upon the core identity of the primary style, using the associated concepts to create a rich, vivid, and compelling narrative description for a song. Follow all rules from your system instruction.
            """.strip()

    else:
        # --- FUSION ANALYSIS ---
        assocs_a = co_occurrence_data.get(primary_style, {})
        assocs_b = co_occurrence_data.get(secondary_style, {})
        
        # 1. Bar Chart Data (with Synergy Boost)
        combined_scores = defaultdict(float)
        all_keys = set(assocs_a.keys()) | set(assocs_b.keys())
        for key in all_keys:
            score_a = assocs_a.get(key, 0)
            score_b = assocs_b.get(key, 0)
            combined_scores[key] = score_a + score_b
            # Synergy Boost for shared associates
            if score_a > 0 and score_b > 0:
                combined_scores[key] *= 1.5

        sorted_combined_assocs = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        bar_chart_data = {style: math.log10(score + 1) for style, score in sorted_combined_assocs[:15]}
        
        # 2. Network Graph Data
        nodes, edges, node_ids = [], [], set()
        top_assocs_a = {style for style, score in sorted(assocs_a.items(), key=lambda x:x[1], reverse=True)[:15]}
        top_assocs_b = {style for style, score in sorted(assocs_b.items(), key=lambda x:x[1], reverse=True)[:15]}
        bridge_nodes = top_assocs_a.intersection(top_assocs_b)

        # Add Primary Nodes
        for style in [primary_style, secondary_style]:
            nodes.append({"id": style, "label": format_label(style), "size": 30, "color": PRIMARY_NODE_COLOR, "title": f"Primary Style: {format_label(style)}"})
            node_ids.add(style)

        # Add Associated Nodes (Top 7 from each primary style)
        for source_style, assocs in [(primary_style, assocs_a), (secondary_style, assocs_b)]:
            top_7 = sorted(assocs.items(), key=lambda x: x[1], reverse=True)[:7]
            for assoc_style, weight in top_7:
                if assoc_style not in node_ids:
                    is_bridge = assoc_style in bridge_nodes
                    node_color = BRIDGE_NODE_COLOR if is_bridge else SECONDARY_NODE_COLOR
                    title_prefix = "Bridge Style" if is_bridge else "Direct Association"
                    nodes.append({"id": assoc_style, "label": format_label(assoc_style), "size": 18, "color": node_color, "title": f"{title_prefix}: {format_label(assoc_style)}<br>Strength: {weight:,}"})
                    node_ids.add(assoc_style)
                edges.append({"from": source_style, "to": assoc_style, "value": math.log10(weight + 1) * 2, "title": f"Association Strength: {weight:,}"})

        graph_data = {"nodes": nodes, "edges": edges}

        # --- PROMPT STARTER KIT (Fusion) - COMPILE BRIEF FOR GEMINI ---
        positive_adjectives = _get_style_adjectives([primary_style, secondary_style])
        creative_direction_section = f"\n        **Mandatory Creative Direction:** {creative_direction.strip()}" if creative_direction and creative_direction.strip() else ""

        if negative_keywords_set:
            negative_adjectives = _get_style_adjectives(list(negative_keywords_set))
            creative_brief = f"""
        **Primary Style 1:** {primary_style}
        **Primary Style 2:** {secondary_style}
        **Creative Goal:** To fuse '{primary_style}' and '{secondary_style}' while actively avoiding the sensibilities of '{', '.join(negative_keywords_set)}'.
        **Emphasize These Combined Qualities:** {', '.join(positive_adjectives) or 'N/A'}
        **Steer Away From These Qualities:** {', '.join(negative_adjectives) or 'N/A'}{creative_direction_section}
        **Task:** Based on the data above, write an optimal Suno 4.5+ style prompt. Your primary goal is to find a creative angle to fuse the two styles, resolving their contradictions into a believable and compelling musical idea, while actively contrasting with the specified negative qualities. Follow all rules from your system instruction.
            """.strip()
        else:
            # Brief for fusion without negative styles
            p1_personality = STYLE_PERSONALITY_DICT.get(primary_style, {})
            p2_personality = STYLE_PERSONALITY_DICT.get(secondary_style, {})
            creative_brief = f"""
        **Primary Style 1:** {primary_style}
        *   **Personality:** {p1_personality}

        **Primary Style 2:** {secondary_style}
        *   **Personality:** {p2_personality}

        **Contradiction to Resolve:** The core challenge is to blend the potentially conflicting personalities, moods, and aesthetics of {primary_style} and {secondary_style}.

        **Bridge Nodes (Shared Influences):** {', '.join(bridge_nodes) or 'None found, a true experimental fusion.'}
        **Combined Adjectives to Inspire Fusion:** {', '.join(positive_adjectives) or 'N/A'}{creative_direction_section}

        **Task:** Based on the data above, write an optimal Suno 4.5+ style prompt following all rules from your system instruction. Your primary goal is to find a creative angle to fuse the two styles, resolving their contradictions into a believable and compelling musical idea.
        """.strip()

    return {
        "bar_chart_data": bar_chart_data,
        "graph_data": graph_data,
    "creative_brief": creative_brief,
    "secondary_style_analyzed": secondary_style, # Pass this back for UI state
    }
# --- Main Orchestrator ---
@st.cache_data
def prepare_analysis_results(prompt_text: str, negative_keywords: List[str], default_styles: Set[str], co_occurrence_data: Dict) -> Dict[str, Any]:
    positive_keywords = extract_keywords(prompt_text, default_styles)
    negative_keywords_set = set(negative_keywords)

    # Ensure keywords are not in both positive and negative lists (negative wins)
    positive_keywords = [kw for kw in positive_keywords if kw not in negative_keywords_set]

    if not positive_keywords:
        return {"recognized_keywords": [], "error": "No valid Suno styles were found in the prompt."}

    # 1. Analyze the positive prompt in its original state

    # NOTE: The "Repulsive Force" logic has been removed. All analysis now uses the original, un-penalized scores.
    # This provides a more accurate and less misleading representation of the data.
    influence_scores = calculate_influence_scores(positive_keywords, co_occurrence_data)
    
    # Calculate cohesion score for suggestions
    cohesion_score = calculate_cohesion(positive_keywords, co_occurrence_data)

    # Filter out negative keywords from the final influence scores before display
    for neg_kw in negative_keywords_set:
        if neg_kw in influence_scores:
            del influence_scores[neg_kw]

    normalized_scores = {
        style: math.log10(score + 1)
        for style, score in influence_scores.items()
        if style not in positive_keywords
    }
    
    sorted_influences = sorted(normalized_scores.items(), key=lambda item: item[1], reverse=True)
    top_10_fingerprint = dict(sorted_influences[:10]) # Bug Fix: Changed from top_20 to top_10

    # 4. Generate suggestions based on the final, penalized data
    suggestion = generate_suggestions(cohesion_score, positive_keywords, sorted_influences, co_occurrence_data)
    
    # 5. Create annotated HTML for the prompt
    annotated_html = create_annotated_prompt_html(prompt_text, positive_keywords, co_occurrence_data)
    
    nodes, edges = [], []
    node_ids = set()
    top_associated_styles_for_graph = {style for style, score in sorted_influences[:20]}

    for keyword in positive_keywords:
        if keyword not in node_ids:
            nodes.append({"id": keyword, "label": format_label(keyword), "size": 25, "color": PRIMARY_NODE_COLOR, "title": f"Your Keyword: {format_label(keyword)}"})
            node_ids.add(keyword)

    min_log_score = sorted_influences[9][1] if len(sorted_influences) > 9 else 1
    max_log_score = sorted_influences[0][1] if sorted_influences else 1

    for style, score in sorted_influences:
        if style in top_associated_styles_for_graph and style not in node_ids:
            size_ratio = (score - min_log_score) / (max_log_score - min_log_score) if max_log_score > min_log_score else 0
            node_size = 12 + (8 * size_ratio)
            nodes.append({"id": style, "label": format_label(style), "size": node_size, "color": SECONDARY_NODE_COLOR, "title": f"Influence Score: {influence_scores.get(style, 0):,.0f}"})
            node_ids.add(style)

    for keyword in positive_keywords:
        for associated_style, weight in co_occurrence_data.get(keyword, {}).items():
            if associated_style in node_ids and associated_style != keyword and associated_style not in negative_keywords_set:
                edges.append({"from": keyword, "to": associated_style, "value": math.log10(weight + 1), "title": f"Association Strength: {weight:,}"})

    return {
        "recognized_keywords": positive_keywords, # Renamed for backward compatibility with UI
        "negative_keywords": negative_keywords,
        "cohesion_score": cohesion_score,
        "fingerprint": top_10_fingerprint,
        "graph_data": {"nodes": nodes, "edges": edges},
        "annotated_html": annotated_html,
        "suggestion": suggestion,
    }