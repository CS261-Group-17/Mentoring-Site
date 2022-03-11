import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Install VADER sentiment analyser model if does not exist
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')


class SentimentAnalyser:
    sia = SentimentIntensityAnalyzer()

    @staticmethod
    def analyse_both(positive_feedback, negative_feedback):
        """Performs sentiment analysis on the positive and negative feedback"""
        positive_sentiment = (
            SentimentAnalyser.sia.polarity_scores(
                positive_feedback)["compound"]
            * (1 + len(positive_feedback) / 500)
        )
        negative_sentiment = (
            SentimentAnalyser.sia.polarity_scores(
                negative_feedback)["compound"]
            * (1 + len(negative_feedback) / 500)
        )
        return positive_sentiment + abs(negative_sentiment)

    @staticmethod
    def analyse(feedback):
        """Performs sentiment analysis on the feedback"""
        return SentimentAnalyser.sia.polarity_scores(feedback)["compound"]
