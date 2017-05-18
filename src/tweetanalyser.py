from datetime import date, datetime

class TweetAnalyser():
    def __init__(self, tweets, converter):
        self.tweets = tweets
        self.converter = converter

    def getFrequecies(self):
        frequencies = {}

        #Initialise the frequencies to 0
        for i in range(24):
            frequencies[i] = 0

        #Go through the tweets and update the frequencies
        for tweet in self.tweets:
            tz_date = self.converter.convert(tweet.created_at)
            frequencies[tz_date.hour] += 1

        return frequencies
