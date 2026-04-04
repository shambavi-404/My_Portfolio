import streamlit as st
import streamlit.components.v1 as components

# 1. Set page to wide mode
st.set_page_config(page_title="Shambavi P | Portfolio", page_icon="💻", layout="wide")

# 2. CSS to remove Streamlit's default padding and margins
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #root > div:nth-child(1) > div > div > div > div > section > div {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        [data-testid="stAppViewContainer"] > .main {
            padding: 0;
            margin: 0;
        }
        iframe {
            display: block;
            border: none;
            height: 100vh;
            width: 100vw;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Read your index.html file
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_data = f.read()
    
    # 4. Display the HTML with full viewport height and width
    components.html(html_data, height=2000, scrolling=True) # Adjust height if needed
except FileNotFoundError:
    st.error("index.html not found!")