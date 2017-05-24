# FIT4004 Assignment 3 - Twitter Bot UnitTests
Analyses tweets made by an individual, produces a graph showing
frequency of tweeting at particular times of the day, and
posts the graph as a tweet


##Command Line Arguments:
```
-t TIMEZONE : the timezone of the tweeter for analysis purposes. TIMEZONE should be
represented as +/- HH:MM (that is, if a tweet occurred at 13:45 UTC, and their timezone was
+10:00, the tweet is regarded as having occurred at 23:45). The default is UTC.

-a DATE : the date (in local time as specified by the -t argument, if present) to begin analysis
from. Specified as YYYY-MM-DD.

-b DATE : the last date (in local time as specified by the -t argument, if present) to analyse.
Specified as YYYY-MM-DD.

-i ID : The id of the tweeter to analyse. ID should start with the @ sign.
The graph should be a simple line graph showing the time of day on the X-Axis and the average
number of tweets per hour on the Y-Axis.
```


##Twitter Account

Twitter account used: @The_Testables_Bot: https://twitter.com/TheTestablesBot
to change twitter account edit:

```
consumer_key, consumer_secret, access_token, access_token_secret
```
in main.py

## How to install dependencies

```
pip install -r requirements.txt
```

## Sample run
```
main.py -t +10:00 -a 2010-05-16 -b 2017-05-17 -i @realDonaldTrump
```

## Sample output
```
Twitter ID:  @realDonaldTrump From:  2016-01-16 00:00:00 To:  2017-06-17 00:00:00
Fetching...
Analysing and Building Graph...
Tweeting...
Finished!!
```

