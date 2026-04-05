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
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #04060a !important;
        }
        /* Remove iframe border and overflow */
        iframe {
            display: block;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Set height tall enough for full page, scrolling=False so the PAGE scrolls
    components.html(html_content, height=6000, scrolling=False)

except FileNotFoundError:
    st.error("index.html not found. Make sure index.html is in the same folder as app.py.")