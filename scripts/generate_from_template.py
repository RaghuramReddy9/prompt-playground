import csv
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
review_data = [
    ("The movie was fantastic and had great acting.", "Positive"),
    ("It was boring and I almost fell asleep.", "Negative"),
    ("The visuals were good, but the plot made no sense.", "Negative")
]


# Step 5: Initialize Gemini Flash
model = genai.GenerativeModel("gemini-1.5-flash")

# Step 5.1: Open a CSV file to save output
csv_output_path = "results/sentiment_scores.csv"
os.makedirs("results", exist_ok=True)

csv_file = open(csv_output_path, mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write header row
csv_writer.writerow(["Review", "Expected", "Predicted", "Score"])


# Step 6: Loop through reviews and calculate individual scores
total_score = 0

for i, (review_text, expected_label) in enumerate(review_data, start=1):
    final_prompt = prompt_template.format(REVIEW=review_text)
    print(f"\n--- Review {i} ---")
    print("Input:", review_text)

    response = model.generate_content(final_prompt)
    output = response.text.strip()
    print("Sentiment:", output)

    score = 1 if output.lower() == expected_label.lower() else 0
    print("Expected:", expected_label)
    print("Score:", score)
    
    csv_writer.writerow([review_text, expected_label, output, score])

    
    total_score += score

csv_file.close()
print(f"\n📁 Results saved to: {csv_output_path}")


# Step 7: Final accuracy
total_reviews = len(review_data)
accuracy_percent = (total_score / total_reviews) * 100
print(f"\n✅ Total Score: {total_score}/{total_reviews}")
print(f"✅ Accuracy: {accuracy_percent:.2f}%")


    
  



