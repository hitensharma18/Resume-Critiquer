# AI Resume Critiquer
# Learning project built by following a tutorial and experimenting with Streamlit and OpenAI API.

import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found. Please check your .env file.")
    st.stop()

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targetting (optional)")

analyze = st.button("Analyze Resume")



def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")    
        
if analyze and not uploaded_file:
    st.warning("Please upload a resume first.")
    
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not contain any text......")
            st.stop()
        
        # WORD COUNT FEATURE
        word_count = len(file_content.split())
        st.info(f"Resume Word Count: {word_count} words")

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Also provide:
        - A resume score out of 10 
        - Key strengths
        - Key weaknesses
        - Suggested improvements

        Also compare the resume with the job description provided by the user
        Provide:
        - ATS match score (out of 100%)
        - Missing Keywords
        - Suggested improvements to better align with the job description
        
        focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience description
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""

        client = OpenAI(api_key=OPENAI_API_KEY)
        with st.spinner("Analyzing your resume..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
        st.success("Analysis completed!")
        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)

        # DOWNLOAD FEATURE
        st.download_button(
            label="Download Feedback",
            data=response.choices[0].message.content,
            file_name="resume_feedback.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
