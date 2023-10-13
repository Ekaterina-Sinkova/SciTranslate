import streamlit as st
import logging

from app.docxutils import (
    validate_docx_file,
    extract_text_from_docx,
    convert_text_to_docx
)
from app.s3 import S3Handler
# from app.translations import Translator
from googletrans import Translator

BUCKET_NAME = 'scitranslate'

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
with st.form("upload-file", clear_on_submit=True):
    uploaded_file = st.file_uploader("Upload a .docx file for translation")
    submitted = st.form_submit_button("Upload")

if submitted and uploaded_file is not None:
    if validate_docx_file(uploaded_file):
        st.write(f"UPLOADED: {uploaded_file.name}")
        st.session_state['file_is_valid'] = True
        
        # Upload docx file to S3
        # TODO: try async minio client
        try:
            fstorage = S3Handler()
            if not fstorage.client.bucket_exists(BUCKET_NAME):
                fstorage.client.make_bucket(BUCKET_NAME)
            st.session_state['object_uuid'] = fstorage.upload_to_s3(
                bucket_name=BUCKET_NAME,
                file=uploaded_file
            )
            logging.info('File uploaded to S3 with name ' +\
                         st.session_state['object_uuid'])
            st.session_state['upload_successful'] = True
        except Exception as exc:
            logging.exception(f'Upload to S3 failed: {exc}')
        
        # Text extraction
        st.session_state['file_text'] = extract_text_from_docx(uploaded_file)
        logging.info('Text extracted')
        
        # TODO: Write metadata to a database
    
    else:
        st.write("Wrong file type!")
        st.session_state['file_is_valid'] = False

if st.session_state.get('file_is_valid') and\
    st.session_state.get('file_text') is not None:
    if st.button("Translate"):
        with st.spinner("Translating..."):
            
            # Text translation
            # All text processing must be encapsulated
            # TODO: replace by translation service
            translator = Translator()
            translated_text = translator.translate(st.session_state['file_text']).text
            translated_text = translated_text.replace('.', '. ')
            logging.info('Text translated')

            # TODO: Write translation metadata to a database

            # Convert translated text to docx file
            translated_docx = convert_text_to_docx(translated_text)
            logging.info('File ready to download')

            # Button to download translated docx file
            st.download_button(
                label='Download Translated File',
                data=translated_docx,
                file_name='Translation.docx')

            # Upload translated docx file to S3
            # TODO: try async minio client
            try:
                fstorage = S3Handler()
                if not fstorage.client.bucket_exists(BUCKET_NAME):
                    fstorage.client.make_bucket(BUCKET_NAME)
                st.session_state['trans_object_uuid'] = fstorage.upload_to_s3(
                    bucket_name=BUCKET_NAME,
                    file=translated_docx
                )
                logging.info('Translated file uploaded to S3 with name ' +\
                            st.session_state['trans_object_uuid'])
                st.session_state['trans_upload_successful'] = True
            except Exception as exc:
                logging.exception(f'Upload of translation to S3 failed: {exc}')
