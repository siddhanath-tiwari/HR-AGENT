from flask import Flask, request, jsonify
import os
import sys

# Ensure that the script finds the 'metaverse' folder
sys.path.append(os.path.abspath("."))

# Import required modules
from metaverse.virtual_hr_office import VirtualHROffice
from agents.ai_video_interview import AIVideoInterview
from agents.hr_legal_advisor import HRLegalAdvisor
from agents.job_matching import AIJobMatcher

# Initialize Flask app
app = Flask(__name__)

# Initialize AI Components
video_interview = AIVideoInterview()
legal_advisor = HRLegalAdvisor(api_key="your_api_key_here")
job_matcher = AIJobMatcher()
virtual_hr = VirtualHROffice()


@app.route("/")
def home():
    return jsonify({"message": "Welcome to AI-Powered HR Automation System!"})


@app.route("/virtual_office", methods=["GET"])
def enter_office():
    name = request.args.get("name")
    if name:
        return jsonify({"message": virtual_hr.welcome_employee(name)})
    else:
        return jsonify({"error": "Please provide a name"}), 400


@app.route("/ai_video_interview", methods=["POST"])
def analyze_video():
    data = request.get_json()
    video_path = data.get("video_path")
    if video_path:
        return jsonify(video_interview.analyze_interview(video_path))
    return jsonify({"error": "Missing video_path"}), 400


@app.route("/check_hr_compliance", methods=["POST"])
def compliance_check():
    data = request.get_json()
    query = data.get("query")
    if query:
        return jsonify(legal_advisor.check_compliance(query))
    return jsonify({"error": "Missing query"}), 400


@app.route("/job_match", methods=["POST"])
def job_match():
    data = request.get_json()
    jd = data.get("jd")
    resume = data.get("resume")
    if jd and resume:
        return jsonify(job_matcher.match_candidate(jd, resume))
    return jsonify({"error": "Missing jd or resume"}), 400


# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
