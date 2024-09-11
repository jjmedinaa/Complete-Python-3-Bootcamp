import PyPDF2
import re
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

def find_word_in_pdf_text(pdf_path, search_word):
    word_found = False
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            matches = re.finditer(r'\b' + re.escape(search_word) + r'\b', text, re.IGNORECASE)
            for match in matches:
                word_found = True
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end].replace('\n', ' ')
                print(f"Found in text on page {page_num}:")
                print(f"...{context}...")
                print()
    return word_found

def find_word_in_pdf_images(pdf_path, search_word):
    word_found = False
    images = convert_from_path(pdf_path, poppler_path=r'C:\Users\jjmed\OneDrive\Documentos\Courses\Python Z to H\Release-24.07.0-0\poppler-24.07.0\Library\bin')
    for i, image in enumerate(images, start=1):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jjmed\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(image)
        matches = re.finditer(r'\b' + re.escape(search_word) + r'\b', text, re.IGNORECASE)
        for match in matches:
            word_found = True
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            context = text[start:end].replace('\n', ' ')
            print(f"Found in image on page {i}:")
            print(f"...{context}...")
            print()
    return word_found

def find_word_in_pdf(pdf_path, search_word):
    print(f"Searching for '{search_word}' in {pdf_path}")
    print("Searching in text layer...")
    found_in_text = find_word_in_pdf_text(pdf_path, search_word)
    
    print("Searching in images (this may take a while)...")
    found_in_images = find_word_in_pdf_images(pdf_path, search_word)
    
    if not (found_in_text or found_in_images):
        print(f"The word '{search_word}' was not found in the document.")

# Example usage
pdf_file_path = 'C:/Users/jjmed/OneDrive/Documentos/Courses/Python Z to H/Complete-Python-3-Bootcamp/111-Tests/NFL23_CS_PPR.pdf'
word_to_find = 'Quarterbacks'

find_word_in_pdf(pdf_file_path, word_to_find)
