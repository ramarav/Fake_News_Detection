import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()

def predict_news(news_text: str):
    cleaned = clean_text(news_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return "FAKE" if prediction == "FAKE" else "REAL"
