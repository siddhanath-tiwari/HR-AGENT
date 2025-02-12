import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import os

class OCRExtractor:
    def __init__(self, pdf_folder="database/policy_docs/"):
        self.pdf_folder = pdf_folder
        self.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path if needed
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from both text-based and scanned PDFs."""
        text = ""
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text()  # Extract selectable text
                    img = page.get_pixmap()
                    img_pil = Image.frombytes("RGB", [img.width, img.height], img.samples)
                    text += pytesseract.image_to_string(img_pil)  # OCR on images
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
        return text