import pdfplumber

def count_words_in_pdf(filepath):
    """
    Counts the total number of words in a PDF file.
    
    Args:
        filepath (str): Path to the PDF file.
        
    Returns:
        int: The total number of words in the PDF.
    """
    total_words = 0
    
    # open PDF and extract text
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # split text into words + count them
                words = text.split()
                total_words += len(words)
    
    return total_words

if __name__ == "__main__":
    # example usage
    filepath = # replace with PDF file path
    total_words = count_words_in_pdf(filepath)
    
    print(f"Total number of words in the PDF: {total_words}")
