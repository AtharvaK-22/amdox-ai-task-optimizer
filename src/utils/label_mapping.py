# Final unified emotion classes
FINAL_EMOTION_CLASSES = ["happy","sad","angry","stressed","neutral"]

# Text dataset label mapping
TEXT_TO_FINAL = {
    "joy" : "happy",
    "happiness" : "happy",
    "neutral" : "neutral",
    "sadness" : "sad",
    "anger" : "angry",
    "frustration" : "angry",
    "stress" : "stressed",
    "worry" : "stressed",
    "fear" : "stressed",
    "anxiety" : "stressed",
}

# DeepFace dataset label mapping
DEEPFACE_TO_FINAL = {
    "happy": "happy",
    "neutral": "neutral",
    "sad": "sad",
    "angry": "angry",
    "fear": "stressed",
    "disgust": "stressed",
    "surprise": "neutral"
}
