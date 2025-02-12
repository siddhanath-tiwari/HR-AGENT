# phase 4.4

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class WorkforceAnalytics:
    def __init__(self, model_path="models/attrition_model.pkl"):
        self.model = RandomForestClassifier()
        self.model.load(model_path)

    def predict_attrition(self, employee_data):
        """Predicts which employees are likely to leave."""
        prediction = self.model.predict([employee_data])
        return {"Attrition Risk": "High" if prediction[0] else "Low"}