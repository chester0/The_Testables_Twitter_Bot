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
import getopt


def main(argv):
    timezone = ''
    start_date = ''
    end_date = ''
    twitter_id = ''

    # check arguments
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    if len(sys.argv) != 9:
        print('wrong number of arguments. Usage: main.py -t <TIMEZONE> -a <START_DATE> -b <END_DATE> -i <TWITTER_ID')
        sys.exit()

    try:
        opts, args = getopt.getopt(argv, ":t:a:b:i", ["TIMEZONE=", "START_DATE=", "END_DATE", "ID"])
    except getopt.GetoptError:
        print('get opt error')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-t", "--t timezone"):
            timezone = arg
        elif opt in ("-a", "--a start_date"):
            start_date = arg
        elif opt in ("-b", "--b end_date"):
            end_date = arg
        elif opt in ("-a", "--a start_date"):
            start_date = arg

    print('Timezone:', timezone)
    print('Start date:', start_date)
    print('End date:', end_date)
    print('Twitter ID:', twitter_id)

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

# check arguments
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))


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
