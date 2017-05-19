import unittest
from unittest.mock import patch, Mock

from datetime import datetime,timedelta
import sys
sys.path.append("..")

from src.timezone import TimeZoneConverter
from src.tweetanalyser import TweetAnalyser

class MockTweet():
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at

class TestTweetAnalyser(unittest.TestCase):

    def test_frequencies_should_be_set_to_zero(self):
        tz = TimeZoneConverter("+00:00")
        t = TweetAnalyser([], tz)
        frequencies = t.getFrequecies()

        #Must be 24 values, as there are 24 hours in a day
        self.assertEqual(len(frequencies), 24)

        #Since no tweets were parsed then the frequencies should be 0
        for key, value in frequencies.items():
            self.assertEqual(value, 0)

    def test_frequency_with_UTC_timezone(self):
        t1 = MockTweet(0, datetime(2017, 1, 1, 1))
        t2 = MockTweet(0, datetime(2017, 1, 1, 1))
        t3 = MockTweet(0, datetime(2017, 1, 1, 2))

        tz = TimeZoneConverter("+00:00")
        t = TweetAnalyser([t1, t2, t3], tz)
        frequencies = t.getFrequecies()

        #There should be 2 tweets at 1 and 1 tweet at 2
        for key, value in frequencies.items():
            if key == 1:
                self.assertEqual(value, 2)
            elif key == 2:
                self.assertEqual(value, 1)
            else:
                self.assertEqual(value, 0)

    def test_frequency_with_other_timezone(self):
        t1 = MockTweet(0, datetime(2017, 1, 1, 0))
        t2 = MockTweet(0, datetime(2017, 1, 1, 0))
        t3 = MockTweet(0, datetime(2017, 1, 1, 1))

        tz = TimeZoneConverter("-01:00")
        t = TweetAnalyser([t1, t2, t3], tz)
        frequencies = t.getFrequecies()

        #There should be 2 tweets at 23 and 1 tweet at 0 (-1 to utc)
        for key, value in frequencies.items():
            if key == 23:
                self.assertEqual(value, 2)
            elif key == 0:
                self.assertEqual(value, 1)
            else:
                self.assertEqual(value, 0)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTweetAnalyser)
unittest.TextTestRunner(verbosity=2).run(suite)
