import numpy 
import pickle
from scipy import interp
from sklearn import svm, datasets
from sklearn.externals import joblib
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
import csv

import re

classifer = pickle.load(open("classify2.p","rb"))
users = []
with open("ConsolidatedDepressionTweets.csv", newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        if(len(row) >= 1):
            #print(row[0].split(',')[1])
            quoteIndex = 1
            #for i in range(1,  len(row)):
            users.append(row[0].split(',')[0])
    users = users[1:]
    print(users)

output = open("output.txt","w")

import tweepy  # https://github.com/tweepy/tweepy

consumer_key=""
consumer_secret=""

access_key=""
access_secret=""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_all_tweets(screen_name):
    try:
        # Twitter only allows access to a users most recent 3240 tweets with this method

        # initialize a list to hold all the tweepy Tweets
        alltweets = []

        # make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)
        #new_tweets = api.home_timeline()


        # save most recent tweets
        alltweets.extend(new_tweets)

        # save the id of the oldest tweet less one
        if(len(alltweets) == 0):
            return None

        oldest = alltweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            #print("getting tweets before %s" % (oldest))

            # all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

            # save most recent tweets
            alltweets.extend(new_tweets)

            # update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            #print("...%s tweets downloaded so far" % (len(alltweets)))

        # transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [tweet.text.encode("utf-8")for tweet in alltweets]
    except tweepy.error.TweepError:
        output.write("Nope user: " + screen_name+"\n")
        output.flush()    
        return None
    except:
        output.write("Twitter Connection Error user: " + screen_name+"\n")
        output.flush()
        return None

    return outtweets
    # # write the csv
    # with open('%s_tweets.csv' % screen_name, 'wb') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["id", "created_at", "text"])
    #     writer.writerows(outtweets)
    #
    # pass

word_features = pickle.load(open("features.p", "rb")) #REMEBER TO DO .KEYS()!!
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features.keys():
        features['contains(%s)' % word] = (word in document_words)
    return features

averagesDepressed = []
for user in users[0:5]:
    x = get_all_tweets(user)
    sum = 0
    num = 0
    if(x is not None):
        #print(user, x[0])
        for tweet in x[:100]:
            newTweet2 = str(tweet[2:])
            newTweet2 = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newTweet2).split())).strip(" ")
            answer = classifer.classify(extract_features(newTweet2))
            if(answer == "positive"):
                #print("POSITIVE")
                sum += 1
            num += 1
        avg = (sum+0.0)/num
        averagesDepressed.append(avg)
        output.write(str(sum/num) + " user: " + user+"\n")
        output.flush()
        #print(sum/num)

averagesHappy = []
query = 'happy'
try:
    for tweet in tweepy.Cursor(api.search, q = query, lang = "en").items()[0:5]:
        user = api.get_user(tweet.user.id).screen_name
        x = get_all_tweets(user)
        sum = 0
        num = 0
        if(x is not None):
            #print(user, x[0])
            for tweet in x[:100]:
                newTweet2 = str(tweet[2:])
                newTweet2 = (' '.join(re.sub("(@[A-Za-z0-9+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newTweet2).split())).strip(" ")
                answer = classifer.classify(extract_features(newTweet2))
                if(answer == "positive"):
                    sum += 1
                num += 1
            avg = (sum+0.0)/num
            averagesHappy.append(avg)
            #print(sum/num)
            output.write(str(sum/num) + " user: " + user+"\n")
            output.flush()
except tweepy.RateLimitError:
    pass

import random
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 1)
svmclassifier = svm.SVC(kernel = "linear", probability = True)
output.write("starting fitting"+'\n')
output.flush()
temptemp = svmclassifier.fit(x_train, y_train)
output.write("finished fitting"+'\n')
output.flush()
import pickle
pickle.dump(temptemp, open(("s2.p"), "rb"))
y_score = temptemp.decision_function(x_test)




