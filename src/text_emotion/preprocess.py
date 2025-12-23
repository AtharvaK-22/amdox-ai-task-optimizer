import re
import nltk
import pandas as pd
from nltk.corpus import stopwards
from nltk.stem import WordNetLemmatizer 
from src.utils.label_mapping import TEXT_TO_FINAL

nltk.download('stopwords')
nltk.download('wordnet')

stop_wards = set(stopwards.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text  =re.sub(r"[^a-z\s]", "" , text)
    tokens = text.split()
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_wards
    ]
    return " ".join(tokens)

def preprocess_dataset(input_path, output_path):
    df = pd.read_csv(input_path)
    #rename columns to standard names if needed
    df.columns = ["text", "label"]
    # map labels to final emotion classes
    df["label"] = df["label"].map(TEXT_TO_FINAL)
    # drop unmapped labels
    df = df.dropna(subset = ["label"])
    # clean text data
    df["clean_text"] = df["text"].apply(clean_text)
    df[["clean_text", "label"]].to_csv(output_path, index = False)
    print("Text Emotion dataset preprocessed and saved to", output_path)

if __name__ == "__main__":
    preprocess_dataset( "data/raw/text_emotion.csv", "data/processed/text_emotion_processed.csv" )