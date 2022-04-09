# Installing libraries
%pip install langdetect 
%pip install pysentiment2
%pip install python-binance

# Importing all libraries to be used in the code
import requests
import os
import json
from langdetect import detect
from csv import writer
import numpy as np
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import pysentiment2 as ps
from binance import Client
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import time

sentiment_scores = [] # Initialising the sentiment_scores list which will hold the positive sentiment scores(Percentage of eligible tweets with positive sentiments)
price_l = [] # List holds the average price of the currency over the time
negative_sentiment_scores = [] # This list holds the percentage of tweets with negative sentiments over time
limit = 50 # This is the number of tweets to scrape in each iteration
token = str(input('Coin name to look with on twitter: ')) # This means the name of the currenct like BTC,ETH,LTC to be looked out for on Twitter
currency = str(input('Currency name: ')) # Name of the currency to be looked out for on Binance like BTCUSDT,ETHUSDT etc.
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAHH9UAEAAAAA5sA0o6M6OjrRNJ0pNpHKypL%2B%2Bm8%3D3KAHM2kj6PEG0QCNrzMQnacky5IcFHzJYoLhyF2cPAWypKmTbZ" # Twitter api bearer token
in_position = False
client = Client('HysmriB8kLQnMzVqRTjnTpCAFZOrJLx4pxT4Ch3a852bECoNgXtmWkGtxubtSbZK','4juSFo7kh4Kcb0DwP2ds5fAh5ilyGVYUaBnXfCGCoale4ns1tCxtBffFOgIM36g0') # Creating the object for binance class to scrape then prices
# This function creates the header with bearer token, header helps while sending a request for data to twitter server
def create_headers(bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers

# Getting stream rules and putting them into a json
def get_rules(headers, bearer_token):
    # Sending a request GET command to server to get all rules and if we dont face any exception then put the rules into a json format
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    # In case of exception letting the user know
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()

# Deleting the default rules as we want to reset them to be able to scrape tweets.
def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))

# This function sets the rules for scraping the tweets
def set_rules(headers, delete, bearer_token):
    # You can adjust the rules if needed
    global token # Getting the token name given in user input
    sample_rules = [
        {"value": f"#{token}", "tag": token},
    ]
    payload = {"add": sample_rules}
    # Putting the rules into the twitter stream with help of POST command
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    # If we get a exception then letting the user know
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, set, bearer_token):
    # This function scrapes the tweets from the api contionously till limit is reached
    # The function first gets all tweets from the api then we iterate through the tweets and do a sentiment analysis on it then placing all variables into appropriate list/dictionary
    global sentiment_t,fg_index_d,limit
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    current_ind = 0
    for response_line in response.iter_lines(): # Iterating through the response from twitter api
        if response_line: 
            if current_ind == limit: # Checking if we havent hit the limit of number of tweets to look for per iteration
              break
            current_ind += 1
            json_response = json.loads(response_line) # Unloading the json response
            tweet = json_response['data']['text'] # Extracting tweet from json response
            tweet = tweet.replace(':','') # Cleaning the tweet
            try:
                if detect(tweet) == 'en': # If tweets language is english
                    print('')
                    print(tweet)
                    print('')
                    try: 
                        tokens = lm.tokenize(tweet) # Applying sentiment analysis on the tweet
                        score = lm.get_score(tokens)
                        if score['Positive']>score['Negative']: # If tweets positive score exceeds the negative then adding +1 into positive sentiment tweets and similar for negative sentiment tweets
                            sentiment_t['Positive']+=1
                        elif score['Negative']>score['Positive']:
                            sentiment_t['Negative']+=1
                    except:
                        pass
            except Exception as e:
              print(e)
              pass
def main():
    # Here we just call the above functions in right order
    # This function is like a driver code
    try:
        bearer_token = BEARER_TOKEN
        headers = create_headers(bearer_token)
        rules = get_rules(headers, bearer_token)
        delete = delete_all_rules(headers, bearer_token, rules)
        set = set_rules(headers, delete, bearer_token)
        get_stream(headers, set, bearer_token)
    except Exception as ef:
        print(ef)
        print('Done')

for x in range(3): # Scraping the tweets and processing them n time given in range
    lm = ps.LM() # Initialising the sentiment analysis object
    sentiment_t = {'Positive':0,'Negative':0} # Initialising the sentiments dictionary to be used
    main() # Calling the main function to start the process
    print(sentiment_t) # After limit is reached printing the sentiments list and how much positive score was
    print(f'Tweet Sentiment : {max(sentiment_t, key=sentiment_t.get)}')

    # Calculating the negative sentiments percentage,positive sentiments percentage
    negative_sentiment_score = (sentiment_t['Negative']/sum(sentiment_t.values()))*100
    tweet_score=(sentiment_t['Positive']/sum(sentiment_t.values()))*100
    print(f'Tweets Positive Sentiment Score : {tweet_score}')
    avg_price = client.get_avg_price(symbol=currency) # Fetching price from binance
    sentiment_scores.append(tweet_score) # Adding positive sentiment percentage,negative sentiment percentage and avg price at the moment into the appropriate list
    price_l.append(avg_price)
    negative_sentiment_scores.append(negative_sentiment_score)
    print('########### 10 SECONDS BREAK ##############')
    time.sleep(10)

prices = []
for x in price_l:
  prices.append(float(x['price'])) # Extracting prices fetched over time
corr, _ = pearsonr(sentiment_scores, prices) # Calculating pearson correlation between positive sentiments percentage and prices over time
print('Correlation: %.3f' % corr) # Printing the correlation
figure, axis = plt.subplots(3, 1) # Creating 3 plots in 1 columns
axis[0].plot(sentiment_scores) # Plotting the positive sentiments graph
axis[0].set_title("Positive Sentiments")

axis[1].plot(prices) # Plotting the price graph
axis[1].set_title("Price")

axis[2].plot(negative_sentiment_scores) # Plotting the negative sentiments graph
axis[2].set_title("Negative Sentiments")

figure.tight_layout()
plt.show() # Showing all graphs
