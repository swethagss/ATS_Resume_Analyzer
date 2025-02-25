import base64
import io
from dotenv import load_dotenv


load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import fitz

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel(model_name = 'models/gemini-2.0-flash-exp')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the pdf file
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # initializing list to store the text of each page
        text_parts = []

        for page in document:
            text_parts.append(page.get_text())
        
        pdf_text_content = " ".join(text_parts)
        return pdf_text_content
    else:
        raise FileNotFoundError("No File Uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume Expert", page_icon="📄", layout="wide")
st.header("AI-Powered Resume Reviewer")
st.markdown("""**This application helps you review your resume with the power of Gemini AI (LLM)**.

**Upload your Resume and Paste the Job description below:**

- Get a comprehensive review of your resume
- Identify areas to imporve your skills
- Identify which missing keywords are missing compared to the job description
- See the percentage match with the job description 
""")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=['pdf'],
help= "Please ensure your resume is in PDF format")
pdf_content = ""

if uploaded_file is not None:
    pdf_content = input_pdf_setup(uploaded_file)
    st.write("PDF Uploaded Successfully")
else:
    pdf_content = ""

if uploaded_file and input_text:
    st.header("Analysis Options")
    analysis_type = st.radio(
        "Select any option below:",
        ["In-Depth Resume Assessment", "Job Fit Percentage"]
    )

    if analysis_type == "In-Depth Resume Assessment":
        prompt = """
        As an experienced Technical Human Resource Manager, 
        please provide a comprehensive professional evaluation of the candidate's resume in relation to the job description. 
        Your analysis should address the following:
        1. Overall comptiblity with the position
        2. Key strengths and matching qualifications
        3. Significant defeciencies or areas for imporvement
        4. Concrete recommendations for enhancing the resume
        5. A final assessment of the candidates suitability for the role

        Please structure your response with clear headings and use a formal, professional tone.
        """
    else:
        prompt = """
        As an ATS (Applicant Tracking System) specialist, 
        analyze the resume based on the following criteria :
        1. Overall Percentage match 
        2. Key keywords identified in the resume
        3. Crucial missing keywords
        4. Analysis of skill gaps
        5. Actionable recommendations for imporvement
        Begin the response by prominently displaying the match percentage.
        """
    if st.button("Get Your Results 🎯"):
        with st.spinner("Analyzing your results..."):
            response = get_gemini_response(input_text, pdf_content, prompt)

        if response:
            st.markdown("**Analysis Results**")
            st.markdown(response)

            st.download_button(
                label = "📥 Export Analysis",
                data = response,
                file_name = "resume_analysis.txt",
                mime = "text/plain"
            )

else:
    st.info("Please upload your resume and provide the job description to begin the analysis.")