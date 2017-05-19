import getopt
import sys
# parses command line arguments


class ArgParser:

    def __init__(self, argv):
        try:
            opts, args = getopt.getopt(argv, ":t:a:b:i:", ["TIMEZONE=", "START_DATE=", "END_DATE", "ID"])
        except getopt.GetoptError:
            print('get opt error')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-t", "--t timezone"):
                timezone = arg
            elif opt in ("-a", "--a start_date"):
                start_date = arg
            elif opt in ("-b", "--b end_date"):
                end_date = arg
            elif opt in ("-a", "--a start_date"):
                start_date = arg
            elif opt in ("-i", "--a twitter_id"):
                twitter_id = arg

            # check arguments
            if len(sys.argv) != 9:
                print('wrong number of arguments. Usage: main.py -t <TIMEZONE> -a <START_DATE> -b <END_DATE> -i <TWITTER_ID')
                # sys.exit()
            print('Number of arguments:', len(sys.argv), 'arguments.')
            print('Argument List:', str(sys.argv))
            print('Timezone:', timezone)
            print('Start date:', start_date)
            print('End date:', end_date)
            print('Twitter ID:', twitter_id)
