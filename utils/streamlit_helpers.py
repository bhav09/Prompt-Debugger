import streamlit as st
import pyperclip
from datetime import datetime
import hashlib
import requests

def get_client_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
    except Exception as e:
        ip = "127.0.0.1"
    return ip

def generate_session_id(ip):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    session_string = f"{ip}_{now}"
    session_id = hashlib.sha256(session_string.encode()).hexdigest()
    return session_id, now

def copy_url():
    url = 'streamlit.app.com'
    pyperclip.copy(url)
    st.session_state.share_button = False

def get_share_link():
  """Generates the HTML for the share button"""
  share_html = """
  <div style="display: flex; justify-content: space-between;">
    <a href="#" onclick="copyLink()">Copy Link</a>
    </div>
  <script>
  function copyLink() {
    navigator.clipboard.writeText(window.location.href);
    alert("Link copied to clipboard!");
  }
  </script>
  """
  return share_html

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
