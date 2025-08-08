# AI Mood Tracker 

A Python-based mood tracking application that uses Hugging Face's emotion detection model to analyze user input and log emotional data over time.

## Overview

Users enter a short description of how they’re feeling. The app sends that input to a pre-trained Hugging Face model (`distilbert-base-uncased-emotion`) which predicts the most likely emotion (e.g., joy, sadness, anger, etc.). The result is saved with a timestamp in a local mood log.

## Features

- Accepts natural language input describing mood
- Uses Hugging Face API for sentiment/emotion analysis
- Logs each entry with date, text, and predicted emotion
- Matplotlib-powered mood trend visualizations
- Flask web interface to display mood graphs

## Technologies

- Python 3
- Hugging Face Inference API
- `requests`, `datetime`, `os`, `dotenv`
- Git / GitHub for version control

## File Structure
- `main.py` — CLI interface for user input and logging  
- `mood_analyzer.py` — Contains API call and mood prediction logic  
- `mood_log.txt` — Stores historical entries  
- `plot_moods.py` — Script to visualize mood history  
- `app.py` — Flask web application to display mood graphs  
- `.env` — Stores API token (not committed)  
- `.gitignore` — Excludes sensitive or system files from Git  

## How to Run

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install requests python-dotenv matplotlib flask
3. Create a `.env` file and add your Hugging Face token like this:
```
HF_TOKEN=your_token_here 
```
4. Run the CLI app:
```bash
python3 main.py
