

class NLLBTranslator:
    def __init__(self, tokenizer, model, target_lang: str = 'eng_Latn', sent_len: int = 300):
        """
        Initialize the NLLB Translator.
        :param tokenizer: Preloaded NLLB tokenizer.
        :param target_lang: Preloaded NLLB model.

        :param target_lang: Target language code. Default is 'eng_Latn'.
        :param sent_len: Maximum length for generated translations. Default is 300.
        """
        self.tokenizer = tokenizer
        self.model = model
        self.to_lang = target_lang
        self.max_length = sent_len

    def tokenize(self, sent: str):
        """
        Tokenize a sentence using the NLLB tokenizer.

        :param sent: The input sentence.
        :return: Tokenized inputs.
        """
        return self.tokenizer(sent, return_tensors='pt')

    def generate_translation(self, inputs):
        """
        Generate a translation from tokenized inputs.

        :param inputs: Tokenized inputs.

        :return: torch.Tensor: Token IDs of the generated translation.
        """
        return self.model.generate(
            **inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id[self.to_lang],
            max_length=self.max_length)

    def get_decoded(self, toks) -> str:
        """
        Decode token IDs to text.

        :param toks: Token IDs.
        :return: Decoded sentence.
        """
        # Issue with special tokens. We skip PAD but what should we do with UNKs?
        return self.tokenizer.batch_decode(toks, skip_special_tokens=True)[0]

    def translate(self, sent: str) -> str:
        """
        Perform all necessary actions to translate a sentence.

        :param sent: The input sentence.
        :return: The translated sentence.
        """
        tokens = self.tokenize(sent)
        translated = self.generate_translation(tokens)
        result = self.get_decoded(translated)
        return result
