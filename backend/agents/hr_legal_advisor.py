import openai

class HRLegalAdvisor:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def check_compliance(self, query):
        """Checks if an HR decision complies with labor laws."""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
        )
        return response["choices"][0]["message"]["content"]