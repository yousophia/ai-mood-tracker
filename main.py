from mood_analyzer import analyze_mood
from datetime import datetime
import os

entry = input("How are you feeling today?\n> ")
emotion = analyze_mood(entry)

date = datetime.now().strftime("%m-%d-%Y")

log_line = date + " | " + entry + " | Emotion: " + emotion + "\n"

with open("mood_log.txt", "a") as file:
    file.write(log_line)

print("Emotion detected: " + emotion)
print("Token:", os.getenv("HF_TOKEN"))
