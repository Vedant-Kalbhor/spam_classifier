import streamlit as st
import pickle
import pandas as pd                  
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 

                 #read binary mode 
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

from sklearn.utils.validation import check_is_fitted

try:
    check_is_fitted(model)
    print("✅ Model is fitted and ready to use.")
except:
    print("❌ Model is NOT fitted. Retrain and save it again.")



def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]

    for w in text:
        if w.isalnum():
            y.append(w)
    
    text=y[:]
    y.clear()

    for w in text:
        if w not in stopwords.words('english') and w not in string.punctuation:
            y.append(w)

    text=y[:]
    y.clear()
    stemmer = PorterStemmer()
    for w in text:
        y.append(stemmer.stem(w))

    return " ".join(y)



# with open('transform_text.pkl','rb') as f:
#     transform_text=pickle.load(f)

st.title("Email Spam Classifier")

input_sms=st.text_area("Enter the message")


if st.button('Predict'):
    #1.Preprocess
    transformed_sms=transform_text(input_sms)

    #2.Vectorize
    vector_input=tfidf.transform([transformed_sms])

    #3.Predict
    #model.fit(vector_input)
    result = model.predict(vector_input)[0]

    #4.Display
    if result ==1:
        st.header("SPAM")
    else:
        st.header("NOT SPAM")



