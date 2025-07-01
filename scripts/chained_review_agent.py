import os
from dotenv import load_dotenv
import google.generativeai as genai

# Step 1: Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Step 2: Load all 3 prompt templates
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        return content


extract_template = load_prompt("prompts/chain_step1_extract.txt")
formalize_template = load_prompt("prompts/chain_step2_formalize.txt")
decide_template = load_prompt("prompts/chain_step3_decide.txt")

# Step 3: Sample review
review_text = "I ordered a new laptop and it arrived with scratches on the screen. Very disappointed!"

# Step 4: Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 5: Step 1 – Extract Key Summary
extract_prompt = extract_template.replace("{REVIEW}", review_text)
summary_response = model.generate_content(extract_prompt)
summary = summary_response.text.strip().replace("Summary:", "").strip()
print("Step 1 - Summary: ", summary)


# Step 6: Step 2 – Formalize Summary
formal_prompt = formalize_template.replace("{SUMMARY}", summary)
formal_response = model.generate_content(formal_prompt)
formal_report = formal_response.text.strip().replace("Formal Report:", "").strip()
print("Step 2 - Formal Report:",formal_report)

# Step 7: Step 3 – Recommend Action
decision_prompt = decide_template.replace("{REPORT}", formal_report)
action_response = model.generate_content(decision_prompt)
action = action_response.text.strip()
print("Step 3 - Recommended Action: ", action)
