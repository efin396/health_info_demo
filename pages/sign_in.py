import streamlit as st

# Dummy user credentials
USER_CREDENTIALS = {"doctor": "doctor"}

def sign_in():
    st.title("Sign In")
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    if st.button("Sign In"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.switch_page("pages/search.py")  # Navigate to the Main Page
        else:
            st.error("Invalid credentials. Please try again.")

# Initialize authentication flag if not already set
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# If already authenticated, automatically switch to Main Page
if st.session_state["authenticated"]:
    st.switch_page("pages/search.py")
else:
    sign_in()
