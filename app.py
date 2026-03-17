import streamlit as st
import os

from auth.auth_service import login, logout
from modules.resume_analysis import show_resume_analysis
from modules.experience_analysis import show_experience_analysis
from modules.user_management import show_user_management

st.set_page_config(page_title="AI ATS System", layout="wide")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None


# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("AI ATS Resume Screening System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        status, role = login(username, password)

        if status:

            st.session_state.logged_in = True
            st.session_state.role = role
            st.session_state.username = username

            st.rerun()

        else:
            st.error("Invalid username or password")

    st.stop()


# SIDEBAR AFTER LOGIN
with st.sidebar:

    st.write(f"Logged in as: {st.session_state.username}")

    st.markdown("---")
    st.title("Navigation")

    show_logo = st.checkbox("Show Logo", value=True)

    page = st.radio(
        "Navigation",
        [
            "Resume Analysis",
            "Experience Detection",
            "User Management"
        ]
    )

    st.markdown("---")

    if st.button("Logout"):
        logout()


# HEADER
if show_logo:

    col1, col2 = st.columns([1,5])

    with col1:
        st.image("logo/client_logo.jpeg", width=100)

    with col2:
        st.markdown("## Positive Childhood Alliance")
        st.markdown("### AI ATS Resume Screening System")


# PAGE ROUTER
if page == "Resume Analysis":
    show_resume_analysis()

elif page == "Experience Detection":
    show_experience_analysis()

elif page == "User Management":
    show_user_management()