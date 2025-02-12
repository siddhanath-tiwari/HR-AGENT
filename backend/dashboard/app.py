# import streamlit as st
# import json

# st.title("📊 HR Query Analytics")

# with open("database/tags.json") as f:
#     tags_data = json.load(f)

# st.write("### 🏷️ Document Classification")
# st.json(tags_data)

# phase 2nd
# import streamlit as st
# import json

# st.title("📊 HR Recruitment Dashboard – Phase 2.4")

# st.write("### 📌 Top Ranked Candidates")
# with open("database/ranked_candidates.json") as f:
#     ranked_candidates = json.load(f)
# st.json(ranked_candidates)

# st.write("### 🔍 AI Skill Gap Analysis")
# with open("database/skill_gap_analysis.json") as f:
#     skill_gaps = json.load(f)
# st.json(skill_gaps)


#Phase 3.4

# import streamlit as st
# import json

# st.title("📊 AI-Powered HR Management – Phase 3.4")

# st.write("### 📌 Employee Sentiment Analysis")
# with open("database/sentiment_analysis.json") as f:
#     sentiment_data = json.load(f)
# st.json(sentiment_data)

# st.write("### 🔍 AI-Based Legal Compliance Report")
# with open("database/legal_compliance.json") as f:
#     compliance_report = json.load(f)
# st.json(compliance_report)


#phase 4.4

# import streamlit as st
# import json

# st.title("📊 AI-Powered HR Management – Phase 4.4")

# st.write("### 📌 Employee Attrition Risk Analysis")
# with open("database/attrition_analysis.json") as f:
#     attrition_data = json.load(f)
# st.json(attrition_data)

# st.write("### 🔍 Payroll & Leave Analytics")
# with open("database/payroll_summary.json") as f:
#     payroll_data = json.load(f)
# st.json(payroll_data)


# Phase 5.4

import streamlit as st

st.title("📊 AI-Powered HR Management – Phase 5.4")

st.write("### 🌍 AI Virtual HR Office")
st.write("👋 Experience AI-driven employee engagement in the metaverse!")

st.write("### 🎙 AI Video Interview Analytics")
st.write("🔍 AI evaluates candidate confidence & body language.")

st.write("### 🕵 AI-Powered Employee Productivity Monitoring")
st.write("⚡ AI predicts work engagement, stress levels, and retention risks.")




import streamlit as st
import PyPDF2
import os

# ----------------------- UI Setup -----------------------
st.set_page_config(page_title="HR Bot - Upload CV", layout="wide")

st.title("🤖 AI-Powered HR Assistant")

st.sidebar.header("📂 Upload Your Resume Here")
uploaded_file = st.sidebar.file_uploader("Upload PDF Resume", type=["pdf"])

# ----------------------- Resume Parsing -----------------------
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

if uploaded_file:
    st.sidebar.success("✅ Resume Uploaded Successfully!")

    # Extract text from uploaded resume
    resume_text = extract_text_from_pdf(uploaded_file)

    # Show parsed resume content (Summary Example)
    st.sidebar.subheader("📄 Extracted Resume Summary:")
    st.sidebar.write(resume_text[:500] + "...")  # Show first 500 characters

    # Example AI Screening Process
    st.sidebar.subheader("📊 AI Screening Result:")
    st.sidebar.write("✅ *Match Score:* 85%")
    st.sidebar.write("🔹 *Suggested Roles:* Data Scientist, ML Engineer")

# ----------------------- Chat UI -----------------------
st.subheader("💬 Chat with HR Bot")
chat_input = st.text_input("Type your message...")

if chat_input:
    if "upload cv" in chat_input.lower():
        st.write("📂 Please upload your CV from the sidebar!")
    else:
        st.write(f"🤖 AI Bot: I am processing your query - '{chat_input}'")

# ----------------------- End -----------------------