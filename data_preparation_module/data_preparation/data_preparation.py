import os
import re
from pathlib import Path

import pandas as pd
import pygsheets
from docx import Document

from language_identifier.language_identifier import LanguageIdentifier

language_identifier = LanguageIdentifier()


def split_text_into_sent(text: str, lang: str) -> list:
    """Tokenizes input text into sentences using regex"""

    regex_ru = r"(?<!гр)(?<!см)(?<!им)(?<!\sо)(?<!\sг)(?<!\sр)(?<!\.[А-Я])(?<!\.\s[А-Я])(\. +[А-Я])(?!\.)"
    regex_en = r"(?<!gr)(?<!no)(?<!\.[A-Z])(?<!\.\s[A-Z])(\. +[A-Z])(?!\.)"

    regex = regex_ru if lang == "ru" else regex_en

    r1 = re.split(regex, text)
    sents = [r1[0] + "."]
    for i in range(1, len(r1), 2):
        sents.append(r1[i][-1] + r1[i + 1] + ".")
    sents[-1] = sents[-1][0:-1]

    # delete Abstract word
    if not lang == "ru":
        for i in range(len(sents)):
            if sents[i].startswith("Abstract—"):
                sents[i] = sents[i][9:]
    # remove rows without letters
    sents = [sent if re.search("[а-яА-Яa-zA-Z]", sent) else '' for sent in sents]

    return sents


def get_sentences_for_doc(filepath: str) -> dict:
    """Читает документ и определяет его язык. Токенизирует текст на предложения
     Arguments:
         """

    doc = Document(filepath)
    fulltext = ""
    paragraphs = []
    for para in doc.paragraphs:
        paragraphs.append(para.text.strip())
        fulltext += para.text

    try:
        lang = language_identifier.predict([fulltext])[0].iso_code
    except Exception:
        lang = "unk"

    df = pd.DataFrame(paragraphs, columns=["paragraphs"])
    df["sents"] = df["paragraphs"].apply(lambda x: split_text_into_sent(x, lang))
    df = df.explode("sents")["sents"]
    values = [val for val in df.values]

    # remove rows after Conclusions
    try:
        threshold = values.index('СПИСОК ЛИТЕРАТУРЫ')
        values = values[:threshold]
    except ValueError:
        pass

    try:
        threshold = values.index('REFERENCES')
        values = values[:threshold]
    except ValueError:
        pass

    return {"lang": lang, "sentences": values}


def process_pairs_of_docs(doc_url: str) -> None:
    """Рекурсивно читаем папки в директории /data/raw, содержащие пары документов (оригинал и перевод), токенизируем
    документы и записываем во вкладки в гугл-доке"""
    client = pygsheets.authorize()
    spreadsheet = client.open_by_url(doc_url)
    rootdir = Path("data/raw/")
    for root, dirs, files in os.walk(rootdir):
        for dir in dirs:
            root = Path(f"data/raw/{dir}")
            df = pd.DataFrame()
            for file in os.listdir(root):
                doc_info = get_sentences_for_doc(os.path.join(root, file))
                lang, sentences = doc_info["lang"], doc_info["sentences"]
                lang_series = pd.Series(sentences, name=lang)
                df = pd.concat([df, lang_series], axis=1, join="outer")
            try:
                spreadsheet.add_worksheet(dir)
                worksheet = spreadsheet.worksheet("title", dir)
            except Exception:
                worksheet = spreadsheet.worksheet("title", dir)
            worksheet.adjust_column_width(start=1, end=2, pixel_size=600)
            worksheet.set_dataframe(df, start="A1")
    return True


if __name__ == "__main__":
    doc_url = "https://docs.google.com/spreadsheets/d/1omRS01wHJ4MKTdDKf17SmCvR3Fop837QS43gly1WpZA/edit#gid=0"
    process_pairs_of_docs(doc_url)
