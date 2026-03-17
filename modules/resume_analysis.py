import streamlit as st
import pandas as pd

from core.resume_parser import extract_text, extract_email, extract_phone, extract_name
from core.advanced_scoring import extract_experience_years
from core.advanced_scoring import calculate_ats_score


def show_resume_analysis():

    st.title("Resume Analysis")

    job_description = st.text_area("Paste Job Description")

    uploaded_files = st.file_uploader(
        "Upload Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("Analyze Candidates"):

        results = []

        cid = 1

        for file in uploaded_files:

            text = extract_text(file)

            score = calculate_ats_score(text, job_description)

            name = extract_name(text)
            email = extract_email(text)
            phone = extract_phone(text)

            # EXPERIENCE DETECTION
            exp_years = extract_experience_years(text)

            if exp_years == 0:
                exp = "Fresher / <1 yr"
            else:
                exp = f"{exp_years} yrs"

            results.append({
                "Rank": 0,
                "Candidate ID": f"CAND-{cid}",
                "Name": name,
                "Score": score,
                "Email": email,
                "Phone": phone,
                
            })

            cid += 1

        df = pd.DataFrame(results)

        df = df.sort_values(by="Score", ascending=False)

        df["Rank"] = range(1, len(df)+1)

        st.session_state.resume_results = df

    # SAFE DISPLAY BLOCK
    if "resume_results" in st.session_state:

        df = st.session_state.resume_results

        st.subheader("All Candidates")
        st.dataframe(df, use_container_width=True)