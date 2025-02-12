# import os
# import sys
# from flask import Flask, request, jsonify
# import fitz  # PyMuPDF for PDF parsing
# import pandas as pd
# import openai
# import cv2
# import mediapipe as mp
# from google.cloud import speech
# from sentence_transformers import SentenceTransformer
# from transformers import pipeline

# # Ensure backend folder is accessible
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# # Import AI modules
# from backend.agents.ai_hr_chatbot import AIHRChatbot
# from backend.agents.payroll_manager import PayrollManager
# from backend.agents.resume_screening import ResumeScreeningAgent
# from backend.agents.legal_compliance import LegalComplianceChecker
# from backend.agents.onboarding_manager import OfferLetterGenerator
# from backend.agents.sentiment_analysis import SentimentAnalysis
# from backend.agents.document_verification import DocumentVerifier
# from backend.voice_module.voice_to_text import VoiceToText
# from backend.voice_module.text_to_voice import TextToVoice
# from backend.agents.ai_video_interview import AIVideoInterview
# from backend.agents.hr_legal_advisor import HRLegalAdvisor
# from backend.agents.job_matching import AIJobMatcher
# from backend.metaverse.virtual_hr_office import VirtualHROffice

# # Initialize AI Models
# resume_model = SentenceTransformer("all-MiniLM-L6-v2")
# sentiment_analyzer = pipeline("sentiment-analysis")
# face_detector = mp.solutions.face_detection.FaceDetection()

# # Initialize Flask app
# app = Flask(__name__)

# # Initialize AI Agents
# agent = ResumeScreeningAgent()
# print(agent.add_resume("sample_resume.pdf"))
# print(agent.rank_candidates("Python Developer with NLP experience"))

# # resume_agent = ResumeScreeningAgent()
# chatbot = AIHRChatbot()
# virtual_hr = VirtualHROffice()

# # Initialize Google Speech-to-Text Client
# speech_client = speech.SpeechClient()

# @app.route("/")
# def home():
#     return jsonify({"message": "HR Bot API is Running 🚀"})

# @app.route("/virtual_office", methods=["GET"])
# def enter_office():
#     name = request.args.get("name")
#     if name:
#         return jsonify({"message": virtual_hr.welcome_employee(name)})
#     return jsonify({"error": "Please provide a name"}), 400

# @app.route("/upload_resume", methods=["POST"])
# def upload_resume():
#     """Uploads resume & adds to AI system."""
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["file"]
#     file_path = f"database/resumes/{file.filename}"
#     file.save(file_path)

#     return jsonify(resume_agent.add_resume(file_path))

# @app.route("/voice_query", methods=["POST"])
# def voice_query():
#     """Converts voice query to text & fetches HR response."""
#     if "file" not in request.files:
#         return jsonify({"error": "No audio file uploaded"}), 400

#     file = request.files["file"]
#     audio_content = file.read()

#     # Google Speech-to-Text processing
#     audio = speech.RecognitionAudio(content=audio_content)
#     config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16)
#     response = speech_client.recognize(config=config, audio=audio)

#     if not response.results:
#         return jsonify({"error": "No speech detected"}), 400

#     text_query = response.results[0].alternatives[0].transcript
#     return jsonify({"query": text_query, "response": chatbot.respond(text_query)})

# @app.route("/chatbot", methods=["POST"])
# def chatbot_response():
#     """AI chatbot for candidate queries."""
#     data = request.get_json()
#     query = data.get("query")
#     if query:
#         return jsonify({"response": chatbot.respond(query)})
#     return jsonify({"error": "Query not provided"}), 400

# @app.route("/job_match", methods=["POST"])
# def job_match():
#     """Matches candidate resume with job description."""
#     data = request.get_json()
#     jd = data.get("jd")
#     resume = data.get("resume")
#     if jd and resume:
#         job_matcher = AIJobMatcher()
#         return jsonify(job_matcher.match_candidate(jd, resume))
#     return jsonify({"error": "Missing jd or resume"}), 400

# @app.route("/hr_compliance", methods=["POST"])
# def check_compliance():
#     """Checks HR compliance queries."""
#     data = request.get_json()
#     query = data.get("query")
#     if query:
#         compliance_checker = LegalComplianceChecker()
#         return jsonify(compliance_checker.check_compliance(query))
#     return jsonify({"error": "Query not provided"}), 400

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)



import os
import pickle
from flask import Flask, request, jsonify
import fitz  # PyMuPDF for PDF processing
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from deep_translator import GoogleTranslator

from backend.agents.ai_hr_chatbot import AIHRChatbot
from backend.agents.payroll_manager import PayrollManager
from backend.agents.resume_screening import ResumeScreeningAgent
from backend.agents.legal_compliance import LegalComplianceChecker
from backend.agents.onboarding_manager import OfferLetterGenerator
from backend.agents.sentiment_analysis import SentimentAnalysis
from backend.agents.document_verification import DocumentVerifier
from backend.voice_module.voice_to_text import VoiceToText
from backend.voice_module.text_to_voice import TextToVoice
from backend.agents.ai_video_interview import AIVideoInterview
from backend.agents.hr_legal_advisor import HRLegalAdvisor
from backend.agents.job_matching import AIJobMatcher
from backend.metaverse.virtual_hr_office import VirtualHROffice

# Create Flask App
app = Flask(__name__)

# Ensure required directories exist
os.makedirs("models", exist_ok=True)
os.makedirs("database/embeddings", exist_ok=True)

# ✅ Load or Create Dummy Model
model_path = "models/resume_model.pkl"
if not os.path.exists(model_path):
    from sklearn.linear_model import LogisticRegression
    X_train = np.random.rand(10, 10)
    y_train = np.random.randint(0, 2, 10)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("✅ Dummy model created and saved.")
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

# ✅ Initialize AI Tools
chroma_client = chromadb.PersistentClient(path="database/embeddings/")
collection = chroma_client.get_or_create_collection(name="resumes")
encoder = SentenceTransformer("paraphrase-MiniLM-L6-v2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Initialize feature classes
class ResumeScreeningAgent:
    def __init__(self):
        self.model = model
        self.collection = collection
        self.encoder = encoder
        self.summarizer = summarizer

    def extract_text_from_pdf(self, pdf_path):
        """Extracts and translates text from a PDF resume."""
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        detected_lang = GoogleTranslator().detect(text)
        if detected_lang != "en":
            text = GoogleTranslator(source=detected_lang, target="en").translate(text)
        return text

    def add_resume(self, pdf_path):
        """Extracts text, embeds, and stores resume in ChromaDB."""
        text = self.extract_text_from_pdf(pdf_path)
        summary = self.summarizer(text, max_length=150, min_length=50, do_sample=False)
        embedding = self.encoder.encode(text).tolist()
        self.collection.add(documents=[text], embeddings=[embedding])
        return {"message": "Resume added successfully!", "summary": summary}

    def rank_candidates(self, job_desc):
        """Ranks candidates based on job description matching."""
        job_embedding = self.encoder.encode(job_desc).tolist()
        results = self.collection.query(query_embeddings=[job_embedding], n_results=5)

        candidate_scores = []
        for i, doc in enumerate(results["documents"]):
            candidate_features = np.random.rand(10)  # Simulated features
            score = self.model.predict_proba([candidate_features])[0][1]  # ML prediction
            missing_skills = self.analyze_skill_gap(job_desc, doc[0])
            candidate_scores.append({"resume": doc[0], "score": score, "missing_skills": missing_skills})

        ranked_candidates = sorted(candidate_scores, key=lambda x: x["score"], reverse=True)
        return ranked_candidates

    def analyze_skill_gap(self, job_desc, resume_text):
        """Compares job description and resume to identify missing skills."""
        job_words = set(job_desc.lower().split())
        resume_words = set(resume_text.lower().split())
        missing_skills = job_words - resume_words
        return list(missing_skills)


# Initialize all features here
resume_agent = ResumeScreeningAgent()
# Other agents like AIHRChatbot, PayrollManager, etc., will be similarly initialized

# API Routes
@app.route("/")
def home():
    return jsonify({"message": "HR Bot API is Running"})


@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    """Uploads and processes a resume PDF."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    file_path = os.path.join("database/resumes", file.filename)
    os.makedirs("database/resumes", exist_ok=True)

    file.save(file_path)
    result = resume_agent.add_resume(file_path)
    return jsonify(result)


@app.route("/rank_candidates", methods=["POST"])
def rank_candidates():
    """Ranks candidates based on job description."""
    data = request.get_json()
    if "job_desc" not in data:
        return jsonify({"error": "Job description missing"}), 400

    job_desc = data["job_desc"]
    ranked_results = resume_agent.rank_candidates(job_desc)
    return jsonify(ranked_results)


# Add other features (AIHRChatbot, PayrollManager, etc.) below

# AIHRChatbot API Route
@app.route("/ai_hr_chatbot", methods=["POST"])
def ai_hr_chatbot():
    query = request.json.get("query")
    response = AIHRChatbot().respond(query)
    return jsonify({"response": response})


# PayrollManager API Route
@app.route("/payroll_manager", methods=["POST"])
def payroll_manager():
    payroll_data = request.json.get("payroll_data")
    response = PayrollManager().process_payroll(payroll_data)
    return jsonify({"response": response})


# Resume Screening API Route (already implemented above)


# LegalComplianceChecker API Route
@app.route("/check_compliance", methods=["POST"])
def check_compliance():
    query = request.json.get("query")
    response = LegalComplianceChecker().check_compliance(query)
    return jsonify({"response": response})


# OfferLetterGenerator API Route
@app.route("/generate_offer_letter", methods=["POST"])
def generate_offer_letter():
    candidate_data = request.json.get("candidate_data")
    response = OfferLetterGenerator().generate_offer(candidate_data)
    return jsonify({"response": response})


# SentimentAnalysis API Route
@app.route("/sentiment_analysis", methods=["POST"])
def sentiment_analysis():
    text = request.json.get("text")
    response = SentimentAnalysis().analyze_sentiment(text)
    return jsonify({"response": response})


# DocumentVerifier API Route
@app.route("/verify_document", methods=["POST"])
def verify_document():
    file = request.files['document']
    file_path = f"temp/{file.filename}"
    file.save(file_path)
    response = DocumentVerifier().verify(file_path)
    return jsonify({"response": response})


# VoiceToText API Route
@app.route("/voice_to_text", methods=["POST"])
def voice_to_text():
    file = request.files['audio']
    file_path = f"temp/{file.filename}"
    file.save(file_path)
    response = VoiceToText().convert(file_path)
    return jsonify({"response": response})


# TextToVoice API Route
@app.route("/text_to_voice", methods=["POST"])
def text_to_voice():
    text = request.json.get("text")
    response = TextToVoice().convert(text)
    return jsonify({"response": response})


# AIVideoInterview API Route
@app.route("/analyze_video_interview", methods=["POST"])
def analyze_video_interview():
    file = request.files['video']
    file_path = f"temp/{file.filename}"
    file.save(file_path)
    response = AIVideoInterview().analyze_interview(file_path)
    return jsonify({"response": response})


# HRLegalAdvisor API Route
@app.route("/hr_legal_advisor", methods=["POST"])
def hr_legal_advisor():
    query = request.json.get("query")
    response = HRLegalAdvisor().advise(query)
    return jsonify({"response": response})


# AIJobMatcher API Route
@app.route("/job_matching", methods=["POST"])
def job_matching():
    job_desc = request.json.get("job_desc")
    resume = request.json.get("resume")
    response = AIJobMatcher().match_job(job_desc, resume)
    return jsonify({"response": response})


# VirtualHROffice API Route
@app.route("/virtual_hr_office", methods=["POST"])
def virtual_hr_office():
    name = request.json.get("name")
    response = VirtualHROffice().welcome_employee(name)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
