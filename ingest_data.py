from llama_index.core import SimpleDirectoryReader

def ingest_data(data_path="data"):
    documents = SimpleDirectoryReader(data_path).load_data()
    print(f"Ingested {len(documents)} documents.")

if __name__ == "__main__":
    ingest_data()
