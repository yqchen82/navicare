import streamlit as st
from rag.ui import apply_theme, hero, section, feature_card, footer

st.set_page_config(page_title="Methodology | NaviCare", page_icon="🧪", layout="wide")
apply_theme()
hero("Ground answers in evidence, not guesswork.", "NaviCare uses Retrieval-Augmented Generation (RAG) to find relevant policy passages before asking an AI model to explain them.", eyebrow="HOW NAVICARE WORKS", pill="Document retrieval + language generation")
section("The RAG pipeline", "From policy document to answer")
steps=[("01","Ingest","Admin uploads an MOH, CPF Board or AIC policy reference and records its source URL and date."),("02","Extract & chunk","Text is extracted from supported documents and split into smaller overlapping passages."),("03","Embed","OpenAI text-embedding-3-small converts each passage into a numerical vector representation."),("04","Retrieve","ChromaDB performs semantic similarity search to find passages relevant to the user's question and optional profile context."),("05","Generate","The retrieved passages and question are sent to the language model to produce a plain-language response."),("06","Verify","The response includes source references. Users are encouraged to check current rules with the relevant official agency.")]
for i in range(0,len(steps),2):
    cols=st.columns(2)
    for col,(num,title,desc) in zip(cols,steps[i:i+2]):
        with col: st.markdown(f"<div class='info-card' style='margin-bottom:1rem;min-height:150px'><div class='eyebrow' style='color:#087E8B'>{num} / PIPELINE</div><h3>{title}</h3><p>{desc}</p></div>",unsafe_allow_html=True)
section("Technology stack", "Simple, modular and deployable")
a,b,c,d=st.columns(4)
with a: feature_card("🐍","Python","Application logic and document processing.")
with b: feature_card("🖥️","Streamlit","Web interface, forms and role-specific pages.")
with c: feature_card("🧠","OpenAI API","Embeddings and response generation.")
with d: feature_card("🗃️","ChromaDB","Persistent vector store for semantic retrieval.")
section("Responsible-use safeguards")
st.markdown("- **Source grounding:** responses should rely on retrieved policy passages and disclose when evidence is insufficient.\n- **Policy freshness:** Admins should review publication dates and refresh the reference library when official guidance changes.\n- **No automated eligibility decisions:** profile details are self-reported; the prototype is not a rules engine or official assessment.\n- **Premium and claims verification:** users should confirm personalised premiums with CPF Board and disability assessments through an MOH-accredited assessor.\n- **Known limitations:** scanned PDFs may need OCR; RAG can still retrieve incomplete or outdated passages and LLM output must be checked.")
footer()
