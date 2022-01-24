import tweepy
import time
auth = tweepy.OAuthHandler("zBGDHEmb8sDiwP7iCM3vDsAbq", "gFM8ipxUvctC9GlOc90DZwD6Ltwtv9qqI9AeRWA12vK1DH9IlU" )
auth.set_access_token("1286821356781305856-gMnzQpr1B92pQD0hd1auzMEVZXMPeS", "1ag8zH8lzQsMlk2UaUDkv40LZ7GnfKjP2Sb1cnzPBHt8f")
authenticator = tweepy.OAuthHandler("zBGDHEmb8sDiwP7iCM3vDsAbq", "gFM8ipxUvctC9GlOc90DZwD6Ltwtv9qqI9AeRWA12vK1DH9IlU")
authenticator.set_access_token("1286821356781305856-gMnzQpr1B92pQD0hd1auzMEVZXMPeS", "1ag8zH8lzQsMlk2UaUDkv40LZ7GnfKjP2Sb1cnzPBHt8f")
api = tweepy.API(authenticator, wait_on_rate_limit=True)

num = 1
while num <=20:
    crypto_coin = "GT"
    search_term = f'{crypto_coin} -filter:retweets'
    tweet_cursor = tweepy.Cursor(api.search_tweets, q= search_term, lang="tr",tweet_mode="popular").items(1)
    tweets = [tweet.id for tweet in tweet_cursor]
    api.retweet(tweets[0])
    num += 1
    time.sleep(60)

