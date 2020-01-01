#!/usr/bin/python
import tweepy
# Import csv
import csv
import time
auth = tweepy.auth.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('DepressionTweets2.csv', 'a')

# Use csv writer
csvWriter = csv.writer(csvFile)

csvWriter.writerow(["id", "user_name", "text"])

try:
    query = '\"I was diagnosed with depression\" OR \"I have been diagnosed with depression\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)
    query = '\"I am diagnosed with depression\" OR \"I have depression\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)

except tweepy.RateLimitError:
    time.sleep(60*15)
    query = '\"I was diagnosed with depression\" OR \"I have been diagnosed with depression\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)

    query = '\"I am diagnosed with depression\" OR \"I have depression\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)

try:
    query = '\"I was diagnosed with major depressive disorder\" OR \"I have been diagnosed with major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)

    query = '\"I am diagnosed with major depressive disorder\" OR \"I have major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)
except tweepy.RateLimitError:
    time.sleep(60*15)
    query = '\"I was diagnosed with major depressive disorder\" OR \"I have been diagnosed with major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)

    query = '\"I am diagnosed with major depressive disorder\" OR \"I have major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)

try:
    query = '\"I was diagnosed with MDD\" OR \"I have been diagnosed with MDD\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)

    query = '\"I am diagnosed with MDD\" OR \"I have MDD\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        #print(api.get_user(tweet.user.id).screen_name, tweet.text)

except tweepy.RateLimitError:
    time.sleep(60*15)
    query = '\"I was diagnosed with major depressive disorder\" OR \"I have been diagnosed with major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)

    query = '\"I am diagnosed with major depressive disorder\" OR \"I have major depressive disorder\" -filter:retweets'
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
        # print(api.get_user(tweet.user.id).screen_name, tweet.text)


csvFile.close()