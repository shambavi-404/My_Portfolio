import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Shambavi P | Portfolio", page_icon="💻", layout="wide")

# 2. Hard Override of Streamlit's CSS to remove ALL white space
st.markdown("""
    <style>
        /* Removes padding from the main block */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* Hides the Streamlit Header and Footer */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        /* Sets the background of the app to match your portfolio black */
        [data-testid="stAppViewContainer"] {
            background-color: #000000;
        }
        /* Removes the top margin of the main app */
        .main {
            margin-top: -50px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Load index.html
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 4. Display HTML with full width/height
    # We use width=None to let it auto-expand to 100%
    components.html(html_content, height=2000, scrolling=True)
except FileNotFoundError:
    st.error("Error: index.html not found in the root directory.")