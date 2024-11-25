from llama_index.graphs import KGIndex
from llama_index.core import StorageContext

def build_knowledge_graph(data_path="data", storage_path="storage"):
    documents = SimpleDirectoryReader(data_path).load_data()
    kg_index = KGIndex.from_documents(documents)
    kg_index.storage_context.persist(persist_dir=storage_path)
    print("Knowledge graph built and persisted.")

if __name__ == "__main__":
    build_knowledge_graph()
