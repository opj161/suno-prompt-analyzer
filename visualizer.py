# suno-prompt-analyzer/visualizer.py

from typing import Dict, Any
import plotly.graph_objects as go
from pyvis.network import Network
# Match the color from the analyzer for consistency
SECONDARY_NODE_COLOR = "#4682B4"

def create_ranked_bar_chart(data: Dict[str, float], title: str, xaxis_label: str) -> go.Figure:
    """
    Creates a generic horizontal bar chart for ranked data.

    Args:
        data: A dictionary of items and their scores, sorted descending.
        title: The title for the chart.
        xaxis_label: The label for the x-axis.

    Returns:
        A Plotly Figure object ready for rendering.
    """
    # Reverse the data for horizontal bar chart (highest on top)
    if not data:
        return go.Figure().update_layout(title_text=title, annotations=[dict(text="No data available.", showarrow=False)])

    labels = list(data.keys())[::-1]
    values = list(data.values())[::-1]

    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker=dict(color=SECONDARY_NODE_COLOR)
    ))

    fig.update_layout(
        title_text=f'<b>{title}</b>',
        xaxis_title=xaxis_label,
        yaxis_title='Associated Styles',
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False,
        yaxis=dict(
            automargin=True
        )
    )

    return fig


def create_association_map(graph_data: Dict[str, Any]) -> Network:
    """
    Creates an interactive force-directed network graph.

    Args:
        graph_data: A dictionary containing 'nodes' and 'edges' lists.

    Returns:
        A Pyvis Network object.
    """
    net = Network(height="600px", width="100%", notebook=True, cdn_resources='in_line')
    
    # Add nodes
    for node in graph_data['nodes']:
        net.add_node(
            n_id=node['id'],
            label=node['label'],
            size=node['size'],
            color=node['color'],
            title=node['title']
        )
    
    # Add edges
    for edge in graph_data['edges']:
        net.add_edge(
            source=edge['from'],
            to=edge['to'],
            value=edge['value'],
            title=edge['title']
        )
    
    # Set physics options for a better layout
    net.set_options("""
    var options = {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -3000,
          "centralGravity": 0.1,
          "springLength": 150,
          "springConstant": 0.05,
          "damping": 0.09,
          "avoidOverlap": 0.1
        },
        "maxVelocity": 50,
        "minVelocity": 0.1,
        "solver": "barnesHut",
        "stabilization": {
          "enabled": true,
          "iterations": 1000,
          "updateInterval": 25
        }
      }
    }
    """)

    return net