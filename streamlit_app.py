import streamlit as st

st.set_page_config(
    page_title="NaviCare | Long-Term Care Scheme Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = [
    st.Page("pages/0_🏠_Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/6_🔐_Sign_In.py", title="Sign In", icon="🔐"),
    st.Page("pages/1_🧭_Scheme_Navigator.py", title="Scheme Navigator", icon="🧭"),
    st.Page("pages/2_💬_Policy_QA.py", title="Policy Q&A", icon="💬"),
    st.Page("pages/3_🗂️_Document_Management.py", title="Document Management", icon="🗂️"),
    st.Page("pages/4_👥_About_Us.py", title="About Us", icon="👥"),
    st.Page("pages/5_🧪_Methodology.py", title="Methodology", icon="🧪"),
]

current_page = st.navigation(pages, position="hidden")
current_page.run()
