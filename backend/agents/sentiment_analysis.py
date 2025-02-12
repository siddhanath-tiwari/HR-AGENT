import pandas as pd
from transformers import pipeline

class SentimentAnalysis:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def analyze_feedback(self, feedback_text):
        """Analyzes employee sentiment from feedback/reviews."""
        sentiment = self.model(feedback_text)
        return {"feedback": feedback_text, "sentiment": sentiment[0]["label"], "confidence": sentiment[0]["score"]}