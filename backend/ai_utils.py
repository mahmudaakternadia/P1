import requests
import os

# Set your Hugging Face or OpenAI API key as environment variable or directly here
HF_API_TOKEN = os.environ.get("HF_API_TOKEN", "YOUR_HF_API_TOKEN")

def summarize_text(text):
    # Hugging Face summarization (e.g., facebook/bart-large-cnn)
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": text}
    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
        headers=headers,
        json=payload,
        timeout=30,
    )
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    return "Unable to summarize."

def classify_needs(text):
    # Dummy classifier: in production, use a fine-tuned classifier or prompt LLM
    keywords = {
        "medical": ["injury", "hospital", "ambulance", "doctor", "medicine"],
        "food": ["food", "hunger", "meal", "eat"],
        "water": ["water", "drink", "thirst"],
        "shelter": ["shelter", "home", "roof", "tent"],
        "rescue": ["trapped", "rescue", "help", "save"]
    }
    needs = []
    text_lower = text.lower()
    for need, words in keywords.items():
        if any(w in text_lower for w in words):
            needs.append(need)
    return needs if needs else ["general assistance"]

# You can extend this with image classification, translation, etc.