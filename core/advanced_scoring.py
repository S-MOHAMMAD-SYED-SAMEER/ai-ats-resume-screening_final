import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load AI model (optimized)
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')


# -----------------------------
# SKILL EXTRACTION
# -----------------------------
def extract_skills(text):

    skills_db = [
        "python","sql","machine learning","deep learning","ai",
        "data analysis","excel","power bi","tableau",
        "aws","docker","kubernetes","pandas","numpy",
        "scikit-learn","tensorflow","pytorch",
        "nlp","data science","statistics"
    ]

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found


def skill_match_score(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    if len(jd_skills) == 0:
        return 50

    matched = len(set(resume_skills) & set(jd_skills))

    return (matched / len(jd_skills)) * 100


# -----------------------------
# EXPERIENCE DETECTION
# -----------------------------
from datetime import datetime
import re


months = {
    "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,
    "jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12
}


def month_to_num(m):
    return months.get(m.lower(),1)


def extract_experience_years(text):

    text = text.lower()

    total_months = 0

    # Detect month-year ranges first
    pattern = r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s*(\d{4})\s*(?:-|–|—|to)\s*(present|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s*(\d{4}))'

    matches = re.findall(pattern, text)

    for m in matches:

        start_month = month_to_num(m[0])
        start_year = int(m[1])

        if m[2] == "present":
            end = datetime.now()
        else:
            end_month = month_to_num(m[3])
            end_year = int(m[4])
            end = datetime(end_year, end_month, 1)

        start = datetime(start_year, start_month, 1)

        months_diff = (end.year - start.year) * 12 + (end.month - start.month)

        total_months += months_diff


    years = total_months / 12

    return round(years, 2)

def experience_score(resume_text, job_description):

    candidate_exp = extract_experience_years(resume_text)

    job_description = job_description.lower()

    match = re.findall(r'(\d+)\+?\s*(?:years|yrs)', job_description)

    required_exp = int(match[0]) if match else 0


    # detect fresher jobs
    fresher_keywords = [
        "fresher",
        "entry level",
        "graduate",
        "0-1 year",
        "0-2 years",
        "junior"
    ]

    if any(word in job_description for word in fresher_keywords):
        required_exp = 0


    if required_exp == 0:

        if candidate_exp == 0:
            return 80
        elif candidate_exp < 1:
            return 85
        else:
            return 100


    score = min(candidate_exp/required_exp,1)

    return score*100
# -----------------------------
# EDUCATION MATCH
# -----------------------------
def education_score(resume_text):

    text = resume_text.lower()

    if "phd" in text:
        return 100

    if "master" in text:
        return 90

    if "bachelor" in text:
        return 80

    return 50


# -----------------------------
# RESUME SECTION DETECTION
# -----------------------------
def section_score(text):

    sections = [
        "skills",
        "experience",
        "education",
        "projects",
        "summary"
    ]

    score = 0

    for s in sections:

        if s in text.lower():
            score += 20

    return score


# -----------------------------
# KEYWORD SIMILARITY
# -----------------------------
def keyword_similarity(resume_text, job_description):

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors[0], vectors[1])

    return float(similarity[0][0]) * 100


# -----------------------------
# SEMANTIC AI MATCHING
# -----------------------------
def semantic_similarity(resume_text, job_description):

    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2)

    return float(score[0][0]) * 100


# -----------------------------
# FINAL ATS SCORE
# -----------------------------
def calculate_ats_score(resume_text, job_description):

    skill = skill_match_score(resume_text, job_description)

    exp = experience_score(resume_text, job_description)

    edu = education_score(resume_text)

    keyword = keyword_similarity(resume_text, job_description)

    section = section_score(resume_text)

    semantic = semantic_similarity(resume_text, job_description)

    final_score = (
        skill * 0.35 +
        exp * 0.20 +
        edu * 0.10 +
        keyword * 0.15 +
        section * 0.10 +
        semantic * 0.10
    )

    return round(final_score, 2)