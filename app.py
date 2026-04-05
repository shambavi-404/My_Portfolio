import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Shambavi P | Portfolio", page_icon="💻", layout="wide")

st.markdown("""
    <style>
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #04060a !important;
        }
        iframe {
            display: block;
            border: none !important;
            width: 100vw !important;
            height: 100vh !important;
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()

    components.html(html_content, height=900, scrolling=True)

except FileNotFoundError:
    st.error("index.html not found.")