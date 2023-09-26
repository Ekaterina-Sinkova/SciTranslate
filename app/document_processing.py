class DocumentProcessor:
    """если нужно перевести документ"""
    def validate_file(self, file):
        if file.endswith('.docx'):
            return "Загружен файл правильного формата"
        else:
            return "Неверный формат загруженного файла"
    
    def tokenize_docx(self, file):
        # Your document tokenization code goes here
        # Example: Tokenize the DOCX file into sentences

        # Replace with actual implementation
        pass

    def detokenize_translation(self, sentences):
        # Your sentence concatenation code goes here
        # Example: Combine sentences into an output file

        # Replace with actual implementation
        pass

class TextProcessor():
    """если нужно перевести текст"""
    def tokenize_text(self, file):
        # Your document tokenization code goes here
        # Example: Tokenize the DOCX file into sentences

        # Replace with actual implementation
        pass

    def detokenize_translation(self, sentences):
        # Your sentence concatenation code goes here
        # Example: Combine sentences into an output file

        # Replace with actual implementation
        pass
    

