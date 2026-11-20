import streamlit as st
from rag.auth import authenticate
from rag.ui import apply_theme, render_sidebar, hero, footer

apply_theme()
render_sidebar()

hero(
    "Welcome back to NaviCare.",
    "Sign in to access personalised scheme guidance, policy questions and the Admin document workspace.",
    eyebrow="SECURE ACCESS · NAVICARE",
    pill="Choose the account provided for this prototype",
)

if st.session_state.get("authenticated"):
    st.success(
        f"You are signed in as {st.session_state.get('username', 'User')} "
        f"({st.session_state.get('role', 'User')})."
    )
    st.info("Use the side menu to continue. To change accounts, sign out from the side menu first.")
else:
    _, center, _ = st.columns([1, 1.15, 1])
    with center:
        # Maintain vertical spacing without the empty bubble
        st.markdown(
            "<div style='height: 24px;'></div>",
            unsafe_allow_html=True
        )

        st.markdown("### Sign in to NaviCare")
        st.write("Enter your configured username and password.")

        with st.form("navicare_sign_in_form", clear_on_submit=False):
            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )
            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            submitted = st.form_submit_button(
                "Sign in",
                type="primary",
                use_container_width=True,
            )
            
    if submitted:
        role = authenticate(username.strip(), password)
        if role:
            st.session_state.authenticated = True
            st.session_state.username = username.strip()
            st.session_state.role = role
            st.switch_page("pages/0_🏠_Home.py")
        else:
            st.error("Unable to sign in. Please check your configured credentials.")

st.caption("Demo authentication is intended for the NaviCare capstone prototype. Do not reuse personal passwords.")
footer()
