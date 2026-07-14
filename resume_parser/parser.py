import re

SKILLS_DATABASE = [
    "Python",
    "JavaScript",
    "HTML",
    "CSS",
    "Docker",
    "Git",
    "Flask",
    "React",
    "SQL",
    "Linux",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "C",
    "C++",
    "Java"
]


def extract_email(text):

    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(email_pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_skills(text):

    detected_skills = []

    text_lower = text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in text_lower:
            detected_skills.append(skill)

    return detected_skills


def analyze_resume(text):

    return {
        "email": extract_email(text),
        "skills": extract_skills(text)
    }