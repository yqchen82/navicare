"""Shared NaviCare visual system, adapted from the Francine UI reference."""
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets"
NAVY = "#27506A"
TEAL = "#158477"


def apply_theme():
    st.markdown(r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root{--app-bg:#fffdf9;--surface:#fff;--ink:#203246;--muted:#64758a;--navy:#27506a;--teal:#158477;--mint:#e5f6f0;--coral:#e98268;--line:#e3ebe8;--sidebar-bg:#eff8f5;}
    html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
    .stApp{background:linear-gradient(180deg,#fffdf9 0%,#fff 58%,#f7fbf9 100%);color:var(--ink)}
    h1,h2,h3{font-family:'Space Grotesk',sans-serif!important;color:var(--ink);letter-spacing:-.025em}
    h1{font-size:clamp(2.1rem,4vw,3.55rem)!important;line-height:1.02!important;font-weight:700!important}
    h2{font-size:1.85rem!important;font-weight:700!important}
    .block-container{max-width:1220px;padding-top:1.7rem;padding-bottom:3rem}
    [data-testid="stHeader"]{background:rgba(255,253,249,.88)}
    [data-testid="stSidebar"]{background:linear-gradient(180deg,#eff8f5 0%,#f7fbf9 100%);border-right:1px solid var(--line)}
    [data-testid="stSidebar"] *{color:#29475d}
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p{color:#64758a}
    [data-testid="stSidebarNav"]{padding-top:.6rem}
    [data-testid="stSidebar"] a,[data-testid="stSidebar"] a *{color:#0f766e!important;font-weight:650}
    [data-testid="stSidebar"] hr{border-color:var(--line)}
    [data-testid="stSidebar"] [role="radiogroup"] label{padding:.55rem .7rem;border-radius:12px}
    [data-testid="stSidebar"] [role="radiogroup"] label:hover{background:#dff1ec}
    .hero{background:linear-gradient(125deg,#dff6ee 0%,#e6f1fb 56%,#fff0e7 100%);border:1px solid #e3ebe8;border-radius:26px;padding:2.65rem 3rem;margin:.2rem 0 1.45rem;position:relative;overflow:hidden;box-shadow:0 12px 32px rgba(16,42,67,.045)}
    .hero:after{content:'';position:absolute;right:-95px;top:-125px;width:340px;height:340px;border-radius:50%;border:1px solid rgba(21,132,119,.2);box-shadow:0 0 0 34px rgba(21,132,119,.07),0 0 0 68px rgba(233,130,104,.06)}
    .hero h1,.hero h2,.hero p,.hero .eyebrow,.hero .pill{position:relative;z-index:1}
    .hero h1{max-width:780px;margin:.25rem 0 .65rem;color:#203246!important}
    .hero p{color:#64758a!important;max-width:820px;font-size:1.04rem;line-height:1.65;margin:0}
    .eyebrow,.section-kicker{font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;font-weight:800;color:#158477}
    .pill{display:inline-block;margin-top:1rem;padding:.35rem .75rem;border-radius:999px;background:rgba(255,255,255,.7);border:1px solid rgba(21,132,119,.18);color:#27665f;font-size:.76rem;font-weight:600}
    .section-kicker{margin:1.2rem 0 .35rem}
    .info-card,.card{height:100%;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:1.2rem 1.3rem;box-shadow:0 6px 20px rgba(16,42,67,.045)}
    .info-card .icon{font-size:1.55rem;margin-bottom:.55rem}
    .info-card h3{font-size:1.12rem!important;margin:.15rem 0 .4rem}
    .info-card p{color:var(--muted);font-size:.91rem;line-height:1.55;margin:0}
    .feature-card{border-top:4px solid var(--teal)}
    .accent-card{border-top:4px solid var(--coral)}
    div[data-testid="stForm"]{background:#fff;border:1px solid var(--line);border-radius:18px;padding:1.15rem 1.25rem;box-shadow:0 6px 20px rgba(16,42,67,.035)}
    div.stButton>button,div.stFormSubmitButton>button,div.stDownloadButton>button,[data-testid="stLinkButton"] a{border-radius:999px;font-weight:700;min-height:2.65rem}
    div.stButton>button[kind="primary"],div.stFormSubmitButton>button[kind="primary"]{background:#158477;border-color:#158477;color:white}
    [data-testid="stMetric"]{background:#fff;border:1px solid var(--line);border-radius:15px;padding:1rem}
    [data-testid="stChatMessage"]{border:1px solid var(--line);border-radius:16px;padding:.8rem 1rem;background:#fff}
    [data-testid="stFileUploader"]{background:#fff;border:1px dashed #a9c9c1;border-radius:14px;padding:.5rem}
    [data-testid="stImage"] img{border-radius:20px;border:1px solid var(--line)}
    .notice{background:#fff6e8;border:1px solid #f3d49b;color:#674a16;border-radius:14px;padding:1rem 1.1rem;line-height:1.55}
    .source-strip{background:#edf8f6;border-left:4px solid var(--teal);border-radius:8px;padding:.75rem 1rem;color:#245b59;font-size:.9rem}
    .footer-note{color:#718596;font-size:.78rem;border-top:1px solid var(--line);padding-top:1rem;margin-top:2rem;line-height:1.6}
    hr{border-color:var(--line)}
    a{color:#158477;font-weight:600}
    @media(max-width:720px){.hero{padding:1.55rem 1.25rem}.block-container{padding-top:1rem}}
    </style>
    """, unsafe_allow_html=True)


def hero(title, subtitle, eyebrow="NAVICARE · LONG-TERM CARE GUIDANCE", pill=None):
    pill_html = f'<div class="pill">{pill}</div>' if pill else ""
    st.markdown(f'<section class="hero"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p>{subtitle}</p>{pill_html}</section>', unsafe_allow_html=True)


def section(label, title=None):
    heading = f"<div class='section-kicker'>{label}</div>" + (f"<h2 style='margin-top:0'>{title}</h2>" if title else "")
    st.markdown(heading, unsafe_allow_html=True)


def feature_card(icon, title, description):
    st.markdown(f'<div class="info-card feature-card"><div class="icon">{icon}</div><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)


def footer():
    st.markdown('<div class="footer-note">NaviCare is an educational decision-support prototype, not an official government service, insurer, medical assessor or financial adviser. Always verify current policy details with MOH, CPF Board or AIC.</div>', unsafe_allow_html=True)
