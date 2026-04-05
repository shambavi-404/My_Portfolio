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
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Inject a script that tells the iframe its own full scrollHeight
    auto_resize_script = """
    <script>
        window.onload = function() {
            const height = document.documentElement.scrollHeight;
            window.parent.postMessage({type: 'streamlit:setFrameHeight', height: height}, '*');
        };
        // Also fire after images/fonts load
        window.addEventListener('load', function() {
            setTimeout(function() {
                const height = document.documentElement.scrollHeight;
                window.parent.postMessage({type: 'streamlit:setFrameHeight', height: height}, '*');
            }, 1000);
        });
    </script>
    """

    # Inject script just before </body>
    html_with_resize = html_content.replace('</body>', auto_resize_script + '</body>')

    components.html(html_with_resize, height=8000, scrolling=False)

except FileNotFoundError:
    st.error("index.html not found.")