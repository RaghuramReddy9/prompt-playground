import os
from dotenv import load_dotenv
import google.generativeai as genai

# Step 1: Load environment key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 2: Load prompt templates
def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

 # Load 3 prompt styles
direct_prompt = load_prompt("prompts/direct.txt")
role_prompt = load_prompt("prompts/role_based.txt")
cot_prompt = load_prompt("prompts/cot.txt")
scorer_prompt = load_prompt("prompts/scorer.txt")

# Step 3: Define the input for all prompt styles
input_text = "The movie felt long and confusing."

# Step 4: Fill in each prompt
prompt_direct = direct_prompt.replace("{REVIEW}", input_text)
prompt_role = role_prompt.replace("{REVIEW}", input_text)
prompt_cot = cot_prompt.replace("{REVIEW}", input_text)

# Step 5: Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 6: Generate responses
response_direct = model.generate_content(prompt_direct).text.strip()
response_role = model.generate_content(prompt_role).text.strip()
response_cot = model.generate_content(prompt_cot).text.strip()

# Step 7: Print results to inspect
print("\n--- Direct Prompt Response ---")
print(response_direct)

print("\n--- Role-Based Prompt Response ---")
print(response_role)

print("\n--- Chain-of-Thought Prompt Response ---")
print(response_cot)

# Step 8: Compare responses using the scorer prompt
compare_input = scorer_prompt.replace("{INPUT}", input_text)\
                             .replace("{A}", response_direct)\
                             .replace("{B}", response_cot)

# Step 9: Generate evaluation result
evaluation = model.generate_content(compare_input).text.strip()

print("\n--- Evaluation Between Direct vs Chain-of-Thought ---")
print(evaluation)

# Step 10: Compare Role-Based vs Direct
compare_input_2 = scorer_prompt.replace("{INPUT}", input_text)\
                                .replace("{A}", response_role)\
                                .replace("{B}", response_direct)

evaluation_2 = model.generate_content(compare_input_2).text.strip()

print("\n--- Evaluation Between Role-Based vs Direct ---")
print(evaluation_2)

# Step 11: Compare Chain-of-Thought vs Role-Based
compare_input_3 = scorer_prompt.replace("{INPUT}", input_text)\
                                .replace("{A}", response_cot)\
                                .replace("{B}", response_role)

evaluation_3 = model.generate_content(compare_input_3).text.strip()

print("\n--- Evaluation Between Chain-of-Thought vs Role-Based ---")
print(evaluation_3)


