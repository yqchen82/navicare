from pathlib import Path
import streamlit as st
from rag.auth import authenticate
from rag.config import OPENAI_API_KEY
from rag.ui import apply_theme, hero, section, feature_card, footer

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="NaviCare | Long-Term Care Scheme Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_theme()

with st.sidebar:
    logo = ASSETS / "navicare_logo_mark.jpg"
    if logo.exists():
        st.image(str(logo), width=76)
    st.markdown("## NaviCare")
    st.caption("LONG-TERM CARE SCHEME NAVIGATOR")
    st.markdown("---")
    st.caption("YOUR GUIDE TO LONG-TERM CARE COVERAGE")
    st.markdown("CareShield Life · ElderShield 300 / 400")
    st.markdown("---")
    st.caption("CAPSTONE PROTOTYPE · SINGAPORE")

hero(
    "Clarity for the care journey.",
    "Understand CareShield Life and ElderShield with plain-language guidance grounded in policy references. Explore your coverage, ask questions and find the next steps with greater confidence.",
    eyebrow="WELCOME TO NAVICARE · LONG-TERM CARE GUIDANCE",
    pill="RAG-powered · Source-grounded · Singapore-focused",
)

if not st.session_state.get("authenticated"):
    left, center, right = st.columns([1, 1.12, 1])
    with center:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.markdown("### Welcome to NaviCare")
        st.write("Sign in to explore scheme guidance, ask policy questions or manage the reference library.")
        with st.form("login"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Sign in to NaviCare", type="primary", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        if submitted:
            role = authenticate(username, password)
            if role:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.role = role
                st.rerun()
            st.error("Unable to sign in. Please check your configured credentials.")
else:
    st.success(f"Welcome back, {st.session_state.username}. Signed in as {st.session_state.role}.")
    section("Explore NaviCare", "Support for every step")
    c1, c2, c3 = st.columns(3)
    with c1:
        feature_card("🧭", "Scheme Navigator", "Share your birth year and current coverage to explore relevant scheme rules and next steps.")
    with c2:
        feature_card("💬", "Policy Q&A", "Ask about eligibility, benefits, premiums, MediSave and severe-disability claims.")
    with c3:
        feature_card("📚", "Policy Library", "Admins can curate and maintain the policy documents used by NaviCare.")
    st.write("")
    st.info("Use the pages in the left navigation to get started. NaviCare provides educational guidance only; it does not determine eligibility or calculate official premiums.")
    if not OPENAI_API_KEY:
        st.warning("OpenAI API key is not configured. Add OPENAI_API_KEY to your local .env or Streamlit Cloud secrets before using AI features.")
    if st.button("Sign out"):
        for key in ("authenticated", "username", "role", "messages", "profile", "saved_profile"):
            st.session_state.pop(key, None)
        st.rerun()

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
