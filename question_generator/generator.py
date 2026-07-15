import os
from openai import OpenAI

# =========================
# RULE BASED QUESTION BANK
# =========================

QUESTION_BANK = {

    "Python": [
        "Explain Python decorators.",
        "What are Python lists and tuples?",
        "Explain *args and **kwargs."
    ],

    "JavaScript": [
        "Explain closures in JavaScript.",
        "Difference between var, let and const?",
        "Explain event bubbling."
    ],

    "HTML": [
        "What is semantic HTML?",
        "Difference between div and span?"
    ],

    "CSS": [
        "What is Flexbox?",
        "Difference between Grid and Flexbox?"
    ],

    "Docker": [
        "What is Docker?",
        "Difference between containers and virtual machines?",
        "What are Docker volumes?"
    ],

    "Git": [
        "Explain Git branching.",
        "Difference between merge and rebase?",
        "What is Git stash?"
    ],

    "Flask": [
        "What is Flask?",
        "Explain routing in Flask.",
        "How does request handling work?"
    ],

    "React": [
        "What is the Virtual DOM?",
        "Explain React hooks."
    ],

    "Machine Learning": [
        "What is overfitting?",
        "Explain bias vs variance.",
        "Difference between supervised and unsupervised learning?"
    ]
}


PROJECT_QUESTIONS = {

    "Mindbridge": [
        "Explain the architecture of MindBridge.",
        "What challenges did you face while building MindBridge?"
    ],

    "Customer Segmentation": [
        "Which clustering algorithm did you use?",
        "How did you evaluate cluster quality?"
    ],

    "Resume Parser": [
        "How does your resume parser work?",
        "What NLP techniques were used?"
    ]
}


# =========================
# RULE BASED GENERATOR
# =========================

def generate_questions(analysis):

    questions = []

    for skill in analysis.get("skills", []):

        if skill in QUESTION_BANK:
            questions.extend(
                QUESTION_BANK[skill][:1]
            )

    for project in analysis.get("projects", []):

        if project in PROJECT_QUESTIONS:
            questions.extend(
                PROJECT_QUESTIONS[project][:1]
            )

    return questions[:10]


# =========================
# AI QUESTION GENERATOR
# =========================

def generate_ai_questions(
    extracted_text,
    skills,
    projects
):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return [
            "OpenAI API key not found.",
            "Set OPENAI_API_KEY to use AI questions."
        ]

    client = OpenAI(
        api_key=api_key
    )

    prompt = f"""
You are a senior software engineering interviewer.

Analyze this resume:

{extracted_text}

Detected Skills:
{', '.join(skills)}

Detected Projects:
{', '.join(projects)}

Generate:

1. Three technical questions
2. Two project-specific questions
3. One behavioral question

Return only the questions.
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    content = response.choices[0].message.content

    return content.split("\n")