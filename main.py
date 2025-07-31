from mood_analyzer import analyze_mood
from datetime import datetime

entry = input("How are you feeling today?\n> ")
today = datetime.now().strftime("%m-%d-%Y")

mood = analyze_mood(entry)

with open("mood_log.txt", "a") as file:
    file.write(today + ": " + entry + " (Mood: " + mood + ")\n")

print("Your dated entry with mood was saved!")
