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

PROJECT_KEYWORDS = [
    "project",
    "projects",
    "mindbridge",
    "customer segmentation",
    "resume parser",
    "attendance system",
    "juno"
]


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 3:
            return line

    return "Not Found"


def extract_email(text):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r'(\+91[- ]?)?[6-9]\d{9}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_github(text):

    pattern = r'github\.com/[A-Za-z0-9_-]+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_linkedin(text):

    pattern = r'linkedin\.com/in/[A-Za-z0-9_-]+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_skills(text):

    detected = []

    text_lower = text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in text_lower:
            detected.append(skill)

    return detected


def extract_projects(text):

    projects = []

    text_lower = text.lower()

    for project in PROJECT_KEYWORDS:

        if project.lower() in text_lower:
            projects.append(project.title())

    return projects


def calculate_score(data):

    score = 0

    if data["email"] != "Not Found":
        score += 10

    if data["phone"] != "Not Found":
        score += 10

    if data["github"] != "Not Found":
        score += 15

    if data["linkedin"] != "Not Found":
        score += 15

    score += min(len(data["skills"]) * 3, 25)

    score += min(len(data["projects"]) * 5, 25)

    return min(score, 100)


def analyze_resume(text):

    data = {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "github": extract_github(text),

        "linkedin": extract_linkedin(text),

        "skills": extract_skills(text),

        "projects": extract_projects(text)

    }

    data["score"] = calculate_score(data)

    return data