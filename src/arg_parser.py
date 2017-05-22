import getopt
import sys
# parses command line arguments


class ArgParser:

    timezone = ""
    start_date = ""
    end_date = ""
    twitter_id = ""
    arg_length = ""

    def __init__(self, argv):

        try:
            opts, args = getopt.getopt(argv, ":t:a:b:i:", ["TIMEZONE=", "START_DATE=", "END_DATE", "ID"])
        except getopt.GetoptError:
            print('get opt error')
            sys.exit(2)
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

        # print('Number of arguments:', self.arg_length, 'arguments.')
        # print('Argument List:', str(argv))
        # print('Timezone:', self.timezone)
        # print('Start date:', self.start_date)
        # print('End date:', self.end_date)
        # print('Twitter ID:', self.twitter_id)
