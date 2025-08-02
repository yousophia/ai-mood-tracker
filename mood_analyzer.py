import requests
from dotenv import load_dotenv
import os

load_dotenv()

def analyze_mood(text):
    API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
    headers = {
        "Authorization": "Bearer {}".format(os.getenv("HF_TOKEN"))
    }

    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    if response.status_code == 200:
        predictions = response.json()[0]
        top_emotion = max(predictions, key=lambda x: x["score"])["label"]
        return top_emotion
    else:
        print("API error: " + response.text)
        return "unknown"
