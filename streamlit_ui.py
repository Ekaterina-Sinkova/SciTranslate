import streamlit as st
import time
import requests

st.title("SciTranslate Web Service")

uploaded_file = st.file_uploader("Upload a .docx file")
if uploaded_file:
    if st.button("Translate"):
        with st.spinner("Translating..."):
            time.sleep(2)
            # Make a POST request to the FastAPI server to upload and process the file
            response = requests.post("http://localhost:8000/upload", files={"file": uploaded_file})

            if response.status_code == 200:
                st.write(response.text)
                # Display a download link for the translated file
            else:
                st.error("Error processing the file. Please try again.")
