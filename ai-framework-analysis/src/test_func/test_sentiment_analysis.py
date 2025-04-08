import pdfplumber
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment_in_pdf(filepath):
    """
    Analyzes the sentiment of text in a PDF file and calculates the percentage of positive, negative, and neutral text.
    
    Args:
        filepath (str): Path to the PDF file.
        
    Returns:
        dict: A dictionary with percentages of positive, negative, and neutral sentiments.
    """
    # initialise the sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # initialise counters for sentiment scores
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    total_sentences = 0
    
    # open PDF and extract text
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # split text into sentences
                sentences = text.split('.')
                for sentence in sentences:
                    if sentence.strip():  # ignore empty sentences
                        total_sentences += 1
                        sentiment = sia.polarity_scores(sentence)
                        if sentiment['compound'] > 0.05:
                            positive_count += 1
                        elif sentiment['compound'] < -0.05:
                            negative_count += 1
                        else:
                            neutral_count += 1
    
    positive_percentage = (positive_count / total_sentences) * 100 if total_sentences > 0 else 0
    negative_percentage = (negative_count / total_sentences) * 100 if total_sentences > 0 else 0
    neutral_percentage = (neutral_count / total_sentences) * 100 if total_sentences > 0 else 0
    
    return {
        "positive": positive_percentage,
        "negative": negative_percentage,
        "neutral": neutral_percentage
    }

if __name__ == "__main__":
    # example usage
    filepath = # Replace with PDF file path
    sentiment_results = analyze_sentiment_in_pdf(filepath)
    
    print("Sentiment Analysis Results:")
    print(f"Positive: {sentiment_results['positive']:.2f}%")
    print(f"Negative: {sentiment_results['negative']:.2f}%")
    print(f"Neutral: {sentiment_results['neutral']:.2f}%")
