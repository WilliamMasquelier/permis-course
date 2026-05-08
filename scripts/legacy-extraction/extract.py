import pdfplumber
import sys

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                print(f"--- Page {page.page_number} ---")
                print(text)

print("Extracting 2-regle_de_barre-RECTO.pdf")
extract_text("raw/course-2/2-regle_de_barre-RECTO.pdf")
print("Extracting 2-regle_de_barre-VERSO.pdf")
extract_text("raw/course-2/2-regle_de_barre-VERSO.pdf")
