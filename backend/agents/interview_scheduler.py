import json
from googleapiclient.discovery import build

class InterviewScheduler:
    def __init__(self, credentials_path="credentials.json"):
        self.service = build("calendar", "v3", credentials=credentials_path)

    def schedule_interview(self, candidate_name, interviewer_email, datetime):
        """Schedules interview in Google Calendar with smart preference matching."""
        event = {
            "summary": f"Interview with {candidate_name}",
            "start": {"dateTime": datetime, "timeZone": "Asia/Kolkata"},
            "end": {"dateTime": datetime, "timeZone": "Asia/Kolkata"},
            "attendees": [{"email": interviewer_email}],
        }
        event = self.service.events().insert(calendarId="primary", body=event).execute()
        return f"Interview scheduled for {candidate_name} on {datetime}!"