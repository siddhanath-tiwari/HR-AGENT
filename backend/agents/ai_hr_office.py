# backend/agents/ai_hr_office.py

from .base_agent import BaseAgent

class AIHROffice(BaseAgent):
    """
    AIHROffice - HR Assistant Agent
    Handles HR queries, employee records, and general HR assistance.
    """

    def __init__(self):
        super()._init_()
        self.employee_data = {
            "101": {"name": "Amit Sharma", "role": "Software Engineer", "department": "IT"},
            "102": {"name": "Neha Verma", "role": "HR Manager", "department": "HR"},
            "103": {"name": "Rahul Mehta", "role": "Sales Executive", "department": "Sales"}
        }

    def get_employee_info(self, emp_id):
        """Fetch employee details by ID."""
        return self.employee_data.get(emp_id, {"error": "Employee not found"})

    def handle_query(self, query):
        """Handles HR-related queries"""
        query = query.lower()

        if "leave policy" in query:
            return "Company provides 24 paid leaves annually, including sick and casual leaves."
        elif "work from home policy" in query:
            return "Employees can work from home twice a week as per company policy."
        elif "salary cycle" in query:
            return "Salaries are processed on the 1st of every month."
        else:
            return "I couldn't understand your query. Please contact HR for more details."

# For testing
if __name__ == "__main__":
    hr_agent = AIHROffice()
    print(hr_agent.get_employee_info("101"))
    print(hr_agent.handle_query("What is the leave policy?"))