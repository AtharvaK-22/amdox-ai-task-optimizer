from src.text_emotion.predict import predict_text_emotion
from src.facial_emotion import detect_face_emotion
from src.fusion import fuse_emotions
from src.recommendations import recommend_task

text = input("Enter how you feel: ")

text_result = predict_text_emotion(text)
face_result = detect_face_emotion()

final_emotion, confidence = fuse_emotions(text_result, face_result)
tasks = recommend_task(final_emotion, confidence)

print("\nFinal Emotion:", final_emotion)
print("Confidence:", confidence)
print("Recommended Tasks:", tasks)
