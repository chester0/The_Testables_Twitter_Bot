import unittest
import os.path
import sys
from unittest.mock import patch
from src.tweetsubmitter import TweetSubmitter
sys.path.append("..")


class TestTweetSubmitter(unittest.TestCase):

    def test_graph_building(self):
        t = TweetSubmitter(None, "Me", "abc", "def", {0: 1, 1: 2, 2: 3})

        # Check that we correctly parse the x axis values
        for key in range(3):
            self.assertTrue(key in t.x)

        # Check that we correctly parse the frequency values to the y axis
        for value in [1, 2, 3]:
            self.assertTrue(value in t.y)

        # Check if the graph was made
        self.assertTrue(os.path.exists('graph.png'))

    @patch('tweepy.API')
    def test_submitting(self, MockAPI):
        api = MockAPI()
        api.update_with_media.return_value = []

        t = TweetSubmitter(api, "Me", "abc", "def", {0: 1, 1: 2, 2: 3}).submit()

        api.update_with_media.assert_called_with('graph.png')

suite = unittest.TestLoader().loadTestsFromTestCase(TestTweetSubmitter)
unittest.TextTestRunner(verbosity=2).run(suite)
