# Tweets_Opinions
<img src="https://icon-library.com/images/tweet-icon/tweet-icon-27.jpg" width="20%" align="center"/></a> 
<img src="https://www.sundayguardianlive.com/wp-content/uploads/2022/02/istockphoto-862291374-612x612.jpg" width="20%" align="center"/></a> 

This repo contains the capstone project of Misk Data Science Immersive 2021-12.

### Project Objective

Wars are the most destroying factor for humanity. Regardless of the political justifications, no one wants to continue wars in which innocent people are the victims. Our hearts goes out to all that are affected by the war, and we pray for them.

On 28 Feburar 2022, The Russia/Ukraine war was starting and the #ukrainerussiawar hashtag become popular on twitter all over the world. In this project I was trying to predict the emotion of the the tweets in general, and to extract the adjectives that described both Russia and Ukrainie from the tweets that used the hashtag #ukrainerussiawar.

### Phase 1 - Setup

The file phase1_import_tweets.py has the script to import the tweets using Twitter API api.search_tweets. in order to be able to run this file you have to have twitter developer account to obtain Twitter API Security codes. I hide my own for security purpose. 

To run this file you have to have config.ini file that contains your own API twitter security key, it should be saved as following:

api_key = 'YOUR API Key'

api_key_secret = 'YOUR API Key Secret'

access_token = 'YOUR Access Token'

access_token_secret = 'YOUR Access Token Secret'

### Phase 2 - Data Collection / Data Cleaning & EDA

As I target the topic of Ukraine/Russia war, I was able to importe more than 26000 tweets that contains either Ukraine, Russia or #UkraineRussiawar. I used this data as a raw dataset for my porject.

In phase2_clean_tweets.ipynb file, I read the imported tweets from CSV file to dataframe, and after deleting the duplicate tweets, I end up with the 25678 tweets which 98% of them are missing their country code.
I went through text pre-processing including convert to lower case, removing links and special characters, removing stop words and words lemmatization.

### Phase 3 - Conclusion

In the end of phase2_clean_tweets.ipynb file, I illustrated in bar graph the common emotions that was in tweets, and showed the adjective that associated with Russia and Ukraine in word cloud separately

<img src= "https://us.123rf.com/450wm/martialred/martialred1701/martialred170100111/70392184-flying-dove-holding-an-olive-branch-as-a-sign-of-peace-flat-vector-icon-for-apps-and-websites.jpg?ver=6" width="20%" align="center"/></a> 