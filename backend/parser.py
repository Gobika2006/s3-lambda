import io
import PyPDF2

def extract_text(file_content):
    pdf = PyPDF2.PdfReader(io.BytesIO(file_content))
    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    return text.lower()
