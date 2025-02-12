from setuptools import setup, find_packages

# requirements.txt se dependencies read karne ke liye function
def parse_requirements(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="HR_Bot_Agentic_AI",
    version="1.0.0",
    author="siddhanath-tiwari",
    author_email="pratimatiwari8299@gmail.com",
    description="A Multi-Agent AI-powered HR Chatbot using ChromaDB for Recruitment & Customer Support",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/HR_Bot_Agentic_AI",  # Update with your GitHub repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),  # Auto-load dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "hrbot=main:run",  # Ensure your main.py has a run() function
        ]
    },
)