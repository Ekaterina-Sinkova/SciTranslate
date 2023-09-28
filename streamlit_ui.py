
import streamlit as st
import time
import requests
import base64
import json

# Helper function to create a download link
def get_binary_file_downloader_html(bin_data, file_label, button_text):
    b64 = base64.b64encode(bin_data).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}">{button_text}</a>'

st.title("SciTranslate Web Service")
st.markdown("---")

st.sidebar.title("Instructions")
st.sidebar.markdown("1. Upload a .docx file for translation.")
st.sidebar.markdown("OR")
st.sidebar.markdown("2. Enter Russian text for translation.")
st.sidebar.markdown("---")
st.sidebar.markdown("[GitHub Repo](https://github.com/Ekaterina-Sinkova/SciTranslate)")

# File upload section
st.subheader("Translate from a .docx file")
uploaded_file = st.file_uploader("Upload a .docx file for translation")
if uploaded_file:
    if st.button("Translate"):
        with st.spinner("Translating..."):
            time.sleep(2)
            # Make a POST request to the FastAPI server to upload and process the file
            response = requests.post("http://localhost:8000/translate_file", files={"file": uploaded_file})

            if response.status_code == 200:
                st.markdown(get_binary_file_downloader_html(response.content, "Translated_Output.docx",
                                                            "Download Translated File"), unsafe_allow_html=True)
            else:
                st.error("Error processing the file. Please try again.")
                
# Text input section
st.subheader("Translate Russian text")
user_input_text = st.text_area("Enter Russian text for translation and press Ctrl + Enter")

#translation_output = st.empty()
if user_input_text:
    url = "http://localhost:8000/translate_text"
    headers = {"Content-Type":"application/json"}
    data = {"text": user_input_text}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response.encoding = 'utf-8'
        st.text_area("Translation", value=response.text)

