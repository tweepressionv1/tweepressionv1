import nltk
import numpy
import re
import pickle
import tweepy
username = input("Twitter username: ")

consumer_key=""
consumer_secret=""
access_key=""
access_secret=""


def get_all_tweets(screen_name):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        alltweets = []
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            #print("...%s tweets downloaded so far" % (len(alltweets)))
        outtweets = [tweet.text.encode("utf-8")for tweet in alltweets]
    except tweepy.error.TweepError:
        print("Nope")
        return None

    return outtweets

naiveBayes = pickle.load(open("bayes.pickle", "rb"))
word_features = pickle.load(open("features.pickle", "rb"))  # REMEBER TO DO .KEYS()!!
svm = pickle.load(open("svm.pickle","rb"))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features.keys():
        features['contains(%s)' % word] = (word in document_words)
    return features


x = get_all_tweets(username)
sum = 0
num = 0


if(x is not None):
    if(len(x) <= 100):
        print("INSUFFICIENT NUMBER OF TWEETS")
        exit(2)
    for tweet in x:
        newTweet2 = str(tweet[2:])
        newTweet2 = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newTweet2).split())).strip(" ")
        answer = naiveBayes.classify(extract_features(newTweet2))
        if(answer == "positive"):
            sum += 1
    num += 1
    avg = (sum+0.0)/num
    print(sum/num)
    print(svm.predict([[avg]][0]))
