class BaseAgent:
    def __init__(self, name):
        self.name = name

    def process_request(self, request):
        """Process the request (to be overridden by child classes)."""
        raise NotImplementedError("Subclasses must implement process_request method.")
    
    def get_agent_name(self):
        return self.name