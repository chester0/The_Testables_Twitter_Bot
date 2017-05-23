from datetime import date, datetime

# Analyse an array of tweets and construct a frequency dictionary from them
class TweetAnalyser:
    def __init__(self, tweets, converter):
        self.tweets = tweets
        self.converter = converter

    def getFrequencies(self):
        frequencies = {}

        # Initialise the frequencies to 0
        for i in range(24):
            frequencies[i] = 0

        # Go through the tweets and update the frequencies
        for tweet in self.tweets:
            tz_date = self.converter.convert(tweet.created_at)
            frequencies[tz_date.hour] += 1

        return frequencies
