import streamlit as st

def display_colored_text(text, color):
    """Displays text in a specified color using HTML."""
    html = f"<p style='color:{color};'><b>{text}</b></p>"
    st.write(html, unsafe_allow_html=True)

def setup_background(image_url):
    changes = f'''
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('{image_url}');
        background-size: cover;
    }}

    div.esravye2 > iframe {{
        background-color: transparent;
    }}
    </style>
    '''
    st.markdown(changes, unsafe_allow_html=True)