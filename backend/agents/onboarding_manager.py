## 3.4 onboards autodocumented, training and HR meeting
from docx import Document

class OfferLetterGenerator:
    def __init__(self, template_path="templates/offer_template.docx"):
        self.template = Document(template_path)

    def generate_offer_letter(self, candidate_name, role, salary):
        """Creates personalized offer letter from a template."""
        for paragraph in self.template.paragraphs:
            paragraph.text = paragraph.text.replace("{CANDIDATE_NAME}", candidate_name)
            paragraph.text = paragraph.text.replace("{ROLE}", role)
            paragraph.text = paragraph.text.replace("{SALARY}", str(salary))
        
        output_path = f"database/contracts/{candidate_name}_Offer_Letter.docx"
        self.template.save(output_path)
        return f"Offer letter saved at {output_path}"