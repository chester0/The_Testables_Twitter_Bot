#!/usr/bin/python3
#
# FIT4004 Assignment 3
# analyses tweets made by an individual, produces a graph showing
# frequency of tweeting at particular times of the day, and
# posts the graph as a tweet
#
# Authors:
# Demetrios Christou
# Mikunj Varsani
#
#
# should run from the command line and take the following command-line arguments:
#
# -t TIMEZONE : the timezone of the tweeter for analysis purposes. TIMEZONE should be
# represented as +/- HH:MM (that is, if a tweet occurred at 13:45 UTC, and their timezone was
# +10:00, the tweet is regarded as having occurred at 23:45). The default is UTC.
#
# -a DATE : the date (in local time as specified by the -t argument, if present) to begin analysis
# from. Specified as YYYY-MM-DD.
#
# -b DATE : the last date (in local time as specified by the -t argument, if present) to analyse.
# Specified as YYYY-MM-DD.
#
# -i ID : The id of the tweeter to analyse. ID should start with the @ sign.
# The graph should be a simple line graph showing the time of day on the X-Axis and the average
# number of tweets per hour on the Y-Axis.
#
# Twitter account used: @The_Testables_Bot
#
import tweepy
import sys
from tweetfetcher import TweetFetcher
from tweetanalyser import TweetAnalyser
from timezone import TimeZoneConverter
from tweetsubmitter import TweetSubmitter
from arg_parser import ArgParser
from datetime import datetime

consumer_key = 'nQr62OZwOWTK5WxGFFwNgo8Ir'
consumer_secret = '768VVh1exJAvMXEMIAlSx9Sk84EKI1hG6cOC83zELZPnOCQjXN'
access_token = '864747008111788033-eFZKCN7HYr3CxiEyZXNEtbCSmIVjc1V'
access_token_secret = 'mv7WAAFZ1MHIQX22zl8q8YVw138GuGXDuqO5yu7LDO4cr'


def main(argv):
    try:
        args = ArgParser(argv)

        # authenticate
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(args.end_date, '%Y-%m-%d')

        converter = TimeZoneConverter(args.timezone)
        fetcher = TweetFetcher(api, args.twitter_id, start_date, end_date, converter)

        print("Fetching Tweets")
        tweets = fetcher.fetch()

        print("Analysing and Building Graph")
        frequencies = TweetAnalyser(tweets, converter).get_frequencies()
        submitter = TweetSubmitter(api, args.twitter_id, args.start_date, args.end_date, frequencies)

        print("Tweeting")
        submitter.submit()

        print("Finished!!")
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":
    main(sys.argv[1:])
