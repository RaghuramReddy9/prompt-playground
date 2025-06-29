import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.prompts import PromptTemplate

# Step 1: Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Step 2: Load prompt template from file
with open("prompts/sentiment_template.txt", "r", encoding="utf-8") as f:
    template_str = f.read()

# Step 3: Set up LangChain prompt template
    prompt_template = PromptTemplate(
    input_variables=["REVIEW"],
    template=template_str
    )

# Step 4: Sample user reviews
reviews = [
    "The movie was fantastic and had great acting.",
    "It was boring and I almost fell asleep.",
    "The visuals were good, but the plot made no sense."
]

# Step 5: Initialize Gemini Flash
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 6: Generate sentiment for each review
for i, review in enumerate(reviews, start=1):
    final_prompt = prompt_template.format(REVIEW=review)
    print(f"\n--- Review {i} ---")
    print("Input:", review)
    response = model.generate_content(final_prompt)
    print("Sentiment:", response.text.strip())
