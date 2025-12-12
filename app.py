import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Shambavi P | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit's default UI elements (Hamburger menu, Footer, Header)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Function to encode image to Base64 (Fixes broken images in Streamlit)
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 4. Read HTML and inject Image
try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Check if profile.jpg exists and inject it
    if os.path.exists("profile.jpg"):
        img_b64 = get_img_as_base64("profile.jpg")
        # Replace the src="profile.jpg" with the actual Base64 data
        html_content = html_content.replace(
            'src="profile.jpg"', 
            f'src="data:image/jpeg;base64,{img_b64}"'
        )

    # 5. Render the HTML
    # Height is set to 4000px to allow scrolling. 
    # Streamlit creates an iframe, so we need a fixed height large enough for your content.
    components.html(html_content, height=4500, scrolling=False)

except FileNotFoundError:
    st.error("index.html not found. Please make sure it is in the same directory.")