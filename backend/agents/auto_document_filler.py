# backend/agents/auto_document_filler.py
from backend.agents.base_agent import BaseAgent

class AutoDocumentFiller(BaseAgent):
    """
    AI-powered document automation agent.
    It helps in filling HR forms, contracts, and other official documents.
    """

    def __init__(self):
        super().__init__()
        self.agent_name = "Auto Document Filler"

    def fill_document(self, template: str, data: dict) -> str:
        """
        Automatically fills a document template with provided data.

        :param template: Document template with placeholders.
        :param data: Dictionary containing values for placeholders.
        :return: Filled document text.
        """
        try:
            for key, value in data.items():
                template = template.replace(f"{{{{{key}}}}}", value)  # Replace placeholders
            return template
        except Exception as e:
            return f"Error in filling document: {str(e)}"

# Example usage
if __name__ == "__main__":
    agent = AutoDocumentFiller()
    template = "Dear {name},\nYour joining date is {date}. Welcome aboard!"
    data = {"name": "John Doe", "date": "10th Feb 2025"}
    print(agent.fill_document(template, data))