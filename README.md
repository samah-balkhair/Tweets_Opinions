# Tweets_Opinions
<img src="https://icon-library.com/images/tweet-icon/tweet-icon-27.jpg" width="20%" align="center"/></a> 

This repo contains the capstone project of Misk Data Science Immersive 2021-12.
The idea of this project is to analyzing people’s opinion regarding certain hashtag by checking their tweets.


### Phase 1 - Collecting Data

The file import_tweets.py has the script to import the tweets using Twitter API. in order to be able to run this file you have to have twitter developer account to obtain Twitter API Security codes. I hide my own for security purpose. 

To run this file you have to have config.ini file that contains your own API twitter security key, it should be saved as following:

api_key = 'YOUR API Key '
api_key_secret = 'YOUR API Key Secret'
access_token = 'YOUR Access Token'
access_token_secret = 'YOUR Access Token Secret'

The file will ask you about the Hashtag and the date that you want to collect the data. then it will save it in csv file. Afterward, we can read it from Tweets_Opinions.ipynb in a dataframe format 

Note: the source that I use for importing script  https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/
