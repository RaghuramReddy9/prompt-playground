import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model object
model = genai.GenerativeModel("gemini-1.5-flash")

# Load prompt templates
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

extract_template = load_prompt("prompts/chain_step1_extract.txt")
formalize_template = load_prompt("prompts/chain_step2_formalize.txt")
decide_template = load_prompt("prompts/chain_step3_decide.txt")

def extract_summary(review_text):
    prompt = extract_template.replace("{REVIEW}", review_text)
    response = model.generate_content(prompt)
    summary = response.text.strip().replace("Summary:", "").strip()
    return summary

def formalize_summary(summary):
    prompt = formalize_template.replace("{SUMMARY}", summary)
    response = model.generate_content(prompt)
    return response.text.strip().replace("Formal Report:", "").strip()

def recommend_action(formal_report):
    prompt = decide_template.replace("{REPORT}", formal_report)
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    review = "The product I received had a broken screen. Very poor experience."

    summary = extract_summary(review)
    print("Summary: ", summary)

    formal = formalize_summary(summary)
    print("Formal Report: ", formal)

    decision = recommend_action(formal)
    print("Recommended Action: ", decision)

