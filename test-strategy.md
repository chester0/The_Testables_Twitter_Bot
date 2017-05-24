# Test Strategy

Most of the tests will be aimed at functional correctness as per the spec
and making sure the input is correct as specified in the specification

Main functions are spitted into different classes to make testing of each component easier

- arg_parser.py handles the command line arguments and their validation
- timezone.py converts the UTC offset given to a timezone
- tweet_analyser.py makes a frequency dictionary from an array of tweets
- tweet_fetcher.py gets the tweets with the arguments given and adds them to an array
- tweet_submitter.py makes a graph from the frequency dictionary and posts it to twitter 

Functions that require network have been mocked out in the tests such as posting the tweet and
receiving the tweets.
Some tests were writen before the code, and code was make to pass the tests
then more test were written to try to make them to fail

## Argparser.py
Arguments will be validated in this class before passed on to the other
cases to avoid duplicate testing


- Checks if timezone is valid and the format is consistent with the spec, upper/lower boundaries,
and mid points
- Checks if the date format is correct (YYYY-MM-DD) for both
start and and date
- Checks number of arguments is 8 or 7 (timezone optional)
- Tests if ID starts with "@"


## Timezone.py

- Make sure offsets are generated correctly from given timezone string
 
## TweetAnalyser.py

- Make sure that we generate the frequencies correctly from the passed in tweets

## TweetFetcher.py

- Make sure we correctly fetch tweets.
- Make sure when adding tweets to an array that they are in between the given dates.


