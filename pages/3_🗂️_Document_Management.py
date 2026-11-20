import streamlit as st
from pathlib import Path
from uuid import uuid4
from rag.auth import require_admin
from rag.config import DOCS_DIR, SAMPLE_DIR
from rag.document_processor import make_chunks
from rag.vector_store import add_documents, list_sources, delete_source
from rag.ui import apply_theme, hero, section, footer

st.set_page_config(page_title="Policy Library | NaviCare", page_icon="🗂️", layout="wide")
apply_theme(); require_admin()
hero("Keep the knowledge base trustworthy.", "Manage the policy references NaviCare uses to answer questions. Prioritise current MOH, CPF Board and AIC publications.", eyebrow="ADMIN WORKSPACE", pill="Restricted to Admin users")
section("Knowledge ingestion", "Add official policy references")
st.markdown("Upload PDF, DOCX, TXT or Markdown files. Record the official source URL and ensure the publication or effective date is clear in the document.")
with st.form("upload"):
    uploads=st.file_uploader("Choose policy documents", type=["pdf","docx","txt","md"], accept_multiple_files=True)
    source_url=st.text_input("Official source URL", placeholder="https://www.cpf.gov.sg/...")
    confirmed=st.checkbox("I have checked that these are official or approved references and noted their publication / effective dates.")
    submit=st.form_submit_button("Upload and index documents", type="primary", use_container_width=True)
if submit:
    if not uploads: st.warning("Choose at least one document first.")
    elif not confirmed: st.error("Please confirm the source review before indexing.")
    else:
        for f in uploads:
            try:
                payload=f.getvalue(); sid=uuid4().hex
                chunks=make_chunks(f.name,payload,source_url)
                add_documents(chunks,sid)
                target=DOCS_DIR / f"{sid}_{Path(f.name).name}"; target.write_bytes(payload)
                st.success(f"Added {f.name} · {len(chunks)} searchable text chunks")
            except Exception as e: st.error(f"{f.name}: {e}")
section("Starter library", "Load NaviCare demonstration references")
st.caption("Bundled notes are illustrative summaries with source links. For a real advisory workflow, replace or supplement them with the latest official source documents.")
if st.button("Index bundled sample documents"):
    for sample in sorted(SAMPLE_DIR.glob("*.md")):
        try:
            payload=sample.read_bytes(); text=payload.decode("utf-8",errors="ignore")
            url=next((line.split(":",1)[1].strip() for line in text.splitlines() if line.startswith("Source URL:")),"")
            sid=uuid4().hex; chunks=make_chunks(sample.name,payload,url); add_documents(chunks,sid)
            (DOCS_DIR / f"{sid}_{sample.name}").write_bytes(payload)
            st.success(f"Indexed {sample.name} · {len(chunks)} chunks")
        except Exception as e: st.error(f"{sample.name}: {e}")
section("Current knowledge base", "Indexed documents")
sources=list_sources()
if not sources: st.info("Your policy library is empty. Upload references or index the bundled sample set to get started.")
else:
    st.caption(f"{len(sources)} document(s) currently indexed")
    for src in sources:
        a,b=st.columns([5,1])
        a.markdown(f"**📄 {src['filename']}**")
        if b.button("Remove",key=f"del_{src['source_id']}"):
            try:
                delete_source(src['source_id'])
                path=next(iter(DOCS_DIR.glob(f"{src['source_id']}_*")),None)
                if path: path.unlink(missing_ok=True)
                st.success("Document removed from the knowledge base."); st.rerun()
            except Exception as e: st.error(str(e))
footer()
