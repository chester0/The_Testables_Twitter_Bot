#Test Strategy

Most of the tests will be aimed at functional correctness as per the spec
and making sure the input is correct as specified in the specification



# Arg_parser
Arguments will be validated in this class before passed on to the other
cases to avoid duplicate testing
- Checks if timezone is valid
- Checks if the date format is correct (YYYY-MM-DD) for both
start and and date
- Checks number of arguments is 9 (is timezone optional?)
- Tests if ID starts with "@"


# Timezone.py

Make sure offsets are generated correctly
 
# Tweetanalyser.py

