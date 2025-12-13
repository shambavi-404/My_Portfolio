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

# 2. Aggressive CSS to Remove ALL White Space (Header, Footer, Padding)
st.markdown("""
    <style>
        /* Hide Streamlit's default header (The "Deploy" button bar) */
        header[data-testid="stHeader"] {
            display: none;
        }
        
        /* Hide Streamlit's footer */
        footer {
            display: none;
        }
        
        /* Remove all margins and padding from the main block */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0 !important;
        }
        
        /* Remove gap between iframe and window edge */
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)


# 3. Helper Function: Convert Image to Base64 String
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# 4. Main Logic
html_file_path = "index.html"
image_file_path = "profile.jpg" # Make sure this matches your file name exactly

if not os.path.exists(html_file_path):
    st.error(f"Error: 'index.html' not found.")
else:
    # Read the HTML content
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Inject the Image (if it exists)
    if os.path.exists(image_file_path):
        img_b64 = get_img_as_base64(image_file_path)
        # Find 'src="profile.jpg"' in your HTML and replace it with the real image data
        html_content = html_content.replace(
            'src="profile.jpg"', 
            f'src="data:image/jpeg;base64,{img_b64}"'
        )
    else:
        st.warning("Warning: 'profile.jpg' not found. Your profile image might be empty.")

    # 5. Render the Website
    # height=950 ensures it fits a laptop screen, scrolling=True allows navigation
    components.html(html_content, height=950, scrolling=True)