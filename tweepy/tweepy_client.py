"""
This code is for streaming tweets of a given account
"""

from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler

import credentials
import numpy as np
import pandas as pd

###TWITTER CLIENT###
class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    #this method is for general timeline, including retweets and replies
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    #this method is for getting friend list of user
    def get_friend_list(self,num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    
    #this method is for home timeline, no replies  
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

###TWITTER AUTHENTICATOR###
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.api_key,credentials.api_secret_key)
        auth.set_access_token(credentials.access_token,credentials.access_token_secret)
        return auth


if __name__ == "__main__":
    """
    initialize app
    """

    twitter_client = TwitterClient("reuters") #TwitterClient takes user as parameter. If no user is stated it looks up in own account
    print(twitter_client.get_user_timeline_tweets(1))
