import base64
import io
from dotenv import load_dotenv


load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
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
st.header("📄 ATS Resume Analyzer")
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
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me about the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("What are the keywords that are Missing")
submit4 = st.button("Percentage Match")

input_prompt = st.text_input("Queries: Feel Free to Ask here")

submit5 = st.button("Answer my Query") 

input_prompt1 = """
You are an experienced Technical Human resource Manager, you task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidates profile aligns with the role.
Higlight the strengths and weaknesses of the applicant in relation to the specified job requiremnets.
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in Data Science.
Your role is to analyze the resume based on the provided job description.
Share your insights on the candidates suitability for the role from an HR perspective. 
Additionaly, provide insights on skills enhancement and highlight areas for improvement.
"""

input_prompt3 = """
You are a skilled ATS (Application Trcaking system) scanner with deep undrestanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description. As a Human Resource Manager, assess the compatibility of the resume with the role. 
Give me what are the keywords that are missing and also matching. Also, provide recommendations for enhancing the candidates skills and identify which areas require further development.
"""

input_prompt4 = """
You are an skilled ATS (Application Tracking System) scanner with a deep understanding of Data Science and ATS functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description.
First the output should come as percentage and then keywords missing and last final thoughts.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume(PDF) file to proceed")


elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume(PDF) file to proceed")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the Resume(PDF) file to proceed")






