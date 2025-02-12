import json
import os

class DocumentClassifier:
    def __init__(self, policy_folder="database/policy_docs/", tags_file="database/tags.json"):
        self.policy_folder = policy_folder
        self.tags_file = tags_file
        self.tags = {
            "leave": "Leave Policy",
            "salary": "Compensation",
            "performance": "Performance Management",
            "benefits": "Employee Benefits",
            "hiring": "Recruitment Process",
        }

    def classify_document(self, text):
        """Classifies document based on keywords."""
        for keyword, category in self.tags.items():
            if keyword in text.lower():
                return category
        return "Uncategorized"

    def save_tags(self):
        """Saves classified document metadata."""
        data = {}
        for file in os.listdir(self.policy_folder):
            if file.endswith(".pdf"):
                text = OCRExtractor().extract_text_from_pdf(os.path.join(self.policy_folder, file))
                category = self.classify_document(text)
                data[file] = category

        with open(self.tags_file, "w") as f:
            json.dump(data, f)

# Run classification
# DocumentClassifier().save_tags()