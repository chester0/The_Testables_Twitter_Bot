import unittest
import datetime
from src.arg_parser import ArgParser


# test command line arguments
class TestParser (unittest.TestCase):

    arguments = ['-t', '-12:00', '-a', '2017-05-16', '-b', '2017-05-17', '-i', '@realDonaldTrump']
    argument_parser = ArgParser(arguments)

    # should have 8 or 7 arguments
    # timezone is optional, local timezone is assumed if missing
    def test_number_of_arguments(self):
        # check arguments
        if self.argument_parser.arg_length != 8 and self.argument_parser.arg_length != 7:
            raise ValueError('Wrong number of arguments: ', self.argument_parser.arg_length)

    # represented as +/-HH:MM
    # follows after -t
    def test_timezone_argument(self):
        if self.argument_parser.timezone[:1] != '+' and self.argument_parser.timezone[:1] != '-':
            raise ValueError('No leading sign on timezone, found: ', self.argument_parser.timezone[:1])

        if self.argument_parser.timezone[:1] == '+':
            if int(self.argument_parser.timezone[1:3]) > 14 or int(self.argument_parser.timezone[1:3]) < 0:
                raise ValueError('Invalid (+UTC) timezone. found: ', self.argument_parser.timezone[1:3])

        if self.argument_parser.timezone[:1] == '-':
            if int(self.argument_parser.timezone[1:3]) > 12 or int(self.argument_parser.timezone[1:3]) < 1:
                raise ValueError('Invalid (-UTC) timezone. found: ', self.argument_parser.timezone[1:3])

        if self.argument_parser.timezone[3:4] != ':':
            raise ValueError('Invalid timezone format missing ":" found: ', self.argument_parser.timezone[3:4])

        if self.argument_parser.timezone[4:6] != '00':
            raise ValueError('Invalid timezone format, minutes not 0 or not a number. Found: ',
                             self.argument_parser.timezone[4:6])

    # represented by YYYY-MM-DD
    # follows after -a
    def test_start_date_argument(self):
        datetime.datetime.strptime(self.argument_parser.start_date, '%Y-%m-%d')
        self.assertRaises(ValueError)

    # represented by YYYY-MM-DD
    # follows after -b
    def test_end_date_argument(self):
        datetime.datetime.strptime(self.argument_parser.end_date, '%Y-%m-%d')
        self.assertRaises(ValueError)

    # starts with @
    # follows after -i
    def test_id_argument(self):
        self.assertEqual(self.argument_parser.twitter_id[:1], "@")


suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
unittest.TextTestRunner(verbosity=2).run(suite)
