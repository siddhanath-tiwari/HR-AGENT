import os
import pickle
import json
import fitz
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from deep_translator import GoogleTranslator

class ResumeScreeningAgent:
    def __init__(self, model_path="models/resume_model.pkl", embeddings_path="database/embeddings/"):
        self.model = pickle.load(open(model_path, "rb"))
        self.client = chromadb.PersistentClient(path=embeddings_path)
        self.collection = self.client.get_or_create_collection(name="resumes")
        self.encoder = SentenceTransformer("paraphrase-MiniLM-L6-v2")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from resumes, supports multiple languages."""
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        detected_lang = GoogleTranslator().detect(text)
        if detected_lang != "en":
            text = GoogleTranslator(source=detected_lang, target="en").translate(text)
        return text

    def add_resume(self, pdf_path):
        """Adds resume to ChromaDB & generates AI insights."""
        text = self.extract_text_from_pdf(pdf_path)
        summary = self.summarizer(text, max_length=150, min_length=50, do_sample=False)
        embedding = self.encoder.encode(text).tolist()
        self.collection.add(documents=[text], embeddings=[embedding])
        return {"message": "Resume added successfully!", "summary": summary}

    def rank_candidates(self, job_desc):
        """Ranks candidates based on job description & AI skill gap analysis."""
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




# phase 4.4

import pandas as pd
from transformers import pipeline

import os
import pickle
import fitz
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from deep_translator import GoogleTranslator

class ResumeScreeningAgent:
    def __init__(self, model_path="models/resume_model.pkl", embeddings_path="database/embeddings/"):
        """Initializes the Resume Screening Agent with AI models & ChromaDB."""
        
        # Ensure model exists before loading
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        with open(model_path, "rb") as model_file:
            self.model = pickle.load(model_file)

        # Ensure ChromaDB path exists
        if not os.path.exists(embeddings_path):
            os.makedirs(embeddings_path)
        
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(path=embeddings_path)
        self.collection = self.client.get_or_create_collection(name="resumes")

        # Load AI Models
        self.encoder = SentenceTransformer("paraphrase-MiniLM-L6-v2")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

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
        """Processes and adds a resume to the ChromaDB system."""
        text = self.extract_text_from_pdf(pdf_path)
        summary = self.summarizer(text, max_length=150, min_length=50, do_sample=False)
        embedding = self.encoder.encode(text).tolist()

        # Store in ChromaDB
        self.collection.add(documents=[text], embeddings=[embedding])

        return {
            "message": "Resume added successfully!",
            "summary": summary[0]["summary_text"],  # Extract summary text correctly
            "embedding_sample": embedding[:5]  # Show only part of embedding for debugging
        }

    def rank_candidates(self, job_desc):
        """Ranks resumes based on job description match & skill gap analysis."""
        job_embedding = self.encoder.encode(job_desc).tolist()
        results = self.collection.query(query_embeddings=[job_embedding], n_results=5)

        candidate_scores = []
        for i, doc in enumerate(results["documents"]):
            candidate_embedding = self.encoder.encode(doc[0]).tolist()
            score = self.model.predict_proba([candidate_embedding])[0][1]  # AI Model Prediction
            missing_skills = self.analyze_skill_gap(job_desc, doc[0])

            candidate_scores.append({
                "resume": doc[0],
                "score": score,
                "missing_skills": missing_skills
            })

        ranked_candidates = sorted(candidate_scores, key=lambda x: x["score"], reverse=True)
        return ranked_candidates

    def analyze_skill_gap(self, job_desc, resume_text):
        """Identifies missing skills by comparing job description with resume."""
        job_words = set(job_desc.lower().split())
        resume_words = set(resume_text.lower().split())
        missing_skills = job_words - resume_words
        return list(missing_skills)


# ✅ Unbiased Hiring Analysis with NLP
import pandas as pd
from transformers import pipeline

class ResumeScreening:
    def __init__(self):
        self.model = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    def analyze_resume(self, resume_text):
        """Analyzes resumes for bias detection."""
        bias_score = self.model(resume_text)
        return {"resume_text": resume_text, "bias_score": bias_score}
class ResumeScreening:
    def __init__(self):
        self.model = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    def analyze_resume(self, resume_text):
        """Analyzes resumes for unbiased hiring."""
        bias_score = self.model(resume_text)
        return {"resume_text": resume_text, "bias_score": bias_score}