import tweepy
from datetime import date, datetime


# A Class which fetches tweets of the given user from start_date to end_date
class TweetFetcher():

    def __init__(self, api, id, start_date, end_date, converter):

        # Make sure start and end dates are date objects and not strings
        if not isinstance(start_date, date):
            raise TypeError("Start Date must be a date object")
        if not isinstance(end_date, date):
            raise TypeError("End Date must be a date object")

        self.api = api
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.converter = converter

        # Local variables needed to track the tweets
        self.last_tweet_id = None
        self.tweets = []
        self.current_page = 0

    # Add a tweet if it was posted between start_date and end_date
    # Returns 0 if success, -1 if tweet was posted before start_date and 1 if tweet was posted after end_date
    def _addTweet(self, tweet):
        # Convert the utc to timezone that was set
        utc_date = tweet.created_at
        tz_date = self.converter.convert(utc_date)

        # Check if date was before the start date
        if tz_date < self.start_date:
            return -1

        # Check if date was after the end date
        if tz_date > self.end_date:
            return 1

        # It's between start and end so we add it
        self.tweets.append(tweet)

        return 0

    # Fetch the tweets
    # Returns an array of tweets
    def fetch(self):
        if self.last_tweet_id is None:
            self.tweets = []
            self.current_page = 0

        # Get the statuses
        statuses = self.api.user_timeline(id=self.id, max_id=self.last_tweet_id, page=self.current_page)

        # Check if any tweets were returned
        if not statuses:
            self.last_tweet_id = None
            return self.tweets

        # Go through the tweets
        for status in statuses:
            # Check that we haven't gone past the start date
            # This is because tweets are returned from most recent first
            if self._addTweet(status) < 0:
                self.last_tweet_id = None
                return self.tweets

        # Keep fetching until we have enough data
        self.last_tweet_id = statuses[-1].id
        self.current_page += 1
        return self.fetch()
