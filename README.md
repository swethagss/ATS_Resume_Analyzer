# 📄 ATS Resume Analyzer

This project is an **AI-powered Resume analysis** tool built using **Streamlit** and **Google Gemini AI**. It evaluates resumes against job descriptions, providing a detailed assessment, keyword analysis, and match percentage.

## 🔹 Features
- Upload Resume- Upload your resume in PDF format
- Job Description - Paste the job description for comparision
- Analysis Options :
  - **In-Depth Resume Assessment** – Comprehensive analysis, highlighting strengths, weaknesses, and improvements.
  - **Job Fit Percentage** – Calculates match percentage, detects missing keywords, and identifies skill gaps.
- **AI-Powered Insights** – Uses Google Gemini AI to provide professional feedback.
- **Export Results** – Download the analysis as a text file for reference.

## 🖥️ Tech Stack
- **Streamlit** - Web interface for user interaction 
- **Google Gemini AI** - Generates detailed resume analysis
- **PymuPDF (Fitz)** - Extract text from PDF resumes
- **dotenv** - Securely manages API keys and configuration

## Setup Instructions
1. Clone the Repository
```
git clone <repository-url>
cd <repository-folder>

```

2. Install Dependencies
```
pip install -r requirements.txt
```
3. Create a .env file: Add your Google API key to the .env file.
```
GOOGLE_API_KEY=your_google_api_key_here
```
4. **Run the Streamlit app:** After installing the required libraries and setting up the .env file, run the app using:
```
streamlit run app1.py
```

## How to Use
1. **Upload your Resume** - Click on Upload your resume and upload a PDF
2. **Paste Job description** - Copy & Paste the job description
3. **Choose Analysis Type** - Select either **In-Depth Resume Assessment** or **Job Fit Percentage**
4. **Click Get Your Results** – The AI will analyze your resume
5. **Download Report** - Click Export Analysis to save the results

#### In-Depth Resume Assessment
- Overall compatibility with the job.
- Strengths & matching qualifications.
- Areas for improvement.
- Final suitability assessment.
#### Job Fit Percentage
- Overall match percentage.
- Identified & missing keywords.
- Skill gap analysis.
- Actionable recommendations.



