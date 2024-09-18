import PyPDF2
import re

def find_word_in_pdf(pdf_path, search_word):
    word_found = False
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            # Using regex to find whole words only
            matches = re.finditer(r'\b' + re.escape(search_word) + r'\b', text, re.IGNORECASE)
            for match in matches:
                word_found = True
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end].replace('\n', ' ')
                print(f"Found on page {page_num}:")
                print(f"...{context}...")
                print()
    
    if not word_found:
        print(f"The word '{search_word}' was not found in the document.")

# Example usage
pdf_file_path = 'C:/Users/jjmed/OneDrive/Documentos/Courses/Python Z to H/Complete-Python-3-Bootcamp/999-Tests/NFL23_CS_PPR.pdf'
word_to_find = 'Justin'

find_word_in_pdf(pdf_file_path, word_to_find)
