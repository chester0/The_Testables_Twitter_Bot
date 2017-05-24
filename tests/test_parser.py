import unittest
from ..src.argparser import ArgParser


# test command line arguments
class TestParser (unittest.TestCase):

    # argument list should be string
    def test_type_of_arguments(self):
        # number
        with self.assertRaises(TypeError):
            ArgParser(1)
        # string
        with self.assertRaises(TypeError):
            ArgParser("pepas")
        # empty list
        with self.assertRaises(ValueError):
            ArgParser([""])

    def test_too_little_arguments(self):
        with self.assertRaises(ValueError):
            ArgParser(['-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_too_many_arguments(self):
        # one more than it should
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-12:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump',
                       'extra'])

    def test_timezone_format_sign(self):
        # invalid character
        with self.assertRaises(ValueError):
            ArgParser(['-t', '/12:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])
        # no sign at all
        with self.assertRaises(ValueError):
            ArgParser(['-t', '12:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])
        # empty variable
        with self.assertRaises(ValueError):
            ArgParser(['-t', '', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_timezone_format_upper_value(self):
        # over +14:00
        with self.assertRaises(ValueError):
            ArgParser(['-t', '+66:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])
        # +00:00
        with self.assertRaises(ValueError):
            ArgParser(['-t', '+00:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_timezone_format_lower_value(self):
        # lowest possible: -12:00
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-13:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])
            # -00:00
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-00:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_timezone_format_colon(self):
        # colon missing
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-1200', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_timezone_format_minutes_not_zero(self):
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-12:11', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_date_format_start_date(self):
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-12:00', '-a', '16-05-2017', '-b', '2017-05-17', '-i', '@realDonaldTrump'])

    def test_date_format_end_date(self):
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-12:00', '-a', '2017-05-16', '-b', '05-17-2017', '-i', '@realDonaldTrump'])

    def test_twitter_id_format(self):
        with self.assertRaises(ValueError):
            ArgParser(['-t', '-12:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', 'realDonaldTrump'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
unittest.TextTestRunner(verbosity=2).run(suite)
