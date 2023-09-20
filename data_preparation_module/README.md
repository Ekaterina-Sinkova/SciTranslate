SciTranslate. Data Preparation
==============================

Data preparation module for NLLB fine-tuning

## Module Structure
```
data_preparation_module
├── data
│   └── raw                     -> folder for subdirectories with pairs of articles
├── data_preparation            -> submodule for data preparation for labeling
│   ├── __init__.py
│   ├── data_preparation.py     
│   └── cli.py                  
├── language_identifier         -> submodule for determining the input-text language
│   ├── __init__.py
│   └── identify_language.py
├── client_secret.json          -> Google API authentification data
├── requirements.txt
└── setup.py
```

1) Place folders with original and translated papers (.docx ONLY) into the data/raw/ directory. 
2) Place googleAPI's client_secret.json into the root directory
3) Create and activate virtual environment
4) Install the data-preparation package
```python
pip install .
```
5) You may need to place manually lid.176.ftz and ISO-codes.json files of the language_identifier into the .venv/lib/python3.10/site-packages/language_identifier folder
6) run the cli command with argument doc_url - url of the spreadsheet where the results should be written
```python
 data-preparation --doc_url=https://docs.google.com/spreadsheets/d/1ZsTxRosThq-1vGT8tRaLm0m-E826f_7BlQJ08QaK9kI
```
A separate tab will be created in the spreadsheet for each folder in the data/raw/ directory. Each tab will contain two columns "ru" and "en" with tokenized sentences in the corresponding rows.


