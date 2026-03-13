**# AI Resume Critiquer**

AI Resume Critiquer is a Streamlit application that analyzes resumes using the OpenAI API and provides detailed feedback to help improve resume quality.

Users can upload their resume, optionally add a job role and job description, and receive AI-generated suggestions, strengths, weaknesses, and ATS-style insights.

**# Features**

AI-powered resume analysis  
Resume score out of 10  
Key strengths and weaknesses  
ATS match insights based on job descriptions  
Missing keyword suggestions  
Resume word count  
Downloadable feedback report  
Supports PDF and TXT resumes  

**## Environment Variables**

Create a `.env` file in the project root and add your OpenAI API key.

OPENAI_API_KEY=your_api_key_here

The `.env` file is not included in this repository for privacy reasons.

**## Technologies Used**

Python  
Streamlit  
OpenAI API  
PyPDF2  
python-dotenv  

**## Learning Source**

This project was inspired by Project 2 from the following tutorial:

https://www.youtube.com/watch?v=XZdY15sHUa8&t=2773s

The implementation was extended with additional features such as resume word count, ATS comparison, and downloadable feedback.
