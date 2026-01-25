TASK_MAP = {
    "happy": {
        "moderate": ["Routine productive tasks", "Light Collaborative work"],
        "high": ["Creative tasks", "Team Meetings"]
    },
    "neutral": {
        "moderate": ["Routine Tasks"],
        "high": ["Regular work items", "Documentation"]
    },
    "sad": {
        "moderate": ["Low Pressure tasks", "Supportive activities"],
        "high" : ["Very light Individual tasks", "Supportive activities"]
    },
    "stressed": {
        "moderate": ["Reduce Workload", "Work on low-pressure tasks"],
        "high": ["Take Short Break", "Reschedule demanding tasks"]
    },
    "angry": {
        "moderate": ["Independent work"],
        "high": ["Cool-down break", "Avoid meetings"]
    }
}
STRESS_SOFT_THRESHOLD = 0.35
HIGH_CONF = 0.8
MODERATE_CONF = 0.6
LOW_CONF = 0.4

def recommend_task(final_emotion, confidence):

    # Special handling for stress
    if final_emotion == "stressed" and (HIGH_CONF >= confidence >= STRESS_SOFT_THRESHOLD):
        return {
            "emotion": "stressed",
            "confidence": confidence,
            "recommendation_level": "soft",
            "tasks": [
                "Reduce workload temporarily",
                "Focus on low-pressure tasks",
                "Take short breaks if needed"
            ]
        }

    # Very low confidence → neutral
    if confidence < LOW_CONF:
        return {
            "emotion": "neutral",
            "confidence": confidence,
            "recommendation_level": "none",
            "tasks": ["No strong recommendation (low confidence)"]
        }

    # Low confidence → neutral-safe
    if confidence < MODERATE_CONF:
        return {
            "emotion": final_emotion,
            "confidence": confidence,
            "recommendation_level": "low",
            "tasks": TASK_MAP.get("neutral", [])
        }
    
    # Moderate / High confidence
    level = "moderate" if confidence < HIGH_CONF else "high"
    return {
        "emotion": final_emotion,
        "confidence": confidence,
        "recommendation_level": level,
        "tasks": TASK_MAP.get(final_emotion, TASK_MAP["neutral"])
    }

# Sample testing
# if __name__ == "__main__":
#     print(recommend_task("neutral", 0.9))
#     print(recommend_task("sad", 0.3))
#     print(recommend_task("angry", 0.82))