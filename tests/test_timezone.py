import unittest
from datetime import datetime,timedelta
import sys
sys.path.append("..")

from src.timezone import TimeZoneConverter


class TestTimeZone(unittest.TestCase):

    def test_exceptions(self):
        #Should only accept strings
        with self.assertRaises(TypeError):
            t = TimeZoneConverter(1)

        #Should only accepts strings with format -HH:MM or +HH:MM
        with self.assertRaises(ValueError):
            t = TimeZoneConverter("02:30")

    def test_offset_generation(self):
        #Should correctly generate the offsets
        t = TimeZoneConverter("+02:30")
        expected = timedelta(hours=2,minutes=30)
        self.assertEqual(t.offset, expected)

        #Since we have to subtract 2:30, we have to split it up so each component is subtracted aswell
        #Thus we expect hours = -2 and minutes = -30 instead of minutes = 30 (which would add to the time delta)
        t1 = TimeZoneConverter("-02:30")
        expected1 = timedelta(hours=-2, minutes=-30)
        self.assertEqual(t1.offset, expected1)

    def test_correctly_changes_hours_and_minutes(self):
        #Test to see if hours and minutes correctly subtract
        initial = datetime(2017, 1, 1, 1, 59)
        t = TimeZoneConverter("-01:59")
        expected = datetime(2017, 1, 1)
        self.assertEqual(t.convert(initial), expected)

        #Test to see if they correctly add
        t = TimeZoneConverter("+01:02")
        expected = datetime(2017, 1, 1, 3, 1)
        self.assertEqual(t.convert(initial), expected)

    def test_correctly_changes_day(self):
        #See if time rolls back
        initial = datetime(2017, 1, 1)

        t = TimeZoneConverter("-01:00")
        expected = datetime(2016, 12, 31, 23, 0)
        self.assertEqual(t.convert(initial), expected)

        #See if time rolls forward
        t = TimeZoneConverter("+24:30")
        expected = datetime(2017, 1, 2, 0, 30)
        self.assertEqual(t.convert(initial), expected)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeZone)
unittest.TextTestRunner(verbosity=2).run(suite)
