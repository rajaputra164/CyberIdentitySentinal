import networkx as nx
import plotly.graph_objects as go


def create_network_graph():

    G = nx.Graph()

    # Add profiles
    G.add_edge("Profile A", "Profile B")
    G.add_edge("Profile B", "Profile C")
    G.add_edge("Profile C", "Profile D")
    G.add_edge("Fake Account 1", "Fake Account 2")
    G.add_edge("Fake Account 2", "Fake Account 3")

    pos = nx.spring_layout(G)

    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines"
    )

    node_x = []
    node_y = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=list(G.nodes()),
        textposition="top center"
    )

    fig = go.Figure(
        data=[edge_trace, node_trace]
    )

    fig.show()