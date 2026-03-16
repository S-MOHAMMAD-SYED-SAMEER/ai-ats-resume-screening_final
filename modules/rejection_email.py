import streamlit as st
from core.email_list_generator import generate_email_list


def show_rejection_email():

    st.title("Rejection Email Generator")

    if "results" not in st.session_state:

        st.warning("Run resume analysis first")
        return

    df = st.session_state.results

    selected = st.multiselect(
        "Select Rejected Candidates",
        df["Name"]
    )

    rejected_df = df[df["Name"].isin(selected)]

    if st.button("Generate Email List"):

        email_list = generate_email_list(rejected_df)

        st.text_area(
            "Copy Email List",
            email_list,
            height=150
        )