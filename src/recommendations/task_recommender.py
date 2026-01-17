TASK_MAP = {
    "happy": ["Creative tasks", "Brainstorming", "Collaborative work"],
    "neutral": ["Routine tasks", "Documentation", "Regular work items"],
    "sad": ["Light Individual tasks", "Review work", "Supportive activities"],
    "stressed": ["Take Short Break", "Low-pressure tasks", "Task Rescheduling"],
    "angry": ["Cooldown", "No meetings", "Solo tasks"]
}

HIGH_CONF = 0.8
MODERATE_CONF = 0.6
LOW_CONF = 0.4

def recommend_task(final_emotion, confidence):
    if confidence < LOW_CONF:                      # VERY LOW CONFIDENCE -> No Strong Recommendation
        return "No strong recommendation (insufficient confidence)" 
    elif confidence < MODERATE_CONF:               # LOW CONFIDENCE -> Neutral-safe Tasks
        return TASK_MAP.get("neutral", [])
    elif confidence < HIGH_CONF:                   # MODERATE CONFIDENCE -> Soft Recommendation
        return TASK_MAP.get(final_emotion, TASK_MAP["neutral"])
    # HIGH CONFIDENCE -> Strong Recommendation
    return TASK_MAP.get(final_emotion, TASK_MAP["neutral"])