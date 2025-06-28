#  Prompt Playground with Gemini 1.5 Flash

This project explores how prompt phrasing impacts the output of Large Language Models.  
We compare **three core prompt styles** using Google's Gemini 1.5 Flash API.

## Prompt Types Tested:
- **Direct Prompt** – Ask a question plainly
- **Role-Based Prompt** – Set a persona or expert role
- **Chain-of-Thought Prompt** – Encourage step-by-step reasoning
**Few-Shot Prompting** – Teach Gemini with examples (e.g., Informal to Formal Text)

## Technologies Used:
- Google Generative AI (Gemini 1.5 Flash)
- Python 3.10+
- Jupyter Notebook
- Prompt files (.txt)


## Multi-Prompt Evaluation with Gemini (Prompt Scoring)

This experiment compares 3 types of prompts:

- **Direct Prompt**
- **Role-Based Prompt**
- **Chain-of-Thought Prompt (CoT)**

Each prompt was used to generate a response about the history of Artificial Intelligence (AI) using the Gemini API.  
We then used **Gemini itself to evaluate and score the responses** based on:

- Clarity (1 to 5)
- Helpfulness (1 to 5)
- Tone (1 to 5)

### Results:
- **Clarity:** Chain-of-Thought and Direct Prompts scored highest.
- **Helpfulness:** All prompts struggled to fully address the user's input.
- **Best Overall:** Chain-of-Thought (CoT) for structure, Direct for readability.

###  What I Learned:
- How to score prompt outputs using Gemini
- How to compare multiple prompt typesgit add .
git commit -m "Multi-Prompt Evaluation with Gemini - Prompt Scoring"
git push origin main

- How to automate evaluation in real-world GenAI workflows

> This method can be used in real apps to choose the best prompt for chatbots, summarizers, and assistants.


## How to Run:
1. Clone the repo:
   ```bash
   git clone https://github.com/RaghuramReddy9/prompt-playground.git
   cd prompt-playground

<pre> prompt-playground/ │ ├── .venv/ ← Python virtual environment ├── .gitignore ├── README.md ├── requirements.txt │ ├── notebooks/ ← Jupyter notebooks │ └── prompt_playground.ipynb │ ├── prompts/ ← All prompt templates │ ├── cot.txt │ ├── direct.txt │ ├── few_shot.txt ← ✅ renamed for consistency │ ├── role_based.txt │ ├── scorer.txt │ └── sentiment_template.txt │ ├── scripts/ ← Python scripts for app logic │ ├── generate_and_score.py │ └── generate_from_template.py └── .env ← API keys (not pushed to GitHub) </pre>