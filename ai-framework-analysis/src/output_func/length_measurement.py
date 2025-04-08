import pdfplumber
import os
import csv

def count_words_in_pdf(filepath):
    """
    Counts the total number of words in a PDF file.
    
    Args:
        filepath (str): Path to the PDF file.
        
    Returns:
        int: The total number of words in the PDF.
    """
    total_words = 0
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                words = text.split()
                total_words += len(words)
    return total_words

def process_length_measurement(input_folder, output_csv):
    """
    Processes all PDF files in the input folder and writes the filename/word count to a CSV file.
    
    Args:
        input_folder (str): Path to the folder containing PDF files.
        output_csv (str): Path to the output CSV file.
    """
    with open(output_csv, 'w', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Length'])  # header
        
        for filename in os.listdir(input_folder):
            if filename.endswith('.pdf'):
                filepath = os.path.join(input_folder, filename)
                word_count = count_words_in_pdf(filepath)
                writer.writerow([filename.replace('.pdf', ''), word_count])

if __name__ == "__main__":
    input_folder = # enter input folder path
    output_csv = # enter output folder path
    process_length_measurement(input_folder, output_csv)
    print(f"Length results have been written to {output_csv}")