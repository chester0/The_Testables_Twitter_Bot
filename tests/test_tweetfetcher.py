import unittest
from unittest.mock import patch
from datetime import datetime
from src.timezone import TimeZoneConverter
from src.tweetfetcher import TweetFetcher


class MockTweet:
    def __init__(self, user_id, created_at):
        self.id = user_id
        self.created_at = created_at


class TestTweetFetcher(unittest.TestCase):

    def test_date_exceptions(self):
        # Should only accept dates for start_date and end_date
        with self.assertRaises(TypeError):
            TweetFetcher(None, "", "2017-01-02", None, None)

        with self.assertRaises(TypeError):
            TweetFetcher(None, "", datetime(2017, 1, 1), "2017-01-02", None)

    def test_add_tweet_on_boundary_values(self):
        tz = TimeZoneConverter("+00:00")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(None, "", start, end, tz)

        upper = MockTweet(0, start)
        lower = MockTweet(1, end)

        self.assertEqual(t.add_tweet(upper), 0)
        self.assertEqual(t.add_tweet(lower), 0)

        self.assertEqual(len(t.tweets), 2)
        self.assertTrue(upper in t.tweets)
        self.assertTrue(lower in t.tweets)

    def test_add_tweet_with_UTC_timezone(self):
        tz = TimeZoneConverter("+00:00")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(None, "", start, end, tz)

        # The tweets
        before = MockTweet(0, datetime(2017, 1, 1))  # Should return -1
        between = MockTweet(1, datetime(2017, 1, 2, 12))  # Should return 0
        after = MockTweet(2, datetime(2017, 1, 4))  # Should return 1

        self.assertEqual(t.add_tweet(before), -1)
        self.assertEqual(t.add_tweet(between), 0)
        self.assertEqual(t.add_tweet(after), 1)

        # It should have added the between tweet
        self.assertEqual(len(t.tweets), 1)
        self.assertTrue(between in t.tweets)

    def test_add_tweet_with_positive_timezone(self):
        tz = TimeZoneConverter("+01:30")
        start = datetime(2017, 1, 2)  # Local to the timezone
        end = datetime(2017, 1, 3)  # Local to the timezone
        t = TweetFetcher(None, "", start, end, tz)

        # The tweets
        before = MockTweet(0, datetime(2017, 1, 1))  # Should return -1
        between = MockTweet(1, datetime(2017, 1, 1, 22, 30))  # Should return 0 as it adds to 2017, 1, 2 Local
        after = MockTweet(2, datetime(2017, 1, 3))  # Should return 1 as it goes past 2017, 1, 3 Local

        self.assertEqual(t.add_tweet(before), -1)
        self.assertEqual(t.add_tweet(between), 0)
        self.assertEqual(t.add_tweet(after), 1)

        # It should have added the between tweet
        self.assertEqual(len(t.tweets), 1)
        self.assertTrue(between in t.tweets)

    def test_add_tweet_with_negative_timezone(self):
        tz = TimeZoneConverter("-01:30")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(None, "", start, end, tz)

        # The tweets
        before = MockTweet(0, datetime(2017, 1, 2))  # Should return -1 as it is before 2017, 1, 2 Local
        between = MockTweet(1, datetime(2017, 1, 2, 1, 30))  # Should return 0
        after = MockTweet(2, datetime(2017, 1, 4))  # Should return 1

        self.assertEqual(t.add_tweet(before), -1)
        self.assertEqual(t.add_tweet(between), 0)
        self.assertEqual(t.add_tweet(after), 1)

        # It should have added the between tweet
        self.assertEqual(len(t.tweets), 1)
        self.assertTrue(between in t.tweets)

    @patch('tweepy.API')
    def test_fetch_resets_variables(self, mock_api):
        api = mock_api()
        api.user_timeline.return_value = []

        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(api, "id", start, end, None)

        # Check that local variables get reset
        t.tweets = [1, 2]
        t.current_page = 1

        t.fetch()
        self.assertEqual(len(t.tweets), 0)
        self.assertEqual(t.current_page, 0)

    @patch('tweepy.API')
    def test_fetch_api_returns_nothing(self, mock_api):
        api = mock_api()
        api.user_timeline.return_value = []

        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(api, "id", start, end, None)

        results = t.fetch()

        api.user_timeline.assert_called_with(id="id", max_id=None, page=0)
        self.assertTrue(len(results) == 0)

    @patch('tweepy.API')
    def test_fetch_api_returns_tweets(self, mock_api):

        before = MockTweet(0, datetime(2017, 1, 1))
        between = MockTweet(1, datetime(2017, 1, 2, 12))
        after = MockTweet(2, datetime(2017, 1, 4))

        api = mock_api()
        api.user_timeline.return_value = [after, between, before]

        tz = TimeZoneConverter("+00:00")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(api, "id", start, end, tz)

        # Only the between tweet should be returned
        results = t.fetch()
        self.assertEqual(len(results), 1)
        self.assertTrue(between in results)

    @patch('tweepy.API')
    def test_fetch_api_should_terminate_if_tweet_is_before_start_date(self, mock_api):

        before = MockTweet(0, datetime(2017, 1, 1))
        between = MockTweet(1, datetime(2017, 1, 2, 12))
        after = MockTweet(2, datetime(2017, 1, 4))

        api = mock_api()
        api.user_timeline.return_value = [before, between, after]

        tz = TimeZoneConverter("+00:00")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(api, "id", start, end, tz)

        # No tweets should be returned
        results = t.fetch()
        self.assertEqual(len(results), 0)

    @patch('tweepy.API')
    def test_fetch_api_recursively_fetches_tweets(self, mock_api):

        before = MockTweet(0, datetime(2017, 1, 1))
        between = MockTweet(1, datetime(2017, 1, 2, 12))
        after = MockTweet(2, datetime(2017, 1, 4))

        api = mock_api()
        api.user_timeline.side_effect = [[after], [between], [before]]

        tz = TimeZoneConverter("+00:00")
        start = datetime(2017, 1, 2)
        end = datetime(2017, 1, 3)
        t = TweetFetcher(api, "id", start, end, tz)

        # Only the between tweet should be returned
        results = t.fetch()
        self.assertEqual(len(results), 1)
        self.assertTrue(between in results)

        # Check that local variables have been updated accordingly and we called the appropriate amount of times
        self.assertEqual(t.current_page, 2)
        self.assertEqual(api.user_timeline.call_count, 3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTweetFetcher)
unittest.TextTestRunner(verbosity=2).run(suite)
