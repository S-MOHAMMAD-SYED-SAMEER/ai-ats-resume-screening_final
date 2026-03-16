AI ATS Resume Screening System

This project is a simple AI-based resume screening tool built with Streamlit.

Features
• Login portal
• User management (admin can add/update/delete users)
• Upload resumes (PDF / DOCX)
• Paste job description
• Analyze candidates
• Automatic candidate ranking
• Candidate profile view
• Generate rejection email list
• HR can copy emails and send rejection emails through Outlook

Project Structure

ATS_SYSTEM_V3

app.py – Main application

pages
    1_resume_analysis.py – Resume analysis page
    2_rejection_email.py – Rejection email generator

core
    resume_parser.py – Extract candidate info
    section_parser.py – Extract resume sections
    scoring_engine.py – Calculate candidate score
    email_list_generator.py – Generate email list

auth
    auth_service.py – Login system
    user_manager.py – User management

utils
    pdf_reader.py – Read resume files
    text_cleaner.py – Clean text
    keyword_extractor.py – Extract keywords

logo
    client_logo.jpeg

users.json – User credentials
requirements.txt – Required libraries

How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the system

streamlit run app.py

The system will open in your browser.

Default Login

Username: admin
Password: admin123