import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements

st.title(':green[GATE CSE] GPT :bulb: ')


question = st.text_input(
    "Search all your doubts at one place",
    placeholder="What data are you looking for? DFS, BFS, Little endian, von neumann architecture, PYQ's..."
    
)
"Ft. Pathway, OpenAI"

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")

# background image

import base64
import streamlit as st

original_title = ''
st.markdown(original_title, unsafe_allow_html=True)


# Set the background image
background_image = """
<style>


[data-testid="stAppViewContainer"] > .main {

    background-image: url("https://raw.githubusercontent.com/souvikcseiitk/webpage_cse.iitk.ac.in-users-souvik-/main/llmapp8.jpg");
    background-size: contain;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)