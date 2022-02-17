import tweepy
import configparser
import pandas as pd

#read configparser
config = configparser.ConfigParser()
config.read('config.ini')

api_key =config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication 
auth= tweepy.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# function to perform data extraction
def scrape(words, date_since, numtweet):

		# Creating DataFrame using pandas
		db = pd.DataFrame(columns=['username',
								'description',
								'location',
								'hashtags',
								'text'])

		# We are using .Cursor() to search
		# through twitter for the required tweets.
		# The number of tweets can be
		# restricted using .items(number of tweets)
		tweets = tweepy.Cursor(api.search_tweets,
							words, lang="en",
							since_id=date_since,
							tweet_mode='extended').items(numtweet)


		# .Cursor() returns an iterable object. Each item in
		# the iterator has various attributes
		# that you can access to
		# get information about each tweet
		list_tweets = [tweet for tweet in tweets]

		# Counter to maintain Tweet Count
		i = 1

		# we will iterate over each tweet in the
		# list for extracting information about each tweet
		for tweet in list_tweets:
				username = tweet.user.screen_name
				description = tweet.user.description
				location = tweet.user.location
				hashtags = tweet.entities['hashtags']

				# Retweets can be distinguished by
				# a retweeted_status attribute,
				# in case it is an invalid reference,
				# except block will be executed
				try:
					text = tweet.retweeted_status.full_text
				except AttributeError:
					text = tweet.full_text
				hashtext = list()
				for j in range(0, len(hashtags)):
						hashtext.append(hashtags[j]['text'])

				# Here we are appending all the
				# extracted information in the DataFrame
				ith_tweet = [username, description,
							location, hashtext, text]
				db.loc[len(db)] = ith_tweet
				
				i = i+1
		filename = 'tweets_data.csv'

		# save  database as a CSV file.
		db.to_csv(filename)

if __name__ == '__main__':
	# Enter Hashtag and initial date
	#print("Enter Twitter HashTag to search for")
	words = input('Enter Twitter HashTag to search for: ')
	#print("Enter Date since The Tweets are required in yyyy-mm--dd")
	date_since = input('Enter Date since The Tweets are required in yyyy-mm--dd: ')

	# number of tweets you want to extract in one run
	numtweet = 200
	scrape(words, date_since, numtweet)
	print('Scraping has completed!')