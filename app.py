from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import os


nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

# Load pre-trained model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = [w for w in text if w.isalnum()]  # Remove special characters

    y = [w for w in y if w not in stopwords.words('english') and w not in string.punctuation]

    stemmer = PorterStemmer()
    y = [stemmer.stem(w) for w in y]

    return " ".join(y)

# API endpoint to classify text
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get("text", "")

    if not input_text.strip():
        return jsonify({"error": "Empty text provided"}), 400

    # 1. Preprocess text
    transformed_sms = transform_text(input_text)

    # 2. Vectorize text
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    return jsonify({"result": int(result)})

@app.route('/')
def home():
    return "Spam Classifier API is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000
    from waitress import serve
    serve(app, host="0.0.0.0", port=port)
