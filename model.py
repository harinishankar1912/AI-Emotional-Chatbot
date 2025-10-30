from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def get_emotion(text):
