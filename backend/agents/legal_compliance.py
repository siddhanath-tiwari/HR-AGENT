# phase 3.4  of2

import json
from transformers import pipeline

class LegalComplianceChecker:
    def __init__(self, model_path="models/compliance_model.pkl"):
        self.model = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    def check_compliance(self, policy_text):
        """Checks HR policies for legal violations using AI."""
        analysis = self.model(policy_text)
        return {"policy": policy_text, "compliance_status": analysis}