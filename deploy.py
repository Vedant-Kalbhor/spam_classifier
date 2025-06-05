# import streamlit as st
# import pickle
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# import os

# # --- Fix for NLTK data on deployment ---
# # Add local nltk_data folder to nltk data path
# nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
# nltk.data.path.append(nltk_data_path)

# # Remove nltk.download calls because they fail on deployment
# # nltk.download('punkt')
# # nltk.download('stopwords')

# # Load pre-trained model and vectorizer with caching
# @st.cache_data(show_spinner=False)
# def load_model_vectorizer():
#     with open('vectorizer.pkl', 'rb') as f:
#         tfidf = pickle.load(f)
#     with open('model.pkl', 'rb') as f:
#         model = pickle.load(f)
#     return tfidf, model

# tfidf, model = load_model_vectorizer()

# # Text preprocessing function
# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
#     text = [word for word in text if word.isalnum()]
#     stop_words = set(stopwords.words('english'))
#     text = [word for word in text if word not in stop_words]
#     stemmer = PorterStemmer()
#     text = [stemmer.stem(word) for word in text]
#     return " ".join(text)

# # Streamlit UI
# st.title("📧 Email Spam Classifier")

# user_input = st.text_area("Enter the email text here:")

# if st.button("Classify"):
#     if user_input.strip() == "":
#         st.error("Please enter some text to classify.")
#     else:
#         processed_text = transform_text(user_input)
#         vector_input = tfidf.transform([processed_text])
#         prediction = model.predict(vector_input)[0]
#         label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
#         st.success(f"Prediction: {label}")



import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import nltk

# Add nltk_data path manually
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Load stopwords manually (stopwords only requires one-time download)
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Load model and vectorizer
@st.cache_data(show_spinner=False)
def load_model_vectorizer():
    with open("vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return tfidf, model

tfidf, model = load_model_vectorizer()

# Custom tokenizer using regex
def transform_text(text):
    text = text.lower()
    text = re.findall(r'\b\w+\b', text)  # Tokenizes without punkt
    text = [word for word in text if word not in stop_words]
    text = [ps.stem(word) for word in text]
    return " ".join(text)

# UI
st.title("📧 Email Spam Classifier")

user_input = st.text_area("Enter the email text here:")

if st.button("Classify"):
    if user_input.strip() == "":
        st.error("Please enter some text to classify.")
    else:
        processed_text = transform_text(user_input)
        vector_input = tfidf.transform([processed_text])
        prediction = model.predict(vector_input)[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: {label}")
