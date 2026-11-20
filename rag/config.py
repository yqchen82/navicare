import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = DATA_DIR / "policy_docs"
CHROMA_DIR = DATA_DIR / "chroma_db"
SAMPLE_DIR = ROOT / "sample_docs"
for folder in (DOCS_DIR, CHROMA_DIR):
    folder.mkdir(parents=True, exist_ok=True)

def setting(name: str, default: str = "") -> str:
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st
        value = st.secrets.get(name, default)
        return str(value) if value is not None else default
    except Exception:
        return default

OPENAI_API_KEY = setting("OPENAI_API_KEY")
CHAT_MODEL = setting("OPENAI_CHAT_MODEL", "gpt-4o-mini")
EMBEDDING_MODEL = setting("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
