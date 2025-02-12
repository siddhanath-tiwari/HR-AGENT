import pandas as pd
from transformers import pipeline

class EmployeeProductivity:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def analyze_mood(self, employee_text):
        """Detects stress levels based on chat/email sentiment."""
        mood_score = self.sentiment_analyzer(employee_text)
        return {"employee_text": employee_text, "mood_score": mood_score}