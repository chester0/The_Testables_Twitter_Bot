import unittest
import datetime


# test command line arguments
class TestParser (unittest.TestCase):

    # should have 9 arguments
    # or is timezone optional?
    def test_number_of_arguments(self):
        pass

    # represented as +/-HH:MM
    # follows after -t
    def test_timezone_argument(self):
        pass

    # represented by YYYY-MM-DD
    # follows after -a
    def test_start_date_argument(self):
        start_date = "2005-12-25"
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.assertRaises(ValueError)

    # represented by YYYY-MM-DD
    # follows after -b
    def test_end_date_argument(self):
        date_text = "2005-12-25"
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        self.assertRaises(ValueError)

    # starts with @
    # follows after -i
    def test_id_argument(self):
        t_id = "@test_name"
        self.assertEqual(t_id[:1], "@")


suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
unittest.TextTestRunner(verbosity=2).run(suite)