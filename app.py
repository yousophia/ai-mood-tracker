from flask import Flask, render_template
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def index():
    # Read mood data
    timestamps = []
    emotions = []
    with open("mood_log.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) >= 2:
                timestamps.append(datetime.strptime(parts[0].strip(), "%Y-%m-%d %H:%M:%S"))
                emotions.append(parts[1].strip())

    # Convert emotions to numbers
    unique_emotions = list(set(emotions))
    y_values = [unique_emotions.index(e) for e in emotions]

    # Plot graph
    plt.figure(figsize=(8, 4))
    plt.plot(timestamps, y_values, marker="o")
    plt.yticks(range(len(unique_emotions)), unique_emotions)
    plt.xlabel("Time")
    plt.ylabel("Emotion")
    plt.title("Mood History")
    plt.tight_layout()

    # Save plot to base64
    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template("index.html", graph_url=graph_url)

if __name__ == "__main__":
    app.run(debug=True)
