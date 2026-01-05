import cv2
from deepface import DeepFace

def detect_face_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "neutral", 0.0

    try:
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        emotion = result[0]['dominant_emotion']
        confidence = float(result[0]['emotion'][emotion])

        return emotion, confidence

    except Exception:
        return "neutral", 0.0
