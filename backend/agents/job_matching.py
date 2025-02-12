import pandas as pd
# from sentence_transformers import SentenceTransformer


# backend/agents/job_matching.py
from backend.agents.base_agent import BaseAgent

class JobMatching(BaseAgent):
    """
    AI-powered job matching system that suggests job roles 
    based on candidate skills and experience.
    """

    def __init__(self):
        super().__init__()
        self.agent_name = "AI Job Matching"

    def match_job(self, candidate_skills: list) -> list:
        """
        Matches job roles based on skills.

        :param candidate_skills: List of candidate's skills.
        :return: List of suitable job roles.
        """
        job_database = {
            "Python": ["Software Engineer", "Data Scientist"],
            "Machine Learning": ["AI Engineer", "Data Scientist"],
            "HR Management": ["HR Manager", "Recruitment Specialist"],
            "Marketing": ["Digital Marketer", "SEO Specialist"]
        }

        matching_jobs = []
        for skill in candidate_skills:
            matching_jobs.extend(job_database.get(skill, []))

        return list(set(matching_jobs))  # Remove duplicates

    def recommend_candidates(self, job_role: str) -> list:
        """
        Suggests candidates for a given job role.

        :param job_role: The job position to fill.
        :return: List of matching candidates.
        """
        candidate_profiles = {
            "Software Engineer": ["Alice", "Bob"],
            "Data Scientist": ["Charlie", "David"],
            "HR Manager": ["Eve", "Frank"],
            "Digital Marketer": ["Grace", "Hannah"]
        }

        return candidate_profiles.get(job_role, ["No suitable candidates found."])

# Example usage
if __name__ == "__main__":
    agent = JobMatching()
    print(agent.match_job(["Python", "Machine Learning"]))
    print(agent.recommend_candidates("Software Engineer"))




class AIJobMatcher:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def match_candidate(self, job_description, resume_text):
        """Finds the best match between a job and a candidate's resume."""
        job_embedding = self.model.encode(job_description)
        resume_embedding = self.model.encode(resume_text)
        similarity_score = (job_embedding @ resume_embedding.T) / (
            (job_embedding * 2).sum() * 0.5 * (resume_embedding * 2).sum() * 0.5
        )
        return {"job_match_score": similarity_score}