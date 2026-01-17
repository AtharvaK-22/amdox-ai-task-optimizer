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

HIGH_CONF = 0.8
MODERATE_CONF = 0.6
LOW_CONF = 0.4

def recommend_task(final_emotion, confidence):
    if confidence < LOW_CONF:                      # VERY LOW CONFIDENCE -> No Strong Recommendation
        return "No strong recommendation (insufficient confidence)" 
    elif confidence < MODERATE_CONF:               # LOW CONFIDENCE -> Neutral-safe Tasks
        return "['Routine Tasks', 'Regular work items', 'Documentation']"
    elif confidence < HIGH_CONF:                   # MODERATE CONFIDENCE -> Soft Recommendation
        return TASK_MAP.get(final_emotion, TASK_MAP["neutral"])["moderate"]
    # HIGH CONFIDENCE -> Strong Recommendation
    return TASK_MAP.get(final_emotion, TASK_MAP["neutral"])["high"]

# Sample testing
# if __name__ == "__main__":
#     print(recommend_task("neutral", 0.9))
#     print(recommend_task("sad", 0.3))
#     print(recommend_task("angry", 0.82))