"""
This code is for streaming tweets that match a given set of hashtags
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials
import numpy as np
import pandas as pd

###TWITTER AUTHENTICATOR###
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.api_key,credentials.api_secret_key)
        auth.set_access_token(credentials.access_token,credentials.access_token_secret)
        return auth

###TWITTER STREAMER###
class TwitterStreamer():
    """
    Class for streaming and processing live tweets
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self,fetched_tweets_filename, hash_tag_list):
        #this hanldes tw authentication and the connection to tehe tw streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        #tweet filter
        stream.filter(track=hash_tag_list)

###TWITTER LISTENER###
class TwitterListener(StreamListener):
    """
    This is a basic listener class that just prints recieved tweets to stdout
    """
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename,"a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self,data):
        if status == 420:
            # Returning false on_data method in case rate limit occurs
            return False
        print(status)


if __name__ == "__main__":
    """
    initialize app
    """
    hash_tag_list = ["beirut"]
    fetched_tweets_filename = "beirut_tweets.py" #set output file

    twitter_streamer = TwitterStreamer() #create instance of the streamer class
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list) #call the stream method