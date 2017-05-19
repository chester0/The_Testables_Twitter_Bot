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

import tweepy
import sys
from tweetfetcher import TweetFetcher
from timezone import TimeZoneConverter
from arg_parser import ArgParser
from datetime import datetime


def main(argv):

    ArgParser(argv)

if __name__ == "__main__":
    main(sys.argv[1:])


consumer_key = 'nQr62OZwOWTK5WxGFFwNgo8Ir'
consumer_secret = '768VVh1exJAvMXEMIAlSx9Sk84EKI1hG6cOC83zELZPnOCQjXN'
access_token = '864747008111788033-eFZKCN7HYr3CxiEyZXNEtbCSmIVjc1V'
access_token_secret = 'mv7WAAFZ1MHIQX22zl8q8YVw138GuGXDuqO5yu7LDO4cr'

# authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# testing twitter connection
public_tweets = api.home_timeline()
# for tweet in public_tweets:
#    print(tweet.text)


# sample code
user = api.get_user('realDonaldTrump')
print("Name:", user.name)
print("Location:", user.location)
print("Following:", user.friends_count)
print("Followers:", user.followers_count)

tz = TimeZoneConverter("+00:00")
t = TweetFetcher(api, 'realDonaldTrump', datetime(2017, 4, 1), datetime(2017, 5, 17), tz)
statuses = t.fetch()
print("page:" + str(t.current_page))
print("count:" + str(len(statuses)))
