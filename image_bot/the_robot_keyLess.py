# therobot

import tweepy as tp
import time
import os

# credentials to login to twitter api 
# found in Developer Portal -> Project -> Keys and tokens
# don't share your keys
consumer_key = # your API key
consumer_secret = # your API secret goes here
access_token = # your access token goes here
access_secret = # your access secret goes here

# login to twitter account api
# see docs.tweepy.com for more information on this section
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('images')

# iterates over pictures in target folder, posts them to twitter at a fixed interval
for model_image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(60)
