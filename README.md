# Prompt Engineering Playground with Gemini

This project explores how different types of prompts affect the quality of LLM responses using Google Gemini.

We used Gemini 1.5 Flash to generate and evaluate outputs from:
- Direct Prompts
- Role-Based Prompts
- Chain-of-Thought (CoT) Prompts

Each output was automatically scored by Gemini itself on:
- Clarity (1–5)
- Helpfulness (1–5)
- Tone (1–5)

---

## Project Goals

- Compare multiple prompt styles using real-world examples.
- Automate evaluation scoring with LLMs.
- Build a reusable playground for testing prompt engineering ideas.

---

##  Project Structure
prompt-playground/
│
├── .venv/ ← Python virtual environment
├── .gitignore
├── README.md
├── requirements.txt
│
├── notebooks/ ← Jupyter notebooks
│ └── prompt_playground.ipynb
│
├── prompts/ ← All prompt templates
│ ├── cot.txt
│ ├── direct.txt
│ ├── few_shot.txt
│ ├── role_based.txt
│ ├── scorer.txt
│ └── sentiment_template.txt
│
├── scripts/ ← Python scripts for app logic
│ ├── generate_and_score.py
│ └── generate_from_template.py
└── .env ← API keys (not pushed to GitHub)


---

##  Key Learnings

- Prompt formatting directly affects clarity and relevance of LLM output.
- Chain-of-Thought prompts often outperform others in clarity.
- Evaluation can be automated using LLMs for structured feedback.
- This method can power real-world GenAI tools like chatbots, reviewers, and assistants.

---

##  How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/RaghuramReddy9/prompt-playground.git
cd prompt-playground

# 2. Set up a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key to a .env file
GOOGLE_API_KEY=your_key_here

# 5. Run the script
python scripts/generate_and_score.py


### Multi-Prompt Response Examples  
![Prompt Outputs](screenshots/prompt_outputs.png)

### Gemini Evaluation Scores  
![Evaluation Results](screenshots/scoring.png)



