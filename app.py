import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode
st.set_page_config(layout="wide")

# Read your index.html file
with open("index.html", 'r', encoding='utf-8') as f:
    html_data = f.read()

# Display the HTML in Streamlit
components.html(html_data, height=1000, scrolling=True)