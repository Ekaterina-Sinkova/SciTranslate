from fastapi import FastAPI, UploadFile
from app.document_processing import DocumentProcessor
document_processor = DocumentProcessor()

app = FastAPI()


@app.post('/upload')
async def upload_file(file: UploadFile):
    message = document_processor.validate_file(file.filename)
    return message
