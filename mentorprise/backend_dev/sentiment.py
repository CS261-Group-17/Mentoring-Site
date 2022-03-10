import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Install VADER sentiment analyser model if does not exist
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')


class SentimentAnalyser:
    sia = SentimentIntensityAnalyzer()
    
    # Performs sentimental analysis on text passed and returns number from -1 to 1 
    # negative is < 0
    @staticmethod
    def analyse(text):
        return  SentimentAnalyser.sia.polarity_scores(text)["compound"]