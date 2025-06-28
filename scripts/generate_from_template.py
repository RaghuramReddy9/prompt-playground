import os
from dotenv import load_dotenv
import google.generativeai as genai

# Step 1: Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Step 2: Load the prompt template from file
with open("prompts/sentiment_template.txt", "r", encoding="utf-8") as f:
    template = f.read()

# Step 3: List of example user reviews to classify
reviews = [
    "The movie was fantastic and had great acting.",
    "It was boring and I almost fell asleep.",
    "The visuals were good, but the plot made no sense."
]

# Step 4: Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 5: Loop through each review and generate sentiment
for i, review in enumerate(reviews, start=1):
    prompt = template.replace("{REVIEW}", review)
    print(f"\n--- Review {i} ---\n{review}")
    response = model.generate_content(prompt)
    print("Sentiment:", response.text.strip())
