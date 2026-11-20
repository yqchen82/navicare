import streamlit as st
from rag.auth import require_login
from rag.qa import answer_question
from rag.ui import apply_theme, render_sidebar, hero, section, footer

apply_theme(); render_sidebar(); require_login()
hero("Your scheme, made clearer.", "Share a little context and ask a question. NaviCare will retrieve relevant policy guidance to help you understand what to check next.", eyebrow="PERSONALISED POLICY EXPLORATION", pill="Your details are self-reported and are not verified")
section("Step 1 · Your context", "A few details help focus the search")
with st.form("scheme_profile_form"):
    c1, c2 = st.columns(2)
    with c1:
        birth_year = st.number_input("Year of birth", min_value=1900, max_value=2026, value=1968, step=1)
        residency = st.selectbox("Residency", ["Singapore Citizen", "Singapore Permanent Resident", "Other / prefer not to say"])
        coverage = st.selectbox("Current long-term care coverage", ["ElderShield 300", "ElderShield 400", "CareShield Life", "Not sure / uninsured", "Other"])
    with c2:
        adl_status = st.selectbox("Self-reported ADL situation", ["Not currently unable to perform ADLs", "Needs some assistance (less than 3 ADLs)", "May require full assistance with 3 or more ADLs", "Not sure / prefer not to say"])
        ask = st.text_area("What would you like to understand?", placeholder="Example: I was born in 1968 and have ElderShield 400. What should I know before considering CareShield Life?", height=145)
    submitted = st.form_submit_button("Explore my options", type="primary", use_container_width=True)
if submitted:
    if not ask.strip(): st.warning("Please enter a question so NaviCare knows what to look for.")
    else:
        profile = {"Birth year": int(birth_year), "Residency": residency, "Existing coverage": coverage, "Self-reported ADL situation": adl_status}
        st.session_state["saved_profile"] = profile
        st.session_state["profile"] = profile
        with st.spinner("Searching the policy library and preparing your guidance..."):
            try:
                response, citations = answer_question(ask, profile)
                section("Step 2 · Your guidance", "What the policy references say")
                st.markdown(response)
                if citations:
                    with st.expander("View retrieved source references", expanded=True):
                        for c in citations:
                            st.markdown(f"**{c['source']}** · relevance {c['score']}")
                            if c['url']: st.link_button("Open official source", c['url'])
            except Exception as e: st.error(f"Unable to generate guidance: {e}")
st.warning("Important: If you or a family member may meet severe-disability criteria, only an MOH-accredited severe disability assessor can assess this. NaviCare does not diagnose or determine claim eligibility.")
footer()
