import pdfplumber
import re

def count_words_in_pdf(filepath, words_to_count):
    """
    Counts the occurrences of specific words in a PDF file.
    
    Args:
        filepath (str): Path to the PDF file.
        words_to_count (list): List of words to count.
        
    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    # initialise dictionary to store word counts
    word_counts = {word: 0 for word in words_to_count}
    
    # open  PDF and extract text
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # convert text to lowercase for case-insensitive matching
                text = text.lower()
                # count occurrences of each word
                for word in words_to_count:
                    word_counts[word] += len(re.findall(re.escape(word), text))
    
    return word_counts

if __name__ == "__main__":
    # example usage
    filepath = # replace with your PDF file path
    words_to_count = ["risk", "safe", "bias", "security", 
                      "accountab", "transparen", "explainab", "policy",
                      "compliance", "governance", "protect", "sustainab",
                      "fair", "catastroph", "responsib", "prepare"] 
    word_counts = count_words_in_pdf(filepath, words_to_count)
    
    # print the results
    for word, count in word_counts.items():
        print(f"{word}: {count}")