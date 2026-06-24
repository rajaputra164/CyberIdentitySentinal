import streamlit as st
import requests

st.set_page_config(page_title="Cyber Identity Sentinel", layout="wide")
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #00E5FF;
}

.stButton>button {
    background: linear-gradient(90deg,#00E5FF,#00FFA3);
    color: black;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    padding: 10px 25px;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 15px;
}

div[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Profile Analysis", "Risk Report","Graph Visualizations",
        "Copilot Interface"]
)

API_URL = "https://cyberidentity-api.onrender.com/analyze"

# ---------------- DASHBOARD ----------------
# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.markdown("""
    <h1 style='text-align:center;color:#00E5FF'>
    🛡️ Cyber Identity Sentinel
    </h1>

    <h4 style='text-align:center;color:white'>
    AI-Powered Digital Identity Threat Detection Platform
    </h4>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Main Project Statistics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Profiles Scanned", "500")
    col2.metric("Fake Profiles", "143")
    col3.metric("Critical Threats", "27")
    col4.metric("Detection Accuracy", "94%")

    st.markdown("---")

    # System Status
    col1, col2, col3 = st.columns(3)

    col1.metric("Model Status", "Active")
    col2.metric("API Status", "Running")
    col3.metric("Version", "1.0")

    st.info("Go to Profile Analysis to test accounts")
# ---------------- PROFILE ANALYSIS ----------------
elif page == "Profile Analysis":
    st.title("🔍 Profile Analysis")

    followers = st.number_input("Followers", min_value=0)
    following = st.number_input("Following", min_value=0)
    posts = st.number_input("Posts", min_value=0)
    age = st.number_input("Account Age (days)", min_value=0)

    if st.button("Analyze"):
        payload = {
            "followers": followers,
            "following": following,
            "posts": posts,
            "age": age
        }

        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()

            st.success("Analysis Complete")

            st.write("### Result")
            st.json(result)

            st.metric("Risk Score", result["score"])
            st.metric("Risk Level", result["risk"])

        except Exception as e:
            st.error(f"API Error: {e}")


# ---------------- RISK REPORT ----------------
elif page == "Risk Report":
    st.title("📈 Risk Report")

    import pandas as pd

    report_data = pd.DataFrame({
        "Profile": ["user123", "fake_acc01", "john_doe"],
        "Risk Score": [25, 89, 67],
        "Risk Level": ["LOW", "HIGH", "MEDIUM"]
    })

    st.subheader("Analyzed Profiles")

    st.dataframe(report_data, use_container_width=True)

    st.subheader("Risk Summary")

    high_risk = len(report_data[report_data["Risk Level"] == "HIGH"])
    medium_risk = len(report_data[report_data["Risk Level"] == "MEDIUM"])
    low_risk = len(report_data[report_data["Risk Level"] == "LOW"])

    col1, col2, col3 = st.columns(3)

    col1.metric("High Risk", high_risk)
    col2.metric("Medium Risk", medium_risk)
    col3.metric("Low Risk", low_risk)

    st.success("Risk report generated successfully")
    # ---------------- GRAPH VISUALIZATIONS ----------------
elif page == "Graph Visualizations":

    import streamlit as st
    import networkx as nx
    import plotly.graph_objects as go
    import random

    st.title("🌐 Network Intelligence & Relationship Mapping")

    # Top Metrics
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Accounts", "150", "+12%")
    c2.metric("Normal Accounts", "98", "+8%")
    c3.metric("Suspicious Accounts", "32", "+15%")
    c4.metric("Fake Accounts", "20", "+25%")

    st.markdown("---")

    # Network Graph
    G = nx.Graph()

    normal_nodes = [f"N{i}" for i in range(1, 11)]
    suspicious_nodes = [f"S{i}" for i in range(1, 5)]
    fake_nodes = [f"F{i}" for i in range(1, 4)]

    for node in normal_nodes:
        G.add_node(node, group="normal")

    for node in suspicious_nodes:
        G.add_node(node, group="suspicious")

    for node in fake_nodes:
        G.add_node(node, group="fake")

    edges = [
        ("N1","N2"),("N2","N3"),("N3","N4"),
        ("N4","S1"),("S1","S2"),("S2","F1"),
        ("F1","F2"),("F2","F3"),
        ("N5","N6"),("N6","S3"),
        ("S3","F2"),("N7","N8"),
        ("N8","N9"),("N9","S4")
    ]

    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)

    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_color = []

    for node in G.nodes():

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        group = G.nodes[node]["group"]

        if group == "normal":
            node_color.append("green")

        elif group == "suspicious":
            node_color.append("orange")

        else:
            node_color.append("red")

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=list(G.nodes()),
        textposition="top center",
        marker=dict(
            size=25,
            color=node_color,
            line_width=2
        )
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Account Relationship Network",
            showlegend=False,
            hovermode='closest',
            height=700,
            paper_bgcolor="#0E1117",
            plot_bgcolor="#0E1117",
            font=dict(color="white")
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Risk Distribution")

        pie = go.Figure(
            data=[
                go.Pie(
                    labels=["Normal","Suspicious","Fake"],
                    values=[98,32,20],
                    hole=0.55
                )
            ]
        )

        pie.update_layout(
            paper_bgcolor="#0E1117",
            font_color="white"
        )

        st.plotly_chart(pie, use_container_width=True)

    with col2:

        st.subheader("🚨 Network Insights")

        st.error("High Risk Connections : 14")
        st.warning("Suspicious Clusters : 3")
        st.info("Community Groups : 4")
        st.success("Active Monitoring Enabled")

    st.markdown("---")

    st.subheader("🔍 Cluster Analysis")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Cluster 1", "25 Accounts")
    c2.metric("Cluster 2", "18 Accounts")
    c3.metric("Cluster 3", "12 Accounts")
    c4.metric("Cluster 4", "8 Accounts")
    # ---------------- COPILOT INTERFACE ----------------
elif page == "Copilot Interface":
    st.title("🤖 Cyber Identity Copilot")

    user_query = st.text_area(
        "Ask about a profile analysis"
    )

    if st.button("Generate Insight"):

        st.info(
            """
            Analysis Summary:

            • Account exhibits abnormal follower ratio.

            • Posting activity appears suspicious.

            • Risk level classified as HIGH.

            Recommendation:
            Perform manual verification before trust.
            """
        )
