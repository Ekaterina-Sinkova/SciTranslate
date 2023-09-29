from googletrans import Translator
from typing import List
from app.models import NLLBTranslator
from app.model_downloader import ModelOrchestrator


class TranslationService:
    def __init__(self):
        tokenizer, model = ModelOrchestrator.load_nllb_model()
        self.tokenizer = tokenizer
        self.model = model

    def nllb_model(self, sentences: List[str], target_lang: str = 'eng_Latn') -> List[str]:
        """
        Use NLLB model to translate sentences
        """
        translator = NLLBTranslator(self.tokenizer, self.model, target_lang=target_lang)  # Only from russian language
        translated_sentences = []
        for sentence in sentences:
            result = translator.translate(sentence)
            translated_sentences.append(result)
        return translated_sentences

    def translate_sentences(self, sentences: list):
        # Your sentence translation code goes here
        # Example: Translate the sentences using a translation service
        results = self.nllb_model(sentences)
        # Replace with actual implementation
        return 'translation: ' + ' '.join(results)

    def gtrans(self, sentences: List[str], source_lang: str = 'ru', target_lang: str = 'en') -> List[str]:
        """
        Use google translate online client to translate sentences
        """
        translator = Translator()
        translated_sentences = []
        for sentence in sentences:
            result = translator.translate(sentence, src=source_lang, dest=target_lang)
            translated_sentences.append(result.text)
        return translated_sentences
