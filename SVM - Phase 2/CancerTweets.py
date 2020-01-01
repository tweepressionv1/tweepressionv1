import tweepy
import csv  # Import csv
auth = tweepy.auth.OAuthHandler('KfnEeAWUH3PYOtddB2Kcdmk5i', '7MD619cW1mkN1J2qwMJFgp9mF2gjOo7ghLYla46VFjodtJ0495')
auth.set_access_token('765735365072138240-rU8AzIykP4t6stMiRtWh6PWXj0n6C1s', 'yEOZokiXbCBLloNfHdr7PCXS9P5u1o18Paaq6Cyazy9YG')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('CancerTweets2.csv', 'a')

# Use csv writer
csvWriter = csv.writer(csvFile)

csvWriter.writerow(["id", "user_name", "text"])
query = '\"I have cancer\" OR \"I have been diagnosed with cancer\" OR \"I am diagnosed with cancer\"-filter:retweets'
for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.user.id, api.get_user(tweet.user.id).screen_name, tweet.text.encode('utf-8')])
    #print(api.get_user(tweet.user.id).screen_name, tweet.text)
csvFile.close()