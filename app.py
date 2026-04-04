import streamlit as st
import streamlit.components.v1 as components

# 1. Wide Layout
st.set_page_config(page_title="Shambavi P | Portfolio", page_icon="💻", layout="wide")

# 2. Advanced CSS to kill the gap
st.markdown("""
    <style>
        /* This targets the exact container Streamlit uses for content */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            margin-top: -5rem !important; /* Pulls content up significantly */
        }
        
        /* Hides the top bar entirely */
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        
        /* Force background color to match your portfolio */
        [data-testid="stAppViewContainer"] {
            background-color: #000000 !important;
        }

        /* Removes additional padding from the main area */
        .main .block-container {
            max-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Load index.html
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 4. Display HTML 
    # Use scrolling=False if you want it to feel like one single page
    components.html(html_content, height=1200, scrolling=True) 
except FileNotFoundError:
    st.error("index.html not found.")