# Define the folder structure
import os

FOLDERS = [
    "HR_Bot_Agentic_AI",
    "HR_Bot_Agentic_AI/agents",
    "HR_Bot_Agentic_AI/database",
    "HR_Bot_Agentic_AI/database/embeddings",
    "HR_Bot_Agentic_AI/models",
    "HR_Bot_Agentic_AI/scripts"
]

# Define the files with optional default content
FILES = {
    "HR_Bot_Agentic_AI/_init_.py": "",
    "HR_Bot_Agentic_AI/agents/_init_.py": "",
    "HR_Bot_Agentic_AI/agents/resume_screening.py": "# Resume shortlisting agent",
    "HR_Bot_Agentic_AI/agents/interview_scheduler.py": "# Auto scheduling agent",
    "HR_Bot_Agentic_AI/agents/hr_query_agent.py": "# FAQ answering agent",
    "HR_Bot_Agentic_AI/database/_init_.py": "",
    "HR_Bot_Agentic_AI/models/_init_.py": "",
    "HR_Bot_Agentic_AI/models/resume_model.pkl": "",
    "HR_Bot_Agentic_AI/scripts/_init_.py": "",
    "HR_Bot_Agentic_AI/scripts/preprocess.py": "# Data cleaning script",
    "HR_Bot_Agentic_AI/scripts/train_model.py": "# Model training script",
    "HR_Bot_Agentic_AI/app.py": "# Main FastAPI/Flask entry point",
    "HR_Bot_Agentic_AI/requirements.txt": "# Dependencies",
    "HR_Bot_Agentic_AI/README.md": "# Documentation"
}

def create_structure():
    """Creates the required folder structure and files."""
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)

    for file_path, content in FILES.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ HR Bot structure created successfully in VS Code!")

if __name__ == "__main__":
    create_structure()