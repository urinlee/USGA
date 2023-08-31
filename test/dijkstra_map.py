import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(2, 0))
G.add_node("C", pos=(2, 2))
G.add_node("D", pos=(4, 0))

# Add edges with weights
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=1)
G.add_edge("A", "C", weight=4)
G.add_edge("B", "D", weight=5)

# Find shortest path
shortest_path = nx.shortest_path(G, source="A", target="D", weight="weight")
print("Shortest Path:", shortest_path)

# Draw the graph
pos = nx.get_node_attributes(G, "pos")
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12, font_weight="bold")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
