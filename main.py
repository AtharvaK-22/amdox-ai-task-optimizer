#!/usr/bin/env python3
"""
AMDOX AI Task Optimizer - Main Application
AI-powered decision support system for workplace wellness
"""

import sys
import cv2
from src.text_emotion.predict import predict_text_emotion
from src.facial_emotion.face_detect import detect_face
from src.facial_emotion.emotion_detect import detect_facial_emotion
from src.fusion.emotion_fusion import fuse_emotions
from src.recommendations.task_recommender import recommend_tasks

def get_text_emotion():
    """Get emotion from user text input"""
    print("\n📝 Text Emotion Analysis")
    text = input("Enter how you feel today: ").strip()
    
    if not text:
        return "neutral", 0.0
    
    emotion, confidence = predict_text_emotion(text)
    print(f"Text Emotion: {emotion} (Confidence: {confidence:.1%})")
    return emotion, confidence

def get_facial_emotion():
    """Get emotion from camera/facial analysis"""
    print("\n📷 Facial Emotion Analysis")
    print("Press SPACE to capture, ESC to skip, Q to quit")
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Camera not available, skipping facial analysis")
        return "neutral", 0.0
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Show preview
            cv2.imshow('Facial Emotion Capture (SPACE to capture, ESC to skip)', frame)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord(' '):  # Space to capture
                face_img = detect_face(frame)
                if face_img is not None:
                    emotion, confidence = detect_facial_emotion(face_img)
                    print(f"Facial Emotion: {emotion} (Confidence: {confidence:.1%})")
                    cap.release()
                    cv2.destroyAllWindows()
                    return emotion, confidence
                else:
                    print("❌ No face detected, try again")
            
            elif key == 27:  # ESC to skip
                print("⏭️  Skipping facial analysis")
                cap.release()
                cv2.destroyAllWindows()
                return "neutral", 0.0
            
            elif key == ord('q'):  # Q to quit
                cap.release()
                cv2.destroyAllWindows()
                sys.exit(0)
    
    except Exception as e:
        print(f"❌ Facial analysis error: {e}")
        cap.release()
        cv2.destroyAllWindows()
        return "neutral", 0.0

def main():
    """Main application workflow"""
    print("🚀 AMDOX AI Task Optimizer")
    print("=" * 50)
    print("AI-powered workplace wellness and task optimization")
    print("Privacy-first emotion detection and task recommendations")
    print("=" * 50)
    
    try:
        # Step 1: Get text emotion
        text_result = get_text_emotion()
        
        # Step 2: Get facial emotion
        facial_result = get_facial_emotion()
        
        # Step 3: Fuse emotions
        print("\n🔄 Multi-Modal Emotion Fusion")
        final_emotion, final_confidence = fuse_emotions(text_result, facial_result)
        
        print(f"\n🎭 Final Emotion Analysis:")
        print(f"   Emotion: {final_emotion.upper()}")
        print(f"   Confidence: {final_confidence:.1%}")
        
        # Step 4: Get task recommendations
        print(f"\n📋 Task Recommendations for '{final_emotion}' mood:")
        tasks = recommend_tasks(final_emotion)
        
        for i, task in enumerate(tasks, 1):
            print(f"   {i}. {task}")
        
        print(f"\n💡 Tip: Tasks are optimized for your current emotional state")
        print(f"🔒 Privacy: No personal data stored, all processing done locally")
        
    except KeyboardInterrupt:
        print("\n👋 Thank you for using AMDOX AI Task Optimizer!")
    except Exception as e:
        print(f"\n❌ Application error: {e}")
        print("Please check your setup and try again.")

if __name__ == "__main__":
    main()