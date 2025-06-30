# Prompt Engineering Playground with Gemini

This project explores how different types of prompts affect the quality of LLM responses using Google Gemini.

We used Gemini 1.5 Flash to generate and evaluate outputs from:
- Direct Prompts
- Role-Based Prompts
- Chain-of-Thought (CoT) Prompts
- LangChain PromptTemplate-based Sentiment Classification

Each output was optionally scored by:
- Gemini itself (self-evaluation)
- Manual scoring logic (1 = correct, 0 = incorrect)

---

## Project Goals

- Compare multiple prompt styles using real-world examples.
- Automate evaluation scoring with LLMs.
- Build a reusable playground for testing prompt engineering ideas.
- Test prompt templates with LangChain and analyze response accuracy.

---

## 📁 Project Structure
prompt-playground/
│
├── .venv/ ← Python virtual environment
├── .gitignore
├── README.md
├── requirements.txt
│
├── notebooks/
│ └── prompt_playground.ipynb
│
├── prompts/
│ ├── cot.txt
│ ├── direct.txt
│ ├── few_shot.txt
│ ├── role_based.txt
│ ├── scorer.txt
│ └── sentiment_template.txt 
│
├── results/
│ └── sentiment_scores.csv 
│
├── scripts/
│ ├── generate_and_score.py
│ └── generate_from_template.py 
│
├── screenshots/
│ ├── prompt_outputs.png
│ └── scoring.png
│
└── .env ← API keys (not pushed to GitHub)

---


## 📸 Screenshots

### 🖼️ Prompt Outputs Example  
![Prompt Outputs](screenshots/prompt_outputs.png)

### 📊 Scoring Table  
![Scoring Output](screenshots/scoring.png)


---


## 🆕 New Module: Sentiment Classification with LangChain + Gemini

This script demonstrates how to:
- Use `LangChain.PromptTemplate` to fill a structured prompt
- Send the review to Gemini Flash (1.5)
- Get predicted sentiment (Positive/Negative)
- Compare it to expected label
- Score accuracy (1 = correct, 0 = incorrect)
- Save all outputs to `sentiment_scores.csv`

---

### 🧪 Example Output

```markdown
```text
--- Review 1 ---
Input: The movie was fantastic and had great acting.
Sentiment: Positive
Expected: Positive
Score: 1

✅ Total Score: 3/3
✅ Accuracy: 100.00%

| Review                                             | Expected | Predicted | Score |
| -------------------------------------------------- | -------- | --------- | ----- |
| The movie was fantastic and had great acting.      | Positive | Positive  | 1     |
| It was boring and I almost fell asleep.            | Negative | Negative  | 1     |
| The visuals were good, but the plot made no sense. | Negative | Negative  | 1     |


# Set up project as usual...
# Run the sentiment classification scoring script
python scripts/generate_from_template.py

----
