import pdfplumber
import docx
import re


def extract_text(file):

    text = ""

    if file.type == "application/pdf":

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                content = page.extract_text()

                if content:
                    text += content

    else:

        doc = docx.Document(file)

        for p in doc.paragraphs:
            text += p.text

    return text.lower()


def extract_email(text):

    email = re.findall(r'\S+@\S+', text)

    return email[0] if email else "Not detected"


def extract_phone(text):

    phone = re.findall(r'\+?\d[\d\s\-]{8,15}', text)

    return phone[0] if phone else "Not detected"


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:5]:

        if len(line.split()) >= 2:
            return line.title()

    return "Not detected"


def extract_experience(text):

    exp = re.findall(r'\d+\+?\s*years?', text)

    return exp[0] if exp else "Not detected"