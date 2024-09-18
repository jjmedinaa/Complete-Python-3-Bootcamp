import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_csv):
    # Read PDF file
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    # Combine all tables into a single DataFrame
    combined_df = pd.concat(tables, ignore_index=True)
    
    # Save the combined DataFrame to a CSV file
    combined_df.to_csv(output_csv, index=False)
    print(f"Tables extracted and saved to {output_csv}")

# Example usage
pdf_file = 'C:/Users/jjmed/OneDrive/Documentos/Courses/Python Z to H/Complete-Python-3-Bootcamp/999-Tests/example_table.pdf'
output_file = 'extracted_tables.csv'
extract_tables_from_pdf(pdf_file, output_file)
