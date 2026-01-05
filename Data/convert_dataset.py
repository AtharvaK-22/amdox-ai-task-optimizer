import pandas as pd

files = ["train.txt", "test.txt", "val.txt"]
data = []

for file in files:
    with open(f"data/{file}", "r", encoding="utf-8") as f:
        for line in f:
            text, emotion = line.strip().split(";")
            data.append([text, emotion])

df = pd.DataFrame(data, columns=["text", "emotion"])

df.to_csv("data/text_emotion.csv", index=False)

print("✅ text_emotion.csv created successfully")
