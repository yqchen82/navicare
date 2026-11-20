import streamlit as st
from rag.ui import apply_theme, render_sidebar, hero, section, feature_card, footer

apply_theme()
render_sidebar()
hero("Care information should feel easier to navigate.", "NaviCare is a capstone concept exploring how responsible Generative AI can make complex long-term care policy information easier to understand.", eyebrow="ABOUT THE PROJECT", pill="AI Bootcamp · August 2025 Run · Capstone")
section("Our mission", "Making policy information more approachable")
st.markdown("Singapore's long-term care financing landscape includes CareShield Life and legacy ElderShield coverage. Rules can vary by birth cohort, existing coverage and the nature of a person's care needs. NaviCare aims to help citizens, caregivers and financial counsellors find and understand relevant official information without having to search across multiple websites unaided.")
a,b,c=st.columns(3)
with a: feature_card("🧭", "Navigate", "Explore scheme rules and identify the official information relevant to a question.")
with b: feature_card("📖", "Understand", "Translate dense policy language into clear, plain-language explanations.")
with c: feature_card("🔎", "Verify", "Show supporting source references so users can check the underlying guidance.")
section("The team", "NaviCare project members")
team=[("Chen Yongquan","Project team"),("Francine Goh","Project team"),("Robin Chen","Project team"),("Jony Yen","Project team")]
cols=st.columns(4)
for col,(name,role) in zip(cols,team):
    with col: st.markdown(f"<div class='info-card'><div class='icon'>👤</div><h3>{name}</h3><p>{role}</p></div>",unsafe_allow_html=True)
st.write("")
st.info("NaviCare is an educational decision-support prototype. It is not an official government service, insurer, medical assessor or financial adviser. It does not access Singpass, CPF accounts or personal policy records, calculate an individual's official premium, assess disability or approve claims.")
footer()
