# SciTranslate
Machine Translation Service for Scientific Articles 

# Опыт и предпосылки
В течение десяти лет я сотрудничала с издательством научной литературы Pleiades Publishing, что позволило накопить обширную базу статей и их переводов для использования в качестве обучающих данных. Современные SOTA модели машинного перивода хорошо справляются с грамматикой, но иногда могут неточно переводить отдельные термины, что недопустимо в научном переводе. Мы надеемся, что дообучение модели nllb на собранных данных позволит улучшить качество перевода.  

# Цели и задачи Проекта
1) Сбор и предобработка корпуса параллельных текстов для улучшения качества перевода
2) Дообучение нейросетевой модели nllb (https://huggingface.co/docs/transformers/model_doc/nllb) на парах предложений из собранного корпуса
3) Интеграция базы данных для хранения и управления загруженными статьями, данными для обучения и результатами переводов.
4) Создание пользовательского интерфейса, позволяющего загружать статьи и получать их переводы. Как минимум - без сохранения внутренней структуры документа, текстовый формат. 
Как максимум - возможность загрузки пдф, перевод с сохранением деления на разделы.  
5) Разработка системы оценки качества переводов. Есть эксперты, которых можно привлечь для оценки качества.

# Project Structure
```
SciTranslate/
│
├── data_preparation_module     # Data preparation for NLLB fine-tuning
│   ├── data_preparation        # Data preparation for labeling
│   └── language_identifier     # Determination of the input-text language
│
├── app/                        # Main application folder
│   ├── __init__.py
│   ├── main.py                 # FastAPI main application
│   ├── database.py             # PostgreSQL database handling
│   ├── s3.py                   # AWS S3 file storage handling
│   ├── document_processing.py  # Document processing logic
│   └── translations.py         # Translation logic 
│
├── streamlit_ui.py             # Streamlit user interface
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .env                        # Environment variables (for secrets and configurations)
└── .gitignore                  # Git ignore file
```
**Usage Instructions:**

1. Install the required dependencies listed in **`requirements.txt`** using **`pip install -r requirements.txt`**.
2. Configure the **`.env`** file with the necessary environment variables (e.g., database credentials, AWS S3 credentials).
3. Start the FastAPI server by running **`uvicorn app.main:app --host 0.0.0.0 --port 8000`**.
4. Start the Streamlit user interface using **`streamlit run streamlit_ui.py`**.
5. Access the SciTranslate web service through the Streamlit interface to upload, process, and download translated documents.