from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.database import DatabaseHandler
from app.s3 import S3Handler
from app.translations import TranslationService
from app.data_processing import DataProcessor

app = FastAPI()
db_handler = DatabaseHandler()
s3_handler = S3Handler()
data_processor = DataProcessor()
translation_service = TranslationService()

class Text(BaseModel):
    text: str

@app.post('/translate_file')
async def upload_file(file: UploadFile = File(...)):
    if data_processor.validate_file(file.filename):
        docx_file = await file.read()
        sentences = data_processor.tokenize_docx(docx_file)
    else:
        pass
    output_file = data_processor.concatenate_sentences_to_docx(sentences)
    output_filename = f'{file.filename.split(".")[0]}_eng.docx'
    output_file.save(output_filename)

    return FileResponse(output_filename, headers={'Content-Disposition': 'attachment; filename=translated_output.docx'})


@app.post('/translate_text')
async def translate_text(text: Text):
    sentences = data_processor.tokenize_text(text.text)
    text = translation_service.translate_sentences(sentences)
    return text
