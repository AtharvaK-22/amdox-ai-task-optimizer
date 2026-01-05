def fuse_emotions(text_result, face_result):
    text_emotion, text_conf = text_result
    face_emotion, face_conf = face_result

    if face_conf > text_conf:
        return face_emotion, face_conf
    else:
        return text_emotion, text_conf
