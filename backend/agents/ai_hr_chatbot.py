# phase 4.4


import openai
from deep_translator import GoogleTranslator

class AIHRChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def translate_query(self, query, target_lang="en"):
        """Translates query to English before AI processing."""
        return GoogleTranslator(source="auto", target=target_lang).translate(query)

    def get_response(self, query, language="en"):
        """Generates AI-powered HR responses in multiple languages."""
        query_in_english = self.translate_query(query, "en")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query_in_english}]
        )
        response_text = response["choices"][0]["message"]["content"]
        return GoogleTranslator(source="en", target=language).translate(response_text)