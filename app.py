import os
from PIL import Image
from utils import utils
import streamlit as st
from dotenv import load_dotenv; load_dotenv()

# Setup your config
st.set_page_config(
    page_title="Interactive Audiobook",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png"
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Interactive Audiobook by Lyzr")
st.markdown("### Welcome to the Interactive Audiobook!")
st.markdown("Interactive Audiobook by Lyzr will convert children's book into interactive audiobook")

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Interactive Audiobook Application
    
# replace this with your openai api key or create an environment variable for storing the key.
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


# create directory if it doesn't exist
data = "data"
os.makedirs(data, exist_ok=True)
 


if __name__ == "__main__":
    style_app()

    with st.expander("ℹ️ - About this App"):
        st.markdown("""
        This app uses Lyzr Voice Bot agent to convert books into interactive audiobooks. The QABot agent is built on the powerful Retrieval-Augmented Generation (RAG) model, enhancing your ability to extract valuable insights. For any inquiries or issues, please contact Lyzr.
        
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)