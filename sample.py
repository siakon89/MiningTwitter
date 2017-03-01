#import appropriate packages
import twitter
import json

#create a class to be able to use it properly
class SampleTwitter:

    #declare class variables
    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''

    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):

        # Twitter tokens
        SampleTwitter.consumer_key = consumer_key
        SampleTwitter.consumer_secret = consumer_secret
        SampleTwitter.access_token_key = access_token_key
        SampleTwitter.access_token_secret = access_token_secret


    #use the python-twitter package to get the tweets
    #where screen_name is name of the account you want to sample
    def getTweets(self, screen_name):

        # Connect to twitter api
        api = twitter.Api(consumer_key=SampleTwitter.consumer_key, consumer_secret=SampleTwitter.consumer_secret, access_token_key=SampleTwitter.access_token_key, access_token_secret=SampleTwitter.access_token_secret)
        statuses = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=True,
                                       trim_user=False, exclude_replies=True)
        #Gather all tweets to a list
        tweets = []

        for i in statuses:
            #the tweets come ona jason format
            tweet = json.loads(str(i))
            tweets.append(tweet['text'])

        return tweets
