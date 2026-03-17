import streamlit as st
import pandas as pd

from core.resume_parser import extract_text, extract_name
from core.advanced_scoring import extract_experience_years


def show_experience_analysis():

    st.title("Experience Detection")

    uploaded_files = st.file_uploader(
        "Upload Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("Analyze Experience"):

        results = []

        cid = 1

        for file in uploaded_files:

            text = extract_text(file)

            name = extract_name(text)

            exp_years = extract_experience_years(text)

            if exp_years == 0:
                exp = "Fresher / <1 yr"
            else:
                exp = f"{exp_years} yrs"

            results.append({
                "Candidate ID": f"CAND-{cid}",
                "Name": name,
                "Experience": exp
            })

            cid += 1

        df = pd.DataFrame(results)

        # ✅ STORE IN SESSION
        st.session_state.experience_results = df

    # ✅ DISPLAY STORED DATA
    if "experience_results" in st.session_state:

        df = st.session_state.experience_results
        st.dataframe(df, use_container_width=True)