import requests

class ATSConnector:
    def __init__(self, ats_api_url):
        self.ats_api_url = ats_api_url

    def fetch_job_applications(self):
        """Fetches job applications from ATS."""
        response = requests.get(self.ats_api_url)
        return response.json()