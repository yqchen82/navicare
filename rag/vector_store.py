from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from rag.config import CHROMA_DIR, EMBEDDING_MODEL, OPENAI_API_KEY

COLLECTION = "navicare_policy_knowledge"

def get_store():
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not configured. Add it to .env or Streamlit secrets.")
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL, api_key=OPENAI_API_KEY)
    return Chroma(collection_name=COLLECTION, embedding_function=embeddings, persist_directory=str(CHROMA_DIR))

def add_documents(docs, source_id: str):
    store = get_store()
    for doc in docs:
        doc.metadata["source_id"] = source_id
    ids = [f"{source_id}-{d.metadata['chunk']}" for d in docs]
    store.add_documents(docs, ids=ids)
    return len(docs)

def search_documents(question: str, k: int = 5):
    return get_store().similarity_search_with_relevance_scores(question, k=k)

def list_sources():
    if not CHROMA_DIR.exists() or not any(CHROMA_DIR.iterdir()):
        return []
    try:
        raw = get_store()._collection.get(include=["metadatas"])
        found = {}
        for meta in raw.get("metadatas", []):
            if meta:
                found[meta.get("source_id", meta.get("source", "unknown"))] = meta.get("source", "Unknown")
        return [{"source_id": key, "filename": value} for key, value in found.items()]
    except Exception:
        return []

def delete_source(source_id: str):
    store = get_store()
    store._collection.delete(where={"source_id": source_id})
