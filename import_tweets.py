from datetime import datetime, timedelta
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
#from tweepy.streaming import StreamListener
import pandas as pd
import json
import csv
import sys
import time
import configparser

#reload(sys)
#sys.setdefaultencoding('utf8')
config = configparser.ConfigParser()
config.read('config.ini')

ckey = config['twitter']['api_key']
csecret = config['twitter']['api_key_secret']
atoken = config['twitter']['access_token']
asecret = config['twitter']['access_token_secret']

def toDataFrame(tweets):
    # Convert to data frame
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['retweeted'] = [tweet.retweeted for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetdate'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    DataSet['Coordinates'] = [tweet.coordinates for tweet in tweets]
    DataSet['Language'] = [tweet.lang for tweet in tweets]
    tweets_place= []
    tweets_country = []
    country_code = []
    for tweet in tweets:
        if tweet.place:
            tweets_place.append(tweet.place.full_name)
            tweets_country.append(tweet.place.country)
            country_code.append(tweet.place.country_code)
        else:
            tweets_place.append('null')
            tweets_country.append('null')
            country_code.append('null')

    DataSet['TweetPlace'] = [i for i in tweets_place]
    DataSet['Tweetcountry'] = [i for i in tweets_country]
    DataSet['countrycode'] = [i for i in country_code]
    return DataSet

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
#auth = tweepy.AppAuthHandler('XXXXXXXX', 'XXXXX')

#api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
api = tweepy.API(auth)

# Get place id
places = api.search_geo(query="Ukraine", granularity="country")
place_id = places[0].id
print(place_id)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
else:
    count = 10000 # Set the number of tweets to retrieve
    #words = input('Enter Twitter HashTag to search for: ')
    words = 'Ukraine OR Russia OR #ukrainerussiawar OR #UkraineWar -filter:retweets'
    #print(words)
    print ("Scraping data now") 
    #cursor = api.search_30_day(label='MISK', query="place:%s" % place_id, fromDate="202202200000", toDate="202203010000")
    cursor = tweepy.Cursor(api.search_30_day,label='MISK', query="place:%s" % place_id, fromDate="202202200000", toDate="202203010000")
    #cursor = tweepy.Cursor(api.search_tweets,words,lang='en')
    #cursor = tweepy.Cursor(api.search_tweets,words,geocode=geocode,until = next_day.date())

    results=[]
    for item in cursor.items(count):
        results.append(item)

    DataSet = toDataFrame(results)

    # check if the file exist, it will add the data 
    try:
        with open('./data/russia_raw_tweets.csv') as f:
            print('Add The data to the existing file')
            DataSet.to_csv('./data/russia_raw_tweets.csv',mode='a', header=False, index=False)
    except IOError:
       print('Create new file')
       DataSet.to_csv('./data/russia_raw_tweets.csv', index=False)
    
    print ("Completed.. !!")