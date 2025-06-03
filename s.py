import streamlit as st
import requests

st.title("📧 Spam Classifier")

user_input = st.text_area("Enter your message:")

if st.button("Classify"):
    if user_input.strip():
        response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
        if response.status_code == 200:
            result = response.json()["result"]
            label = "🚫 Spam" if result == 1 else "✅ Not Spam"
            st.success(f"Prediction: {label}")
        else:
            st.error("Error from backend: " + response.text)
    else:
        st.warning("Please enter some text.")
