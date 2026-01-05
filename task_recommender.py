TASK_MAP = {
    "happy": ["Creative work", "Brainstorming", "Presentations"],
    "neutral": ["Routine tasks", "Documentation", "Emails"],
    "sad": ["Light tasks", "Review work", "Support tasks"],
    "stressed": ["Break", "Low-pressure tasks", "Breathing exercise"],
    "angry": ["Cooldown", "No meetings", "Solo tasks"]
}

def recommend_task(emotion):
    return TASK_MAP.get(emotion, ["General tasks"])
