import json
import os
from pathlib import Path
from typing import List

import fasttext as ft
from pydantic import BaseModel, validator


class LanguageIdentificationDto(BaseModel):
    iso_code: str
    english_description: str
    russian_description: str
    confidence: float

    @validator('iso_code')
    def iso_code_lenght(cls, v):
        if len(v) > 3:
            raise ValueError('длина кода ISO-639 должна быть не более 3 символов')
        return v

    @validator('confidence')
    def confidence_sanity_check(cls, v):
        if v > 1.01:  # поправка на машинную точность
            raise ValueError('уверенность модели должна быть меньше 1')
        return v


class LanguageIdentifier():
    model = None
    iso_dict = None
    k = None  # количество языков по умолчанию, которая выводит модель, не сильно влияет на качество, из-за низких вероятностей в хвосте

    def __init__(self, k=20):
        self.k = k
        file_dir = Path(__file__).resolve().parents[0]  # получаем текущую папку и загружаем файлы
        self.model = ft.load_model(os.path.join(file_dir, "lid.176.ftz"))
        with open(os.path.join(file_dir, "ISO_codes.json"), "r", encoding="utf-8") as file:
            self.iso_dict = json.load(file)

    def get_russian_description_by_iso_code(self, iso_code: str):
        return self.iso_dict[iso_code]["language_ru"]

    def get_english_description_by_iso_code(self, iso_code: str):
        return self.iso_dict[iso_code]["language_en"]

    def predict(self, texts: List[str], confidence_threshold: float = 0.05) -> List[LanguageIdentificationDto]:
        '''
        Определяет язык текстов.

        Parameters:
            texts: List[str]: Список текстов
            confidence_threshold: float: Минимальная вероятность языка для его последующего учёта

        Returns:
            List[LanguageIdentificationDto]: список языков по убыванию вероятности
        '''

        # объект prediction возвращает кортеж, где первый элемент - список списков языков,
        # а второй - список numpy массивов с уверенностью модели
        prediction = self.model.predict(texts, k=self.k)

        # для всех предсказаний собираем словарь - iso_code языка и уверенность модели, 
        # если уверенность выше заданного порога
        dict_list = []
        for i in range(len(texts)):
            iso_code_confidence_dict = dict()
            labels = prediction[0][i]
            confidences = prediction[1][i]
            for lang_label, confidence in zip(labels, confidences):
                if confidence > confidence_threshold:
                    iso_code = lang_label.split("__")[-1]
                    iso_code_confidence_dict[iso_code] = confidence
            dict_list.append(iso_code_confidence_dict)

        # собираем словарь со всеми кодами языка, суммируя уверенности модели    
        all_codes_dict = dict()
        for iso_code_confidence_dict in dict_list:
            for key in iso_code_confidence_dict.keys():
                if all_codes_dict.get(key):
                    all_codes_dict[key] += iso_code_confidence_dict[key]
                else:
                    all_codes_dict[key] = iso_code_confidence_dict[key]

        # нормируем уверенности относительно количества текстов на входе
        for key in all_codes_dict.keys():
            all_codes_dict[key] /= len(texts)

        # сортируем по убыванию confidence и записываем с сохранением порядка
        sorted_keys = sorted(all_codes_dict, key=all_codes_dict.get, reverse=True)
        result_list = []

        # возвращаем список отсортированных по убыванию DTO-объектов
        for key in sorted_keys:
            result_list.append(LanguageIdentificationDto(
                iso_code=key,
                english_description=self.iso_dict[key]["language_en"],
                russian_description=self.iso_dict[key]["language_ru"],
                confidence=all_codes_dict[key]))
        return result_list
