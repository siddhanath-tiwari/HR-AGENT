from transformers import pipeline

class CandidateChatbot:
    def __init__(self):
        self.chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

    def respond(self, user_query):
        """Generates AI-based candidate interaction responses."""
        response = self.chatbot(user_query, max_length=100, num_return_sequences=1)
        return response[0]["generated_text"]