import re

STOPWORDS = {
"the","and","with","for","from","this","that","have","will",
"using","used","skills","skill","work","working","experience"
}

def extract_keywords(text):

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    keywords = [w for w in words if w not in STOPWORDS and len(w) > 3]

    return list(set(keywords))