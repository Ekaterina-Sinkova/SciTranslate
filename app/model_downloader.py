""""
model_downloader.py
This snippet is created to download the translation model if it's not on a local machine yet
"""

import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class CFG:
    nllb_name = "facebook/nllb-200-distilled-600M"
    nllb_tokenizer_path = 'pretrained_models/nllb_tokenizer_rus'
    nllb_model_path = 'pretrained_models/nllb_model'
    access_name = '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'  # delete before prod


class ModelOrchestrator:

    @classmethod
    def load_nllb_model(cls, config=CFG):
        """"
        Check if the model folder exists, download if not and return
        """
        # Loading model every time takes a lot of time,pretty sure we can have it running on the server
        if not os.path.exists(config.nllb_model_path):
            print('No NLLB model detected.\nDownloading...')
            tokenizer = cls.download_nllb_tokenizer(config)
            model = cls.download_nllb_model(config)
            print('Model loaded successfully.')
        else:
            tokenizer, model = cls._load_nllb(config)
        return tokenizer, model

    @classmethod
    def download_nllb_model(cls, config=CFG):
        model = AutoModelForSeq2SeqLM.from_pretrained(config.nllb_name, token=config.access_name)
        model.save_pretrained(config.nllb_model_path)
        return model

    @classmethod
    def download_nllb_tokenizer(cls, config=CFG):
        tokenizer = AutoTokenizer.from_pretrained(config.nllb_name, src_lang="rus_Cyrl", token=config.access_name)
        tokenizer.save_pretrained(config.nllb_tokenizer_path)
        return tokenizer

    @classmethod
    def _load_nllb(cls, config=CFG):
        tokenizer = AutoTokenizer.from_pretrained(config.nllb_tokenizer_path, src_lang="rus_Cyrl")
        model = AutoModelForSeq2SeqLM.from_pretrained(config.nllb_model_path)
        return tokenizer, model


if __name__ == '__main__':
    tokenizer, model = ModelOrchestrator.load_nllb_model()
