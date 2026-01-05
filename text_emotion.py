import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ==============================
# Paths
# ==============================
DATA_PATH = "Data/text_emotion_processed.csv"
MODEL_PATH = "models/text_model.pkl"
VEC_PATH = "models/vectorizer.pkl"


def train_model():
    df = pd.read_csv(DATA_PATH)

    print("Columns:", df.columns)

    # 🔹 Remove rows with missing text or label
    df = df.dropna(subset=['clean_text', 'label'])

    # 🔹 Ensure text is string
    X_text = df['clean_text'].astype(str)
    y = df['label']

    print("Training samples:", len(df))

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(X_text)

    # Logistic Regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # Save model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    # Save vectorizer
    with open(VEC_PATH, 'wb') as f:
        pickle.dump(vectorizer, f)

    print("✅ Text emotion model trained successfully")



def predict_emotion(text):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    with open(VEC_PATH, 'rb') as f:
        vectorizer = pickle.load(f)

    text_vector = vectorizer.transform([text])

    emotion = model.predict(text_vector)[0]
    probabilities = model.predict_proba(text_vector)[0]
    confidence = float(round(max(probabilities) * 100, 2))


    return emotion, confidence
