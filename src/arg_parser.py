import getopt
import datetime


# parses command line arguments
class ArgParser:

    timezone = ""
    start_date = ""
    end_date = ""
    twitter_id = ""
    arg_length = ""

    def __init__(self, argv):

        # Check that arguments is a list
        if not isinstance(argv, list):
            raise TypeError("Arguments must be of type: list")

        try:
            opts, args = getopt.getopt(argv, ":t:a:b:i:", ["TIMEZONE=", "START_DATE=", "END_DATE", "ID"])
        except getopt.GetoptError:
            raise ValueError('get opt error, invalid options detected')
        self.arg_length = len(argv)
        for opt, arg in opts:
            if opt in ("-t", "--t timezone"):
                self.timezone = arg
            elif opt in ("-a", "--a start_date"):
                self.start_date = arg
            elif opt in ("-b", "--b end_date"):
                self.end_date = arg
            elif opt in ("-a", "--a start_date"):
                self.start_date = arg
            elif opt in ("-i", "--a twitter_id"):
                self.twitter_id = arg

        # check arguments
        # should have 8 or 7 arguments
        # timezone is optional, local timezone is assumed if missing
        if self.arg_length != 8 and self.arg_length != 7:
            raise ValueError('Wrong number of arguments: ', self.arg_length)

        # validate timezone format: +/-10:00 *max +14:00, min -12:00
        if self.timezone[:1] != '+' and self.timezone[:1] != '-':
            raise ValueError('No leading sign on timezone, found: ', self.timezone[:1])
        if self.timezone[:1] == '+':
            if int(self.timezone[1:3]) > 14 or int(self.timezone[1:3]) < 0:
                raise ValueError('Invalid (+UTC) timezone. found: ', self.timezone[1:3])
        if self.timezone[:1] == '-':
            if int(self.timezone[1:3]) > 12 or int(self.timezone[1:3]) < 1:
                raise ValueError('Invalid (-UTC) timezone. found: ', self.timezone[1:3])
        if self.timezone[3:4] != ':':
            raise ValueError('Invalid timezone format missing ":" found: ', self.timezone[3:4])
        if self.timezone[4:6] != '00':
            raise ValueError('Invalid timezone format, minutes not 0 or not a number. Found: ',
                             self.timezone[4:6])

        # start date, represented by YYYY-MM-DD
        try:
            datetime.datetime.strptime(self.start_date, '%Y-%m-%d')
        except ValueError as err:
            raise ValueError(err)

        # end date, represented by YYYY-MM-DD
        try:
            datetime.datetime.strptime(self.end_date, '%Y-%m-%d')
        except ValueError as err:
            raise ValueError(err)

        # test twitter_id starts with @
        if self.twitter_id[:1] != "@":
            raise ValueError('Invalid twitter ID: No leading @')

        # print('Number of arguments:', self.arg_length, 'arguments.')
        # print('Argument List:', str(argv))
        # print('Timezone:', self.timezone)
        # print('Start date:', self.start_date)
        # print('End date:', self.end_date)
        # print('Twitter ID:', self.twitter_id)
