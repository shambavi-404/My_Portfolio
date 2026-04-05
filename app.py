import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Shambavi P | Portfolio", page_icon="💻", layout="wide")

st.markdown("""
    <style>
        /* 1. Remove the white space at the very top */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        
        /* 2. Remove padding from the container */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }

        /* 3. Adjust this margin to bring your header back into view */
        /* If it's still missing, change -2rem to 0rem */
        .main {
            margin-top: -0rem !important; 
        }

        /* 4. Ensure the background is black so there's no white flicker */
        [data-testid="stAppViewContainer"] {
            background-color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Using width=None allows the component to take full browser width
    components.html(html_content, height=1500, scrolling=True)
except FileNotFoundError:
    st.error("index.html not found.")