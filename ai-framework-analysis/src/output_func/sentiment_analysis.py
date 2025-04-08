import pdfplumber
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os
import csv

nltk.download('vader_lexicon')

def analyze_sentiment_in_pdf(filepath):
    sia = SentimentIntensityAnalyzer()
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    total_sentences = 0
    
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                sentences = text.split('.')
                for sentence in sentences:
                    if sentence.strip():
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
    
    return positive_percentage, negative_percentage, neutral_percentage

def process_sentiment_analysis(input_folder, output_csv):
    with open(output_csv, 'w', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Positive', 'Negative', 'Neutral'])  # Header row
        
        for filename in os.listdir(input_folder):
            if filename.endswith('.pdf'):
                filepath = os.path.join(input_folder, filename)
                positive, negative, neutral = analyze_sentiment_in_pdf(filepath)
                writer.writerow([filename.replace('.pdf', ''), positive, negative, neutral])

if __name__ == "__main__":
    input_folder = # enter input folder path
    output_csv = # enter output folder path
    process_sentiment_analysis(input_folder, output_csv)
    print(f"Sentiment analysis results have been written to {output_csv}")