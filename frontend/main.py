import streamlit as st
import requests

st.title("HR Bot Dashboard")

# if st.button("Check API Status"):
#     response = requests.get("http://127.0.0.1:5000/")
#     st.write(response.json())

# st.sidebar.header("Features")
# option = st.sidebar.selectbox("Choose a Function", ["HR Query", "Productivity Analysis"])

# if option == "HR Query":
#     user_query = st.text_input("Enter your HR question")
#     if st.button("Submit"):
#         response = requests.post("http://127.0.0.1:5000/hr_query", json={"query": user_query})
#         st.write(response.json())

# if option == "Productivity Analysis":
#     if st.button("Analyze Employee Productivity"):
#         response = requests.post("http://127.0.0.1:5000/productivity")
import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found in .env file. Please check your configuration.")
    st.stop()

# Base URL for your Flask API
BASE_URL = "http://127.0.0.1:5000"

# Helper function to call Flask API endpoints
def call_api(endpoint, data=None, files=None, method="POST"):
    url = f"{BASE_URL}/{endpoint}"
    try:
        print(f"Calling API endpoint: {url}")  # Debugging statement
        print(f"Payload being sent: {data}")   # Debugging statement
        if method == "POST":
            if files:
                response = requests.post(url, data=data, files=files)
            else:
                response = requests.post(url, json=data)
            response.raise_for_status()  # Raise HTTP errors
            print(f"Response received: {response.json()}")  # Debugging statement
            return response.json()
        else:
            raise ValueError("Unsupported HTTP method")
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
        return None
    except ValueError as e:
        st.error(f"Invalid response format: {str(e)}")
        return None

# Title of the app
st.title("HR Automation System")

# Home Section
st.header("Welcome to the HR Bot")
st.write("Choose an action from the menu")

# Sidebar Menu
st.sidebar.title("Select Action")
option = st.sidebar.selectbox(
    "Choose an action", 
    [
        "AIHR Chatbot", "Payroll Manager", "Resume Screening", 
        "Legal Compliance", "Offer Letter Generator", "Sentiment Analysis", 
        "Document Verification", "Voice to Text", "Text to Voice", 
        "AI Video Interview", "HR Legal Advisor", "Job Matching", 
        "Virtual HR Office"
    ]
)

# Generic function to handle API calls and display responses
def handle_api_call(endpoint, input_key, input_label, file_type=None, additional_data=None):
    if file_type:
        uploaded_file = st.file_uploader(input_label, type=file_type)
        if uploaded_file:
            files = {"file": uploaded_file}
            if st.button("Submit"):
                with st.spinner("Processing..."):
                    response = call_api(endpoint, data=additional_data, files=files)
                if response:
                    if "response" in response:
                        st.success("Response:")
                        st.write(response["response"])
                    elif "error" in response:
                        st.error(f"Error: {response['error']}")
                    else:
                        st.error("Invalid or empty response from API.")
    else:
        user_input = st.text_area(input_label)
        if st.button("Submit"):
            with st.spinner("Processing..."):
                data = {input_key: user_input}
                if additional_data:
                    data.update(additional_data)
                response = call_api(endpoint, data=data)
            if response:
                if "response" in response:
                    st.success("Response:")
                    st.write(response["response"])
                elif "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    st.error("Invalid or empty response from API.")

# Action Handlers
if option == "AIHR Chatbot":
    st.header("AIHR Chatbot")
    handle_api_call("aihr_chatbot", "query", "Enter your query:")

elif option == "Payroll Manager":
    st.header("Payroll Manager")
    handle_api_call("payroll_manager", "payroll_data", "Enter payroll data:")

# Add other actions similarly...