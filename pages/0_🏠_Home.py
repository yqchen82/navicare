from pathlib import Path
import streamlit as st
from rag.config import OPENAI_API_KEY
from rag.ui import apply_theme, render_sidebar, hero, section, feature_card, footer

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

apply_theme()
render_sidebar()

hero(
    "Clarity for the care journey.",
    "Understand CareShield Life and ElderShield with plain-language guidance grounded in policy references. Explore your coverage, ask questions and find the next steps with greater confidence.",
    eyebrow="WELCOME TO NAVICARE · LONG-TERM CARE GUIDANCE",
    pill="RAG-powered · Source-grounded · Singapore-focused",
)

if st.session_state.get("authenticated"):
    st.success(
        f"Welcome back, {st.session_state.get('username', 'User')}. "
        f"Signed in as {st.session_state.get('role', 'User')}."
    )
else:
    st.info("You can browse the project overview without signing in. Sign in from the side menu to access the Scheme Navigator and Policy Q&A.")

section("Explore NaviCare", "Support for every step")
c1, c2, c3 = st.columns(3)
with c1:
    feature_card("🧭", "Scheme Navigator", "Share your birth year and current coverage to explore relevant scheme rules and next steps.")
with c2:
    feature_card("💬", "Policy Q&A", "Ask about eligibility, benefits, premiums, MediSave and severe-disability claims.")
with c3:
    feature_card("📚", "Policy Library", "Admins can curate and maintain the policy documents used by NaviCare.")
st.write("")
st.info("NaviCare provides educational guidance only; it does not determine eligibility or calculate official premiums.")
if not OPENAI_API_KEY:
    st.warning("OpenAI API key is not configured. Add OPENAI_API_KEY to your local .env or Streamlit Cloud secrets before using AI features.")

section("What NaviCare helps with", "A clearer view of coverage and care")
col1, col2 = st.columns(2)
with col1:
    feature_card("🛡️", "Understand coverage", "Compare scheme structures and understand cohort-specific joining and upgrade considerations.")
with col2:
    feature_card("🤝", "Navigate claims", "Learn about the six Activities of Daily Living and the formal assessment pathway.")

image_path = ASSETS / "navicare_scheme.jpg"
if image_path.exists():
    st.write("")
    st.image(str(image_path), caption="Explore long-term care coverage and official policy guidance.", use_container_width=True)
footer()
