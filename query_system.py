from llama_index.core import StorageContext, load_index_from_storage

def query_knowledge_graph(question, storage_path="storage"):
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    print(response)

if __name__ == "__main__":
    question = input("Enter your query: ")
    query_knowledge_graph(question)

