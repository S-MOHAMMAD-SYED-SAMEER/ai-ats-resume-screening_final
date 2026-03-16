import streamlit as st
from auth.user_manager import add_user, change_password, delete_user


def show_user_management():

    st.title("User Management")

    st.subheader("Create User")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["recruiter", "admin"])

    if st.button("Create User"):

        if add_user(new_user, new_pass, role):
            st.success("User created")

        else:
            st.error("User already exists")

    st.markdown("---")

    st.subheader("Change Password")

    username = st.text_input("Username for password change")
    new_password = st.text_input("New Password", type="password")

    if st.button("Update Password"):

        if change_password(username, new_password):
            st.success("Password updated")

        else:
            st.error("User not found")

    st.markdown("---")

    st.subheader("Delete User")

    del_user = st.text_input("Username to delete")

    if st.button("Delete User"):

        if delete_user(del_user):
            st.success("User removed")

        else:
            st.error("Cannot delete user")