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
    
    # Open the PDF and extract text
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Split the text into words and count them
                words = text.split()
                total_words += len(words)
    
    return total_words

if __name__ == "__main__":
    # Example usage
    filepath = # replace with PDF file path
    total_words = count_words_in_pdf(filepath)
    
    # Print the result
    print(f"Total number of words in the PDF: {total_words}")