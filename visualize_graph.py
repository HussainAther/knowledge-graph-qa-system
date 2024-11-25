import networkx as nx
import matplotlib.pyplot as plt
from llama_index.graphs import KGIndex


def visualize_knowledge_graph(storage_path="storage"):
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    index = load_index_from_storage(storage_context)
    graph_data = index.get_graph()

    G = nx.DiGraph()
    for node in graph_data.nodes:
        G.add_node(node["id"], label=node["text"])
    for edge in graph_data.edges:
        G.add_edge(edge["from"], edge["to"], label=edge["relationship"])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10)
    plt.show()

if __name__ == "__main__":
    visualize_knowledge_graph()

