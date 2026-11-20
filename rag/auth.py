import streamlit as st
from rag.config import setting

# Demo authentication for a bootcamp prototype only. Use an identity provider
# and hashed credentials/secrets management before production use.
def authenticate(username: str, password: str):
    users = {
        setting("ADMIN_USERNAME", "admin"): (setting("ADMIN_PASSWORD"), "Admin"),
        setting("USER_USERNAME", "user"): (setting("USER_PASSWORD"), "User"),
    }
    record = users.get(username)
    if record and record[0] and password == record[0]:
        return record[1]
    return None

def require_login():
    if not st.session_state.get("authenticated"):
        st.warning("Please log in from the Home page to continue.")
        st.stop()

def require_admin():
    require_login()
    if st.session_state.get("role") != "Admin":
        st.error("This page is restricted to Admin users.")
        st.stop()
