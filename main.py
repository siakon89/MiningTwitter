from sample import SampleTwitter

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token_key = 'access token key'
access_token_secret = 'access token secret'


sampling = SampleTwitter(consumer_key, consumer_secret, access_token_key, access_token_secret)

tweets = sampling.getTweets('siaterliskonsta')


for tweet in tweets:
    print tweet

