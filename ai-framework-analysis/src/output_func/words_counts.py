import pdfplumber
import re
import os
import csv

def count_words_in_pdf(filepath, words_to_count):
    word_counts = {word: 0 for word in words_to_count}
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text = text.lower()
                for word in words_to_count:
                    word_counts[word] += len(re.findall(re.escape(word), text))
    return word_counts

def process_word_counts(input_folder, output_csv, words_to_count):
    with open(output_csv, 'w', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename'] + words_to_count)  # header 
        
        for filename in os.listdir(input_folder):
            if filename.endswith('.pdf'):
                filepath = os.path.join(input_folder, filename)
                word_counts = count_words_in_pdf(filepath, words_to_count)
                row = [filename.replace('.pdf', '')] + [word_counts[word] for word in words_to_count]
                writer.writerow(row)

if __name__ == "__main__":
    input_folder = # enter input folder path
    output_csv = # enter output folder path
    words_to_count = ["risk", "safe", "bias", "security", 'ethic',
                      "accountab", "transparen", "explainab", "policy",
                      "compliance", "governance", "protect", "sustainab",
                      "fair", "catastroph", "responsib", "prepare"]  
    process_word_counts(input_folder, output_csv, words_to_count)
    print(f"Word counts have been written to {output_csv}")