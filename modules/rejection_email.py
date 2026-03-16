import streamlit as st


def show_rejection_email():

    st.title("Rejection Email Generator")

    if "results" not in st.session_state:
        st.warning("Please analyze resumes first.")
        return

    df = st.session_state.results

    shortlisted = df[df["Shortlisted"] == "Yes"]
    rejected = df[df["Shortlisted"] == "No"]


    # -----------------------
    # SHORTLISTED
    # -----------------------

    st.subheader("Shortlisted Candidates")

    if len(shortlisted) == 0:
        st.info("No shortlisted candidates")

    else:

        selected_names = st.multiselect(
            "Select Candidate",
            shortlisted["Name"].tolist()
        )

        if selected_names:

            emails = shortlisted[
                shortlisted["Name"].isin(selected_names)
            ]["Email"].tolist()

            email_block = ", ".join(emails)

            st.markdown("### Selected Emails")

            st.code(email_block)


    st.divider()


    # -----------------------
    # REJECTED
    # -----------------------

    st.subheader("Rejected Candidates")

    if len(rejected) == 0:
        st.info("No rejected candidates")

    else:

        selected_names = st.multiselect(
            "Select Rejected Candidates",
            rejected["Name"].tolist()
        )

        if selected_names:

            emails = rejected[
                rejected["Name"].isin(selected_names)
            ]["Email"].tolist()

            email_block = ", ".join(emails)

            st.markdown("### Selected Emails")

            st.code(email_block)