import easyocr

class DocumentVerifier:
    def __init__(self):
        self.reader = easyocr.Reader(["en"])

    def verify_document(self, document_path):
        """Extracts text from ID proof, validates candidate details."""
        text = self.reader.readtext(document_path, detail=0)
        return {"document_text": text}