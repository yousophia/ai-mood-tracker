import matplotlib.pyplot as plt
from datetime import datetime

# Read mood data from file
timestamps = []
emotions = []

with open("mood_log.txt", "r") as file:
    for line in file:
        parts = line.strip().split("|")
        if len(parts) >= 2:
            timestamps.append(datetime.strptime(parts[0].strip(), "%Y-%m-%d %H:%M:%S"))
            emotions.append(parts[1].strip())

# Convert emotions to numeric values for plotting
unique_emotions = list(set(emotions))
y_values = [unique_emotions.index(e) for e in emotions]

# Plot graph
plt.figure(figsize=(10, 5))
plt.plot(timestamps, y_values, marker="o")
plt.yticks(range(len(unique_emotions)), unique_emotions)
plt.xlabel("Time")
plt.ylabel("Emotion")
plt.title("Mood History")
plt.tight_layout()

# Show the plot window
plt.show()
