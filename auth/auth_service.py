import json
import streamlit as st

def load_users():
    with open("users.json") as f:
        return json.load(f)


def login(username, password):
    users = load_users()

    if username in users and users[username]["password"] == password:
        return True, users[username]["role"]

    return False, None


def logout():
    st.session_state.logged_in = False
    st.rerun()