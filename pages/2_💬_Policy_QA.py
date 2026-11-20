import streamlit as st
from rag.auth import require_login
from rag.qa import answer_question
from rag.ui import apply_theme, render_sidebar, hero, section, footer

apply_theme(); render_sidebar(); require_login()
hero("Ask. Understand. Feel more prepared.", "Ask plain-language questions about CareShield Life, ElderShield 300 / 400, eligibility, premiums, MediSave and claims.", eyebrow="NAVICARE POLICY ASSISTANT", pill="Answers are grounded in the Admin-managed reference library")
section("Conversation", "What would you like to know?")
if "messages" not in st.session_state: st.session_state.messages=[]
for item in st.session_state.messages:
    with st.chat_message(item["role"]): st.markdown(item["content"])
question=st.chat_input("For example: What are the six Activities of Daily Living?")
if question:
    st.session_state.messages.append({"role":"user","content":question})
    with st.chat_message("user"): st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Searching NaviCare's policy library..."):
            try:
                answer, citations=answer_question(question, st.session_state.get("profile"))
                st.markdown(answer)
                if citations:
                    with st.expander("Sources used", expanded=True):
                        for c in citations:
                            st.markdown(f"- **{c['source']}** (relevance: {c['score']})" + (f" · [Official source]({c['url']})" if c['url'] else ""))
                st.session_state.messages.append({"role":"assistant","content":answer})
            except Exception as e: st.error(f"Unable to answer: {e}")
if st.session_state.messages and st.button("Clear conversation"):
    st.session_state.messages=[]; st.rerun()
with st.expander("Suggested questions"):
    st.markdown("- What is the difference between ElderShield 300 and ElderShield 400?\n- Who can join CareShield Life?\n- What are the six Activities of Daily Living?\n- How does MediSave premium support work?")
footer()
