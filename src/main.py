
import tweepy

consumer_key = 'nQr62OZwOWTK5WxGFFwNgo8Ir'
consumer_secret = '768VVh1exJAvMXEMIAlSx9Sk84EKI1hG6cOC83zELZPnOCQjXN'
access_token = '864747008111788033-eFZKCN7HYr3CxiEyZXNEtbCSmIVjc1V'
access_token_secret = 'mv7WAAFZ1MHIQX22zl8q8YVw138GuGXDuqO5yu7LDO4cr'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

# user = api.get_user('realDonaldTrump')
# print("Name:", user.name)
# print("Location:", user.location)
# print("Following:", user.friends_count)
# print("Followers:", user.followers_count)
