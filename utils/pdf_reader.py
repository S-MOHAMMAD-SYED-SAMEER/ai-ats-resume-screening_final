import pdfplumber
import docx

def read_resume(file):

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