import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials
import requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

# Firebase REST API endpoint
FIREBASE_API_KEY = "AIzaSyD14Agn9cl3gsZVkg0uHqUSgULaYh-hj3U"
FIREBASE_AUTH_URL = f"https://identitytoolkit.googleapis.com/v1/accounts"

# Helper function for Firebase REST API
def firebase_request(endpoint, data):
    url = f"{FIREBASE_AUTH_URL}:{endpoint}?key={FIREBASE_API_KEY}"
    response = requests.post(url, json=data)
    return response.json()

# Streamlit UI
def main():
    st.title("Firebase Authentication with Streamlit")

    # Tabs for Login and Sign-Up
    tabs = st.tabs(["Login", "Sign Up"])

    # Login Tab
    with tabs[0]:
        st.header("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            data = {
                "email": email,
                "password": password,
                "returnSecureToken": True,
            }
            response = firebase_request("signInWithPassword", data)

            if "idToken" in response:
                st.success("Login successful!")
                st.session_state["idToken"] = response["idToken"]
            else:
                st.error(response.get("error", {}).get("message", "Login failed."))

    # Sign-Up Tab
    with tabs[1]:
        st.header("Sign Up")
        new_email = st.text_input("New Email")
        new_password = st.text_input("New Password", type="password")

        if st.button("Sign Up"):
            try:
                user = auth.create_user(email=new_email, password=new_password)
                st.success("Account created successfully! You can now log in.")
            except Exception as e:
                st.error(f"Error creating account: {e}")

if __name__ == "__main__":
    main()
