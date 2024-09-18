import PyPDF2
import pandas as pd
import re

def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def parse_text_to_table(text):
    # Split the text into lines
    lines = text.strip().split('\n')
    
    # Assume the first line contains column names
    headers = lines[0].split()
    
    # Parse the rest of the lines into data
    data = []
    for line in lines[1:]:
        # Use regex to split the line, handling potential spaces in data
        row = re.findall(r'\S+(?:\s+\S+)*', line)
        if len(row) == len(headers):
            data.append(row)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)
    return df

def pdf_to_table(pdf_path):
    text = extract_data_from_pdf(pdf_path)
    table = parse_text_to_table(text)
    return table

# Example usage
pdf_file_path = 'C:/Users/jjmed/OneDrive/Documentos/Courses/Python Z to H/Complete-Python-3-Bootcamp/999-Tests/example_table.pdf'
result_table = pdf_to_table(pdf_file_path)

# Display the first few rows of the table
print(result_table.head())

# Optionally, save the table to a CSV file
result_table.to_csv('output_table.csv', index=False)
