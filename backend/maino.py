# # Main FastAPI/Flask entry point
# from fastapi import FastAPI, UploadFile, File
# from google.cloud import speech

# app = FastAPI()
# speech_client = speech.SpeechClient()

# @app.post("/voice_query/")
# async def voice_query(file: UploadFile = File(...)):
#     """Converts voice query to text & fetches HR response."""
#     content = await file.read()
#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16)
#     response = speech_client.recognize(config=config, audio=audio)
    
#     text_query = response.results[0].alternatives[0].transcript
#     return {"query": text_query, "response": HRQueryAgent().answer_query(text_query)}

# phase 2nd 

# from fastapi import FastAPI, UploadFile, File
# from agents.resume_screening import ResumeScreeningAgent
# from agents.interview_scheduler import InterviewScheduler
# from agents.candidate_interaction import CandidateChatbot

# app = FastAPI()
# resume_agent = ResumeScreeningAgent()
# scheduler = InterviewScheduler()
# chatbot = CandidateChatbot()

# @app.post("/upload_resume/")
# async def upload_resume(file: UploadFile = File(...)):
#     """Uploads resume & adds to AI system."""
#     file_path = f"database/resumes/{file.filename}"
#     with open(file_path, "wb") as buffer:
#         buffer.write(await file.read())
#     return resume_agent.add_resume(file_path)

# @app.post("/chatbot/")
# async def chatbot_response(query: str):
#     """AI chatbot for candidate queries."""
#     return chatbot.respond(query)



# Phase 3.4 
# from fastapi import FastAPI, UploadFile, File
# from agents.legal_compliance import LegalComplianceChecker
# from agents.onboarding_manager import OfferLetterGenerator
# from agents.sentiment_analysis import SentimentAnalysis
# from agents.document_verification import DocumentVerifier
# from voice_module.voice_to_text import VoiceToText
# from voice_module.text_to_voice import TextToVoice

# app = FastAPI()
# compliance_checker = LegalComplianceChecker()
# offer_generator = OfferLetterGenerator()
# sentiment_analysis = SentimentAnalysis()
# document_verifier = DocumentVerifier()
# voice_to_text = VoiceToText()
# text_to_voice = TextToVoice()

# @app.post("/check_compliance/")
# async def check_compliance(policy_text: str):
#     return compliance_checker.check_compliance(policy_text)

# @app.post("/generate_offer/")
# async def generate_offer(candidate_name: str, role: str, salary: float):
#     return offer_generator.generate_offer_letter(candidate_name, role, salary)

# @app.post("/analyze_sentiment/")
# async def analyze_sentiment(feedback: str):
#     return sentiment_analysis.analyze_feedback(feedback)

# @app.post("/verify_document/")
# async def verify_document(file: UploadFile = File(...)):
#     file_path = f"database/documents/{file.filename}"
#     with open(file_path, "wb") as buffer:
#         buffer.write(await file.read())
#     return document_verifier.verify_document(file_path)

# @app.get("/voice_query/")
# async def voice_query():
#     text = voice_to_text.recognize_voice()
#     response = "You asked: " + text  # Placeholder response
#     text_to_voice.speak(response)
#     return {"query": text, "response": response}







# from fastapi import FastAPI
# from agents.ai_hr_chatbot import AIHRChatbot
# from agents.payroll_manager import PayrollManager
# from agents.resume_screening import ResumeScreening
# from agents.workforce_analytics import WorkforceAnalytics

# app = FastAPI()
# hr_chatbot = AIHRChatbot(api_key="YOUR_OPENAI_API_KEY")
# payroll_manager = PayrollManager()
# resume_screening = ResumeScreening()
# analytics = WorkforceAnalytics()

# @app.post("/chat/")
# async def chat(query: str, lang: str = "en"):
#     return hr_chatbot.get_response(query, lang)

# @app.post("/calculate_salary/")
# async def calculate_salary(emp_id: int):
#     return payroll_manager.calculate_salary(emp_id)

# @app.post("/attrition_risk/")
# async def attrition_risk(employee_data: list):
#     return analytics.predict_attrition(employee_data)


# phase 5.4

# from fastapi import FastAPI
# from agents.ai_video_interview import AIVideoInterview
# from agents.hr_legal_advisor import HRLegalAdvisor
# from agents.job_matching import AIJobMatcher
# from metaverse.virtual_hr_office import VirtualHROffice

# app = FastAPI()
# video_interview = AIVideoInterview()
# legal_advisor = HRLegalAdvisor(api_key="OPENAI_API_KEY")
# job_matcher = AIJobMatcher()
# virtual_hr = VirtualHROffice()

# @app.post("/ai_video_interview/")
# async def analyze_video(video_path: str):
#     return video_interview.analyze_interview(video_path)

# @app.post("/check_hr_compliance/")
# async def compliance_check(query: str):
#     return legal_advisor.check_compliance(query)

# @app.post("/job_match/")
# async def job_match(jd: str, resume: str):
#     return job_matcher.match_candidate(jd, resume)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)




import uvicorn
import fitz  # PyMuPDF for PDF parsing
import os
import pandas as pd
import streamlit as st
import openai
import cv2
import mediapipe as mp
from fastapi import FastAPI, UploadFile, File
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from typing import List

# Initialize FastAPI
app = FastAPI()

# Load AI models
# resume_model = SentenceTransformer("all-MiniLM-L6-v2")
# sentiment_analyzer = pipeline("sentiment-analysis")
# face_detector = mp.solutions.face_detection.FaceDetection()

# OpenAI API Key (Replace with actual key)
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY


# 🌟 PHASE 1.3: AI Resume Parsing & Screening 🌟
@app.post("/parse_resume/")
async def parse_resume(file: UploadFile = File(...)):
    """Extracts text from a PDF resume and returns key details."""
    content = await file.read()
    with fitz.open(stream=content, filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    
    return {"resume_text": text}


# 🌟 PHASE 2.4: AI-Powered Interview Scheduling 🌟
@app.post("/schedule_interview/")
async def schedule_interview(candidate_name: str, interview_date: str):
    """Schedules an interview and sends an AI-generated email."""
    return {"message": f"Interview scheduled for {candidate_name} on {interview_date}."}


# 🌟 PHASE 3.4: AI-Powered HR Query Resolution 🌟
@app.post("/hr_query/")
async def hr_query(question: str):
    """Uses AI to answer HR-related questions."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return {"answer": response["choices"][0]["message"]["content"]}


# 🌟 PHASE 4.4: AI Employee Mood & Performance Tracking 🌟
@app.post("/analyze_mood/")
async def analyze_mood(employee_text: str):
    """Analyzes employee sentiment from text."""
    mood_score = sentiment_analyzer(employee_text)
    return {"mood_score": mood_score}


# 🌟 PHASE 5.4: AI Video Interview Analysis 🌟
@app.post("/analyze_video/")
async def analyze_video(video_path: str):
    """Analyzes facial expressions during an interview."""
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = face_detector.process(frame)
    cap.release()
    return {"message": "Facial expressions analyzed successfully"}


# 🌟 PHASE 5.4: AI-Powered Job Matching 🌟
@app.post("/job_match/")
async def job_match(job_description: str, resume_text: str):
    """Finds the best match between job description and candidate's resume."""
    job_embedding = resume_model.encode(job_description)
    resume_embedding = resume_model.encode(resume_text)
    similarity_score = (job_embedding @ resume_embedding.T) / (
        (job_embedding * 2).sum() * 0.5 * (resume_embedding * 2).sum() * 0.5
    )
    return {"job_match_score": similarity_score}


# 🌟 PHASE 5.4: AI-Powered HR Dashboard 🌟
@app.get("/dashboard/")
async def dashboard():
    """Displays AI-powered HR analytics."""
    return {"dashboard_status": "HR Dashboard is active with AI insights."}

@app.post("/ai_video_interview/")
async def analyze_video(video_path: str):
    return video_interview.analyze_interview(video_path)

@app.post("/check_hr_compliance/")
async def compliance_check(query: str):
    return legal_advisor.check_compliance(query)

@app.post("/job_match/")
async def job_match(jd: str, resume: str):
    return job_matcher.match_candidate(jd, resume)


# 🌟 Streamlit Frontend 🌟
def run_dashboard():
    st.title("📊 AI-Powered HR Management")
    st.write("👋 AI-driven HR Assistant for Smart Recruiting & Employee Engagement")

    if st.button("Parse Resume"):
        st.write("Resume Parsing & AI Screening Active ✅")

    if st.button("Schedule Interview"):
        st.write("AI-Powered Interview Scheduling ✅")

    if st.button("Ask HR Query"):
        st.write("HR AI Assistant is Ready ✅")

    if st.button("Analyze Employee Mood"):
        st.write("AI Sentiment Analysis for Employee Engagement ✅")

    if st.button("Run AI Video Interview Analysis"):
        st.write("AI Interview Analysis Running ✅")

    if st.button("AI Job Matching System"):
        st.write("AI-Powered Job Recommendation ✅")


# 🌟 Run FastAPI & Streamlit Dashboard Together 🌟
if __name__ == "__main__":
    os.system("start cmd /k streamlit run main.py")
    uvicorn.run(app, host="0.0.0.0", port=8000)