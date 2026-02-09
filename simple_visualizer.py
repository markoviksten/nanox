"""
Ultimate GraphRAG Studio Knowledge Graph Visualizer
"""

import streamlit as st

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="GraphRAG Studio Knowledge Graph", layout="wide", page_icon="🕸️")

import networkx as nx
from pyvis.network import Network
import os
import tempfile
import numpy as np
import colorsys
from collections import Counter
import pandas as pd
import html

try:
    import community
    HAS_COMMUNITY = True
except ImportError:
    HAS_COMMUNITY = False

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 5px;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .node-detail-card {
        background: white;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .node-detail-label {
        font-weight: 600;
        color: #667eea;
        font-size: 0.85em;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .node-detail-value {
        color: #333;
        font-size: 0.95em;
        word-wrap: break-word;
    }
</style>
""", unsafe_allow_html=True)

st.title("🕸️ GraphRAG Studio Knowledge Graph Visualizer")

# Show warning about missing library if needed
if not HAS_COMMUNITY:
    st.warning("⚠️ Install python-louvain for community detection: `pip install python-louvain`")

# Määritä data-hakemistot
DATA_DIRS = {
    "Nano-1": "/data/nano1",
    "Nano-2": "/data/nano2",
    "Nano-3": "/data/nano3",
    "Nano-4": "/data/nano4",
    "Nano-5": "/data/nano5",
    "Nano-6": "/data/nano6",
    "Nano-7": "/data/nano7",
}

# GraphML data key mapping (customize based on your data)
DATA_KEY_LABELS = {
    'd0': 'Name',
    'd1': 'Type',
    'd2': 'Description',
    'd3': 'Chunk ID',
    'd4': 'Source Document',
    'd5': 'Timestamp',
    'd6': 'Additional Info',
    'entity_type': 'Entity Type',
    'description': 'Description',
    'source_id': 'Source',
    'weight': 'Weight'
}

def get_readable_label(key):
    """Convert data key to readable label"""
    return DATA_KEY_LABELS.get(key, key.replace('_', ' ').title())

def generate_colors(n: int) -> list:
    """Generate n distinct colors using HSV color space"""
    colors = []
    for i in range(n):
        hue = (i * 0.618033988749895) % 1.0
        saturation = 0.8
        value = 0.95
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        colors.append('#{:02x}{:02x}{:02x}'.format(
            int(rgb[0] * 255), 
            int(rgb[1] * 255), 
            int(rgb[2] * 255)
        ))
    return colors

def format_node_tooltip(node_id, node_data, degree):
    """Create rich HTML tooltip for node"""
    # Escape HTML characters
    safe_node_id = html.escape(str(node_id))
    
    tooltip = f"""
    <div style='
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        max-width: 400px;
        padding: 16px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    '>
        <div style='
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 12px;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(255,255,255,0.3);
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        '>
            📍 {safe_node_id}
        </div>
        
        <div style='
            background: rgba(255,255,255,0.15);
            padding: 8px 12px;
            border-radius: 6px;
            margin-bottom: 12px;
            backdrop-filter: blur(10px);
        '>
            <div style='font-size: 11px; opacity: 0.9; margin-bottom: 4px;'>CONNECTIONS</div>
            <div style='font-size: 20px; font-weight: 600;'>{degree} edges</div>
        </div>
    """
    
    # Add all node attributes
    for key, value in node_data.items():
        if key and value and key != 'id':
            label = get_readable_label(key)
            safe_value = html.escape(str(value))
            
            # Truncate long descriptions for tooltip
            display_value = safe_value
            if len(safe_value) > 200:
                display_value = safe_value[:200] + '...'
            
            # Special formatting for different types
            if key in ['d2', 'description']:  # Description fields
                tooltip += f"""
                <div style='
                    margin-top: 12px;
                    padding: 10px;
                    background: rgba(255,255,255,0.1);
                    border-radius: 6px;
                    border-left: 3px solid rgba(255,255,255,0.5);
                '>
                    <div style='font-size: 11px; opacity: 0.9; margin-bottom: 4px;'>{label.upper()}</div>
                    <div style='font-size: 13px; line-height: 1.5;'>{display_value}</div>
                </div>
                """
            else:
                tooltip += f"""
                <div style='margin-top: 8px;'>
                    <span style='font-size: 11px; opacity: 0.8;'>{label}:</span>
                    <span style='font-size: 13px; font-weight: 500; margin-left: 6px;'>{display_value}</span>
                </div>
                """
    
    tooltip += "</div>"
    return tooltip

def display_node_details_sidebar(node_id, node_data, graph):
    """Display detailed node information in sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📋 Selected Node Details")
    
    # Node ID as header
    st.sidebar.markdown(f"**🎯 {node_id}**")
    
    # Basic metrics
    degree = graph.degree[node_id]
    neighbors = list(graph.neighbors(node_id))
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Degree", degree)
    with col2:
        st.metric("Neighbors", len(neighbors))
    
    # All attributes in expandable sections
    st.sidebar.markdown("#### 🔍 Attributes")
    
    # Primary info (always visible)
    for key in ['d0', 'd1', 'entity_type', 'type']:
        if key in node_data and node_data[key]:
            label = get_readable_label(key)
            st.sidebar.markdown(f"**{label}:** {node_data[key]}")
    
    # Description (collapsible if long)
    for key in ['d2', 'description']:
        if key in node_data and node_data[key]:
            desc = str(node_data[key])
            if len(desc) > 100:
                with st.sidebar.expander("📝 Description"):
                    st.markdown(desc)
            else:
                st.sidebar.markdown(f"**Description:** {desc}")
    
    # Other metadata
    with st.sidebar.expander("📊 Metadata", expanded=True):
        for key, value in node_data.items():
            if key and value and key not in ['id', 'd0', 'd1', 'd2', 'entity_type', 'type', 'description']:
                label = get_readable_label(key)
                value_str = str(value)
                if len(value_str) > 50:
                    st.text(f"{label}:")
                    st.caption(value_str)
                else:
                    st.text(f"{label}: {value_str}")
    
    # Neighbors list
    if neighbors:
        with st.sidebar.expander(f"🔗 {len(neighbors)} Neighbors", expanded=False):
            for i, neighbor in enumerate(neighbors[:20], 1):
                # Get edge data if available
                edge_data = graph.get_edge_data(node_id, neighbor)
                if edge_data:
                    weight = edge_data.get('weight', '')
                    if weight:
                        st.text(f"{i}. {neighbor} (weight: {weight})")
                    else:
                        st.text(f"{i}. {neighbor}")
                else:
                    st.text(f"{i}. {neighbor}")
            
            if len(neighbors) > 20:
                st.caption(f"... and {len(neighbors) - 20} more")
    
    # Centrality metrics
    try:
        with st.sidebar.expander("📈 Centrality Metrics"):
            betweenness = nx.betweenness_centrality(graph)[node_id]
            st.metric("Betweenness", f"{betweenness:.4f}")
            
            try:
                closeness = nx.closeness_centrality(graph)[node_id]
                st.metric("Closeness", f"{closeness:.4f}")
            except:
                pass
            
            try:
                pagerank = nx.pagerank(graph)[node_id]
                st.metric("PageRank", f"{pagerank:.4f}")
            except:
                pass
    except:
        pass

# Initialize session state
if 'filter_min_degree' not in st.session_state:
    st.session_state.filter_min_degree = 0
if 'filter_max_degree' not in st.session_state:
    st.session_state.filter_max_degree = 1000
if 'selected_communities' not in st.session_state:
    st.session_state.selected_communities = []
if 'highlight_neighbors' not in st.session_state:
    st.session_state.highlight_neighbors = False
if 'ego_node' not in st.session_state:
    st.session_state.ego_node = None
if 'ego_radius' not in st.session_state:
    st.session_state.ego_radius = 1
if 'selected_node_for_details' not in st.session_state:
    st.session_state.selected_node_for_details = None

# Sidebar
st.sidebar.title("⚙️ Settings")

# Instance selection
selected_instance = st.sidebar.selectbox("Select Instance", list(DATA_DIRS.keys()))
working_dir = DATA_DIRS[selected_instance]

st.sidebar.info(f"📁 Data: `{working_dir}`")

# Tarkista että hakemisto on olemassa
if not os.path.exists(working_dir):
    st.error(f"❌ Directory not found: {working_dir}")
    st.stop()

# Etsi GraphML-tiedosto
graph_file = os.path.join(working_dir, "graph_chunk_entity_relation.graphml")

if not os.path.exists(graph_file):
    st.warning(f"⚠️ No graph data found in {selected_instance}")
    st.info("Run some queries in LightRAG to generate graph data first.")
    st.stop()

# Lataa graafi
@st.cache_data
def load_graph(filepath):
    try:
        G = nx.read_graphml(filepath)
        return G
    except Exception as e:
        st.error(f"Error loading graph: {e}")
        return None

G_original = load_graph(graph_file)

if G_original is None:
    st.stop()

# Filtering options
st.sidebar.subheader("🔧 Graph Filtering")

filter_mode = st.sidebar.radio(
    "Filter Mode",
    ["Full Graph", "Degree Filter", "Ego Network", "Community Filter", "K-Core", "By Type"]
)

G = G_original.copy()

if filter_mode == "Degree Filter":
    degrees = dict(G.degree())
    max_deg = max(degrees.values())
    
    min_degree = st.sidebar.slider("Minimum Degree", 0, max_deg, 0)
    max_degree = st.sidebar.slider("Maximum Degree", 0, max_deg, max_deg)
    
    # Filter nodes by degree
    nodes_to_keep = [n for n, d in degrees.items() if min_degree <= d <= max_degree]
    G = G.subgraph(nodes_to_keep).copy()
    
    st.sidebar.success(f"Filtered to {G.number_of_nodes()} nodes")

elif filter_mode == "Ego Network":
    all_nodes = list(G_original.nodes())
    ego_node = st.sidebar.selectbox("Select Center Node", all_nodes)
    ego_radius = st.sidebar.slider("Radius (hops)", 1, 5, 1)
    
    if ego_node:
        ego_graph = nx.ego_graph(G_original, ego_node, radius=ego_radius)
        G = ego_graph
        st.sidebar.success(f"Ego network: {G.number_of_nodes()} nodes")

elif filter_mode == "K-Core":
    k_value = st.sidebar.slider("K-Core value", 1, 10, 2)
    try:
        G = nx.k_core(G_original, k=k_value)
        st.sidebar.success(f"K-Core ({k_value}): {G.number_of_nodes()} nodes")
    except:
        st.sidebar.error("Cannot compute K-Core for this graph")
        G = G_original.copy()

elif filter_mode == "By Type":
    # Get all unique types from nodes
    all_types = set()
    for node in G_original.nodes():
        node_data = G_original.nodes[node]
        node_type = node_data.get('d1') or node_data.get('type') or node_data.get('entity_type', 'unknown')
        all_types.add(str(node_type))
    
    selected_types = st.sidebar.multiselect(
        "Select Node Types",
        sorted(all_types),
        default=sorted(all_types)
    )
    
    if selected_types:
        nodes_to_keep = []
        for node in G_original.nodes():
            node_data = G_original.nodes[node]
            node_type = node_data.get('d1') or node_data.get('type') or node_data.get('entity_type', 'unknown')
            if str(node_type) in selected_types:
                nodes_to_keep.append(node)
        
        G = G_original.subgraph(nodes_to_keep).copy()
        st.sidebar.success(f"Filtered to {G.number_of_nodes()} nodes")

# Community detection
@st.cache_data
def detect_communities(_graph):
    if HAS_COMMUNITY:
        try:
            communities = community.best_partition(_graph)
            num_communities = len(set(communities.values()))
            return communities, num_communities
        except:
            return None, 0
    return None, 0

communities, num_communities = detect_communities(G)

if filter_mode == "Community Filter" and communities:
    available_communities = sorted(set(communities.values()))
    selected_communities = st.sidebar.multiselect(
        "Select Communities",
        available_communities,
        default=available_communities[:3] if len(available_communities) > 3 else available_communities
    )
    
    if selected_communities:
        nodes_to_keep = [n for n, c in communities.items() if c in selected_communities]
        G = G.subgraph(nodes_to_keep).copy()
        # Recalculate communities for filtered graph
        communities, num_communities = detect_communities(G)
        st.sidebar.success(f"Showing {len(selected_communities)} communities with {G.number_of_nodes()} nodes")

# Enhanced Statistics Dashboard
st.subheader("📊 Graph Statistics Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Nodes", G.number_of_nodes(), 
              delta=f"{G.number_of_nodes() - G_original.number_of_nodes()}" if G != G_original else None)
with col2:
    st.metric("Edges", G.number_of_edges(),
              delta=f"{G.number_of_edges() - G_original.number_of_edges()}" if G != G_original else None)
with col3:
    density = nx.density(G)
    st.metric("Density", f"{density:.4f}")
with col4:
    if communities:
        st.metric("Communities", num_communities)
    else:
        avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes() if G.number_of_nodes() > 0 else 0
        st.metric("Avg Degree", f"{avg_degree:.2f}")
with col5:
    try:
        clustering = nx.average_clustering(G)
        st.metric("Clustering", f"{clustering:.4f}")
    except:
        st.metric("Clustering", "N/A")

# Degree Distribution Chart
with st.expander("📈 Degree Distribution", expanded=False):
    degrees = [d for n, d in G.degree()]
    degree_counts = Counter(degrees)
    
    df_degrees = pd.DataFrame([
        {'Degree': k, 'Count': v} for k, v in sorted(degree_counts.items())
    ])
    
    if len(df_degrees) > 0:
        st.bar_chart(df_degrees.set_index('Degree'))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Min Degree", min(degrees))
        with col2:
            st.metric("Max Degree", max(degrees))
        with col3:
            st.metric("Median Degree", int(np.median(degrees)))

# Visualization Settings
st.sidebar.subheader("🎨 Visualization Settings")

# Layout selection with descriptions
layout_options = {
    "Spring (Force-directed)": "Physics-based, good for general graphs",
    "Circular": "Nodes in a circle, good for cycles",
    "Shell": "Concentric shells by community",
    "Kamada-Kawai": "Energy minimization, aesthetic",
    "Spectral": "Based on graph spectrum",
    "Random": "Random positioning"
}

layout_type = st.sidebar.selectbox(
    "Layout Algorithm",
    list(layout_options.keys()),
    format_func=lambda x: f"{x}",
    help="Choose layout algorithm"
)

st.sidebar.caption(layout_options[layout_type])

# Display settings
height = st.sidebar.slider("Height (px)", 400, 1200, 800, 50)
physics = st.sidebar.checkbox("Enable Physics", value=True, help="Interactive node dragging")
show_labels = st.sidebar.checkbox("Show Node Labels", value=True)

# Node size options
size_by = st.sidebar.selectbox(
    "Node Size By",
    ["Degree", "Betweenness", "Closeness", "PageRank", "Uniform"],
    help="Metric for node sizing"
)

# Advanced settings
with st.sidebar.expander("⚙️ Advanced Settings"):
    node_size_multiplier = st.slider("Node Size Multiplier", 0.5, 3.0, 1.0, 0.1)
    edge_width = st.slider("Edge Width", 0.5, 5.0, 1.0, 0.5)
    edge_opacity = st.slider("Edge Opacity", 0.1, 1.0, 0.5, 0.1)
    
    color_by = st.selectbox(
        "Color Nodes By",
        ["Community", "Type", "Degree", "Centrality", "Uniform"]
    )
    
    show_edge_labels = st.checkbox("Show Edge Labels", value=False)
    curved_edges = st.checkbox("Curved Edges", value=True)

# Background color picker
with st.sidebar.expander("🎨 Color Theme"):
    bg_color = st.color_picker("Background Color", "#1a1a1a")
    font_color = st.color_picker("Font Color", "#ffffff")
    
    theme_preset = st.selectbox(
        "Preset Themes",
        ["Dark", "Light", "Blue", "Purple", "Matrix"]
    )
    
    if theme_preset == "Light":
        bg_color = "#ffffff"
        font_color = "#000000"
    elif theme_preset == "Blue":
        bg_color = "#0a1929"
        font_color = "#66b2ff"
    elif theme_preset == "Purple":
        bg_color = "#1a0033"
        font_color = "#cc99ff"
    elif theme_preset == "Matrix":
        bg_color = "#000000"
        font_color = "#00ff00"

# Node search with autocomplete
st.sidebar.subheader("🔍 Node Search & Focus")
search_query = st.sidebar.text_input("Search for node", placeholder="Type to search...")

if search_query:
    matching_nodes = [n for n in G.nodes() if search_query.lower() in str(n).lower()]
    if matching_nodes:
        st.sidebar.success(f"Found {len(matching_nodes)} nodes")
        selected_node = st.sidebar.selectbox("Select node", matching_nodes[:20])
        
        if selected_node:
            # Show detailed info
            node_data = G.nodes[selected_node]
            display_node_details_sidebar(selected_node, node_data, G)
            
            highlight_neighbors = st.sidebar.checkbox(
                "Highlight Neighbors", 
                value=False,
                help="Highlight this node and its neighbors"
            )
            
            if highlight_neighbors:
                st.session_state.ego_node = selected_node
                st.session_state.highlight_neighbors = True
    else:
        st.sidebar.warning("No matching nodes found")

# Calculate layout
@st.cache_data
def calculate_layout(_graph, layout_type, communities_dict):
    if "Spring" in layout_type:
        pos = nx.spring_layout(_graph, dim=2, k=2.0, iterations=100, seed=42)
    elif layout_type == "Circular":
        pos = nx.circular_layout(_graph)
    elif layout_type == "Shell":
        if communities_dict:
            comm_lists = [[] for _ in range(max(communities_dict.values()) + 1)]
            for node, comm in communities_dict.items():
                if node in _graph.nodes():
                    comm_lists[comm].append(node)
            comm_lists = [cl for cl in comm_lists if cl]
            pos = nx.shell_layout(_graph, comm_lists)
        else:
            pos = nx.shell_layout(_graph)
    elif layout_type == "Kamada-Kawai":
        try:
            pos = nx.kamada_kawai_layout(_graph)
        except:
            pos = nx.spring_layout(_graph, seed=42)
    elif layout_type == "Spectral":
        try:
            pos = nx.spectral_layout(_graph)
        except:
            pos = nx.spring_layout(_graph, seed=42)
    else:
        np.random.seed(42)
        pos = {node: np.random.rand(2) for node in _graph.nodes()}
    
    return pos

pos = calculate_layout(G, layout_type, communities)

# Calculate centrality measures
@st.cache_data
def calculate_centrality(_graph, measure_type):
    if measure_type == "Betweenness":
        return nx.betweenness_centrality(_graph)
    elif measure_type == "Closeness":
        return nx.closeness_centrality(_graph)
    elif measure_type == "PageRank":
        return nx.pagerank(_graph)
    else:
        return {node: 1.0 for node in _graph.nodes()}

# Calculate node colors and sizes
@st.cache_data
def calculate_node_properties(_graph, communities_dict, color_by, size_by, pos_dict):
    degrees = dict(_graph.degree())
    max_degree = max(degrees.values()) if degrees else 1
    min_degree = min(degrees.values()) if degrees else 1
    
    node_colors = {}
    node_sizes = {}
    
    # Calculate size metric
    if size_by == "Degree":
        size_metric = degrees
    elif size_by in ["Betweenness", "Closeness", "PageRank"]:
        size_metric = calculate_centrality(_graph, size_by)
    else:
        size_metric = {node: 1.0 for node in _graph.nodes()}
    
    # Normalize size metric
    if size_metric:
        max_size = max(size_metric.values())
        min_size = min(size_metric.values())
    
    # Generate community colors
    if communities_dict and color_by == "Community":
        num_comm = len(set(communities_dict.values()))
        comm_colors = generate_colors(num_comm)
    
    # Generate type colors
    if color_by == "Type":
        all_types = set()
        for node in _graph.nodes():
            node_data = _graph.nodes[node]
            node_type = node_data.get('d1') or node_data.get('type') or node_data.get('entity_type', 'unknown')
            all_types.add(str(node_type))
        type_colors = {t: generate_colors(len(all_types))[i] for i, t in enumerate(sorted(all_types))}
    
    # Calculate centrality for coloring if needed
    if color_by == "Centrality":
        centrality = nx.betweenness_centrality(_graph)
        max_cent = max(centrality.values()) if centrality else 1
        min_cent = min(centrality.values()) if centrality else 0
    
    for node in _graph.nodes():
        # Calculate size
        if max_size != min_size and size_metric:
            normalized = (size_metric[node] - min_size) / (max_size - min_size)
            size = 10 + normalized * 40
        else:
            size = 25
        node_sizes[node] = size
        
        # Calculate color
        if color_by == "Community" and communities_dict and node in communities_dict:
            comm_id = communities_dict[node]
            node_colors[node] = comm_colors[comm_id]
        elif color_by == "Type":
            node_data = _graph.nodes[node]
            node_type = node_data.get('d1') or node_data.get('type') or node_data.get('entity_type', 'unknown')
            node_colors[node] = type_colors.get(str(node_type), '#6baed6')
        elif color_by == "Degree":
            normalized = (degrees[node] - min_degree) / (max_degree - min_degree) if max_degree != min_degree else 0.5
            r = int(normalized * 255)
            b = int((1 - normalized) * 255)
            node_colors[node] = f'#{r:02x}80{b:02x}'
        elif color_by == "Centrality":
            normalized = (centrality[node] - min_cent) / (max_cent - min_cent) if max_cent != min_cent else 0.5
            r = 255
            g = int((1 - normalized) * 255)
            node_colors[node] = f'#{r:02x}{g:02x}00'
        else:
            node_colors[node] = '#6baed6'
    
    return node_colors, node_sizes

node_colors, node_sizes = calculate_node_properties(G, communities, color_by, size_by, pos)

# Highlight neighbors if selected
if st.session_state.highlight_neighbors and st.session_state.ego_node:
    ego_node = st.session_state.ego_node
    if ego_node in G.nodes():
        neighbors = list(G.neighbors(ego_node))
        
        node_colors[ego_node] = '#ff6600'
        node_sizes[ego_node] = node_sizes[ego_node] * 1.5
        
        for neighbor in neighbors:
            node_colors[neighbor] = '#ffcc00'

# Create PyVis network with rich tooltips
@st.cache_data
def create_network(_graph, _pos, _node_colors, _node_sizes, _height, _physics, _show_labels, 
                   _node_size_mult, _edge_width, _edge_opacity, _bg_color, _font_color, 
                   _show_edge_labels, _curved_edges):
    net = Network(
        height=f"{_height}px", 
        width="100%", 
        bgcolor=_bg_color, 
        font_color=_font_color,
        cdn_resources='in_line'
    )
    
    # Set physics
    if _physics:
        net.barnes_hut()
    else:
        net.toggle_physics(False)
    
    # Add nodes with rich tooltips
    for node in _graph.nodes():
        node_data = _graph.nodes[node]
        label = str(node)[:30] if _show_labels else ""
        degree = _graph.degree[node]
        
        # Create rich HTML tooltip
        tooltip = format_node_tooltip(node, node_data, degree)
        
        x, y = _pos[node]
        color = _node_colors.get(node, '#6baed6')
        size = _node_sizes.get(node, 20) * _node_size_mult
        
        net.add_node(
            node, 
            label=label, 
            title=tooltip, 
            size=size,
            color=color,
            x=x * 600,
            y=y * 600
        )
    
    # Add edges with tooltips
    for source, target, data in _graph.edges(data=True):
        weight = data.get('weight', 1)
        
        # Create edge tooltip
        if _show_edge_labels and data:
            edge_parts = [f"<div style='padding: 8px; font-family: sans-serif;'>"]
            edge_parts.append(f"<b>{source}</b> → <b>{target}</b><br><br>")
            for k, v in data.items():
                if v and k not in ['source', 'target']:
                    label = get_readable_label(k)
                    edge_parts.append(f"<b>{label}:</b> {v}<br>")
            edge_parts.append("</div>")
            edge_title = "".join(edge_parts)
        else:
            edge_title = f"{source} → {target}"
        
        net.add_edge(
            source, 
            target, 
            value=weight * _edge_width,
            title=edge_title,
            color={'opacity': _edge_opacity},
            smooth=_curved_edges
        )
    
    return net

# Create network with current settings
st.subheader(f"🗺️ Knowledge Graph: {selected_instance}")

if filter_mode != "Full Graph":
    st.info(f"🔍 Filter Active: {filter_mode} | Showing {G.number_of_nodes()}/{G_original.number_of_nodes()} nodes, {G.number_of_edges()}/{G_original.number_of_edges()} edges")

# Debug check
if G.number_of_nodes() == 0:
    st.warning("⚠️ No nodes to display after filtering!")
    st.stop()

with st.spinner("🎨 Rendering graph..."):
    net = create_network(
        G, pos, node_colors, node_sizes, height, physics, show_labels,
        node_size_multiplier, edge_width, edge_opacity, bg_color, font_color, 
        show_edge_labels, curved_edges
    )
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode='w', encoding='utf-8') as f:
        net.save_graph(f.name)
        with open(f.name, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        
        # Render without scrolling
        st.components.v1.html(html_content, height=height+100, scrolling=False)
        os.unlink(f.name)

# Quick Actions
st.subheader("⚡ Quick Actions")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔄 Reset All Filters"):
        st.session_state.filter_min_degree = 0
        st.session_state.highlight_neighbors = False
        st.session_state.ego_node = None
        st.rerun()

with col2:
    if st.button("📸 Export View"):
        st.info("Right-click on the graph and select 'Save image as...'")

with col3:
    if st.button("🎯 Find Central Nodes"):
        centrality = nx.betweenness_centrality(G)
        top_central = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        st.write("**Top 5 Central Nodes:**")
        for node, cent in top_central:
            st.text(f"• {node}: {cent:.4f}")

with col4:
    if st.button("🔗 Find Bridges"):
        try:
            bridges = list(nx.bridges(G))
            st.write(f"**Found {len(bridges)} bridges:**")
            for u, v in bridges[:5]:
                st.text(f"• {u} ↔ {v}")
            if len(bridges) > 5:
                st.text(f"... and {len(bridges) - 5} more")
        except:
            st.warning("Cannot find bridges (graph may not be connected)")

# Advanced Graph Analysis
with st.expander("🔬 Advanced Graph Analysis", expanded=False):
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Centrality", "🌐 Communities", "📈 Metrics", "🔍 Paths"])
    
    with tab1:
        st.markdown("### Centrality Measures")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Top 10 by Degree**")
            degrees = dict(G.degree())
            top_degree = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]
            for node, deg in top_degree:
                st.text(f"{node}: {deg}")
        
        with col2:
            st.markdown("**Top 10 by PageRank**")
            try:
                pagerank = nx.pagerank(G)
                top_pr = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
                for node, pr in top_pr:
                    st.text(f"{node}: {pr:.4f}")
            except:
                st.text("Cannot calculate PageRank")
    
    with tab2:
        if communities:
            st.markdown("### Community Structure")
            
            comm_sizes = Counter(communities.values())
            df_comm = pd.DataFrame([
                {'Community': k, 'Size': v} for k, v in sorted(comm_sizes.items())
            ])
            
            st.dataframe(df_comm, use_container_width=True)
            st.bar_chart(df_comm.set_index('Community'))
            
            try:
                mod = community.modularity(communities, G)
                st.metric("Modularity", f"{mod:.4f}", help="Higher is better (typically 0.3-0.7)")
            except:
                pass
        else:
            st.info("Community detection not available")
    
    with tab3:
        st.markdown("### Graph Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Avg Clustering", f"{nx.average_clustering(G):.4f}")
            st.metric("Transitivity", f"{nx.transitivity(G):.4f}")
            
            try:
                st.metric("Assortativity", f"{nx.degree_assortativity_coefficient(G):.4f}")
            except:
                pass
        
        with col2:
            if nx.is_connected(G):
                st.metric("Diameter", nx.diameter(G))
                st.metric("Avg Path Length", f"{nx.average_shortest_path_length(G):.4f}")
                st.metric("Radius", nx.radius(G))
            else:
                components = list(nx.connected_components(G))
                st.metric("Components", len(components))
                st.metric("Largest Component", len(max(components, key=len)))
    
    with tab4:
        st.markdown("### Path Analysis")
        
        col1, col2 = st.columns(2)
        
        all_nodes_list = list(G.nodes())
        
        with col1:
            source_node = st.selectbox("Source Node", all_nodes_list, key="path_source")
        
        with col2:
            target_node = st.selectbox("Target Node", all_nodes_list, key="path_target")
        
        if source_node and target_node and source_node != target_node:
            try:
                if nx.has_path(G, source_node, target_node):
                    shortest_path = nx.shortest_path(G, source_node, target_node)
                    st.success(f"Shortest path length: {len(shortest_path) - 1}")
                    st.text(" → ".join(str(n) for n in shortest_path))
                    
                    all_paths = list(nx.all_simple_paths(G, source_node, target_node, cutoff=5))
                    if all_paths:
                        st.info(f"Found {len(all_paths)} paths (max length 5)")
                else:
                    st.warning("No path exists between these nodes")
            except Exception as e:
                st.error(f"Error calculating path: {e}")

# Export Options
with st.expander("💾 Export & Download Options"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Export GEXF"):
            export_path = os.path.join(working_dir, f"{selected_instance}_export.gexf")
            nx.write_gexf(G, export_path)
            st.success(f"✅ Exported to {export_path}")
    
    with col2:
        if st.button("Export GraphML"):
            export_path = os.path.join(working_dir, f"{selected_instance}_export.graphml")
            nx.write_graphml(G, export_path)
            st.success(f"✅ Exported to {export_path}")
    
    with col3:
        if st.button("Export Adjacency"):
            export_path = os.path.join(working_dir, f"{selected_instance}_adjacency.csv")
            adj_matrix = nx.to_pandas_adjacency(G)
            adj_matrix.to_csv(export_path)
            st.success(f"✅ Exported to {export_path}")
    
    with col4:
        if st.button("Export Node List"):
            export_path = os.path.join(working_dir, f"{selected_instance}_nodes.csv")
            node_data = []
            for node in G.nodes():
                data = {'node': node, 'degree': G.degree[node]}
                data.update(G.nodes[node])
                node_data.append(data)
            df = pd.DataFrame(node_data)
            df.to_csv(export_path, index=False)
            st.success(f"✅ Exported to {export_path}")

# Comparison with other instances
with st.expander("📊 Compare with Other Instances"):
    st.markdown("### Instance Comparison")
    
    comparison_data = []
    for instance, path in DATA_DIRS.items():
        graph_path = os.path.join(path, "graph_chunk_entity_relation.graphml")
        if os.path.exists(graph_path):
            try:
                g_temp = nx.read_graphml(graph_path)
                comparison_data.append({
                    'Instance': instance,
                    'Nodes': g_temp.number_of_nodes(),
                    'Edges': g_temp.number_of_edges(),
                    'Density': f"{nx.density(g_temp):.4f}",
                    'Avg Degree': f"{sum(dict(g_temp.degree()).values()) / g_temp.number_of_nodes():.2f}"
                })
            except:
                pass
    
    if comparison_data:
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True)

# Info
with st.expander("ℹ️ About & Help"):
    st.markdown("""
    ### GraphRAG Studio Knowledge Graph Visualizer - Ultimate Edition
    
    **🎯 Key Features:**
    
    **Filtering:**
    - 🔢 Degree-based filtering
    - 🎯 Ego network (show node + neighbors)
    - 🔧 K-core decomposition
    - 🌐 Community-based filtering
    - 🏷️ Filter by node type
    
    **Visualization:**
    - 6+ layout algorithms
    - Dynamic node sizing (degree, centrality, PageRank)
    - Multiple coloring schemes (Community, Type, Degree, Centrality)
    - Theme presets
    - Curved/straight edges
    - Adjustable physics
    - **Rich tooltips with all node attributes**
    
    **Analysis:**
    - Community detection (Louvain)
    - Centrality measures
    - Path finding
    - Bridge detection
    - Degree distribution
    - Clustering coefficients
    
    **Export:**
    - GEXF, GraphML formats
    - Adjacency matrix
    - Node lists with attributes
    - Visual screenshots
    
    **Interactivity:**
    - Node search & selection
    - **Detailed node information panel**
    - Neighbor highlighting
    - Rich tooltips with all metadata
    - Zoom & pan
    - Drag nodes
    
    **🎨 Usage Tips:**
    1. Hover over nodes to see all attributes in a rich tooltip
    2. Use search to find and inspect specific nodes
    3. Filter by type to focus on specific entity types
    4. Color by type or community to see patterns
    5. Try different layouts for different insights
    
    **Made with ❤️ using:**
    - Streamlit (UI)
    - NetworkX (Graph analysis)
    - PyVis (Visualization)
    - Python-Louvain (Community detection)
    - Pandas (Data handling)
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("🚀 **GraphRAG Studio v2.0**")
st.sidebar.caption("Ultimate Edition - Enhanced")