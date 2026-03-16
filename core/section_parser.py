import re

def extract_skills_section(text):

    pattern = r"(skills|technical skills)(.*?)(experience|education|projects|$)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(2)

    return ""


def extract_education_section(text):

    pattern = r"(education)(.*?)(experience|projects|skills|$)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(2)

    return ""


def extract_experience_section(text):

    pattern = r"(experience|work experience|internship)(.*?)(education|skills|projects|$)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(2)

    return ""