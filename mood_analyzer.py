def analyze_mood(text):
  """
  basic placeholder mood analyzer
  for now just looks for keywords and returns a simple mood
  """

  text = text.lower()

  if "happy" in text or "good" in text or "great" in text:
      return "happy"
  elif "sad" in text or "bad" in text or "unhappy" in text:
      return "sad"
  elif "tired" in text or "exhausted" in text or "sleepy" in text:
      return "tired"
  elif "anxious" in text or "worried" in text or "nervous" in text:
      return "anxious"
  else:
      return "neutral"
