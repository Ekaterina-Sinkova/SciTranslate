from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.database import DatabaseHandler
from app.s3 import S3Handler
from app.translations import TranslationService
from app.data_processing import DataProcessor


class Text(BaseModel):
    text: str


app = FastAPI()
db_handler = DatabaseHandler()
s3_handler = S3Handler()
data_processor = DataProcessor()
translation_service = TranslationService()


@app.post('/translate_file')
async def upload_file(file: UploadFile = File(...)):
    """
    Reads, validates and translated the uploaded file. 
    Args:
        file: file in Russian, uploaded by the user
    Returns: translated file
    """
    if data_processor.validate_file(file.filename):
        try:
            docx_file = await file.read()
            sentences = data_processor.tokenize_docx(docx_file)
            output_file = data_processor.concatenate_sentences_to_docx(sentences)
            output_filename = f'{file.filename.split(".")[0]}_eng.docx'
            output_file.save(output_filename)
            return FileResponse(output_filename,
                                headers={'Content-Disposition': 'attachment; filename=translated_output.docx'})
        except Exception:
            raise


@app.post('/translate_text')
async def translate_text(text: Text):
    """
    Translates the input text.
    Args:
        text: input text, entered by the user
    Returns:
        translated text
    """
    try:
        sentences = data_processor.tokenize_text(text.text)
        translation = translation_service.translate_sentences(sentences)
        return translation
    except Exception:
        raise
