from datetime import timedelta


# Converts UTC dates to a given timezone in the format +/-HH:MM
class TimeZoneConverter:
    def __init__(self, timezone):
        # Check that the timezone is a string
        if not isinstance(timezone, str):
            raise TypeError("Timezone must be a string")

        # Check that it's in the right format
        if len(timezone) != 6:
            raise ValueError("Timezone must be in the format +HH:MM or -HH:MM")

        # Work out the time deltas
        self.timezone = timezone
        hours = int(timezone[:3])
        minutes = int(timezone[0] + timezone[4:])
        self.offset = timedelta(hours=hours, minutes=minutes)

    # Convert a UTC date to the set timezone of the converter
    def convert(self, date):
        return date + self.offset

