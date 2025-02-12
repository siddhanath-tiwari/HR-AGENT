# backend/agents/ai_training_manager.py
from backend.agents.base_agent import BaseAgent

class AITrainingManager(BaseAgent):
    """
    AI-powered training manager for employee skill enhancement.
    It recommends learning modules and tracks progress.
    """

    def __init__(self):
        super().__init__()
        self.agent_name = "AI Training Manager"

    def recommend_courses(self, job_role: str) -> list:
        """
        Suggests training courses based on job role.

        :param job_role: The employee's job title.
        :return: List of recommended courses.
        """
        course_catalog = {
            "Software Engineer": ["Python for Beginners", "AI & Machine Learning", "System Design"],
            "HR Manager": ["Employee Engagement Strategies", "HR Analytics", "Labor Laws & Compliance"],
            "Marketing Specialist": ["Digital Marketing", "SEO Strategies", "Consumer Psychology"]
        }

        return course_catalog.get(job_role, ["General Business Ethics", "Effective Communication"])

    def track_progress(self, employee_id: str) -> dict:
        """
        Retrieves training progress of an employee.

        :param employee_id: Unique identifier for the employee.
        :return: Training progress details.
        """
        progress_data = {
            "EMP001": {"Python for Beginners": "Completed", "AI & Machine Learning": "In Progress"},
            "EMP002": {"HR Analytics": "Completed", "Labor Laws & Compliance": "Not Started"},
            "EMP003": {"Digital Marketing": "In Progress", "SEO Strategies": "Not Started"},
        }

        return progress_data.get(employee_id, {"message": "No records found."})

# Example usage
if __name__ == "__main__":
    agent = AITrainingManager()
    print(agent.recommend_courses("Software Engineer"))
    print(agent.track_progress("EMP001"))