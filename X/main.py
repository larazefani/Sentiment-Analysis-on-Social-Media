from textblob import TextBlob
from tweepy import Client
import tweepy
import sys

mykeys = open(r'C:\Users\p\xkeys.txt', 'r').read().splitlines()
bearer_token = mykeys[4]

client = Client(bearer_token=bearer_token)

search_term = 'literasi'
tweet_amount = 100

tweets = client.search_recent_tweets(
    query=search_term + ' lang:id',
    max_results=tweet_amount
)

polarity = 0

positive = 0
neutral = 0
negative =0

for tweet in tweets.data:
    final_text = tweet.text.replace('RT','')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1
    polarity += tweet_polarity
    
print(polarity)
print(f'Jumlah tweet positif: {positive}')
print(f'Jumlah tweet netral: {neutral}')
print(f'Jumlah tweet negatif: {negative}')