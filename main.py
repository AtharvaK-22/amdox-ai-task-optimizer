from text_emotion import predict_emotion
from face_emotion import detect_face_emotion
from emotion_fusion import fuse_emotions
from task_recommender import recommend_task

text = input("Enter how you feel: ")

text_result = predict_emotion(text)
face_result = detect_face_emotion()

final_emotion, confidence = fuse_emotions(text_result, face_result)
tasks = recommend_task(final_emotion)

print("\nFinal Emotion:", final_emotion)
print("Confidence:", confidence)
print("Recommended Tasks:", tasks)
