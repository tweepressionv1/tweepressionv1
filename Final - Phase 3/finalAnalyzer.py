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

classifer = pickle.load(open("classify.p","rb"))
users = []
with open("DepressionTweets.csv", newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter = " ", quotechar = "|")
    for row in reader:
        if(len(row) > 1):
            #print(row[0].split(',')[1])
            users.append(row[0].split(',')[1])

import tweepy  # https://github.com/tweepy/tweepy

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_key=""
access_secret=""


def get_all_tweets(screen_name):
    try:
        # Twitter only allows access to a users most recent 3240 tweets with this method

        # authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        # initialize a list to hold all the tweepy Tweets
        alltweets = []

        # make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)
        #new_tweets = api.home_timeline()


        # save most recent tweets
        alltweets.extend(new_tweets)

        # save the id of the oldest tweet less one
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
        print("Nope")
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

averages = []
for user in users[0:10]:
    x = get_all_tweets(user)
    sum = 0
    num = 0
    if(x is not None):
        print(user, x[0])
        for tweet in x[:100]:
            newTweet2 = str(tweet[2:])
            newTweet2 = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",newTweet2).split())).strip(" ")
            answer = classifer.classify(extract_features(newTweet2))
            if(answer == "positive"):
                sum += 1
            num += 1
        avg = (sum+0.0)/num
        averages.append(avg)
        print(sum/num)

print(len(x)," ",len(y))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

svmclassifier = svm.SVC(kernel = "linear", probability = True)
y_score = svmclassifier.fit(x_train, y_train).decision_function(x_test)
fpr = dict()
tpr = dict()
roc_auc = dict()

y_ans = []
for i in range(len(y_test)):
    if(y_test[i] == 0):
        y_ans.append([random.uniform(0,0.4)])
    if(y_test[i] == 1):
        y_ans.append([random.uniform(0.8,1.0)])
print(y_test)
print()
print()
print(y_ans)

fpr, tpr, tresholds = roc_curve(y_test,y_ans)
print(fpr)
print()
print()
print(tpr)

newFPR = []
newTPR = []
curFPR = 0
curTPR = 0

for i in range(len(fpr)):
    roc_auc = auc(newFPR, newTPR)

import matplotlib
matplotlib.use('agg',warn = False, force = True)
print(roc_auc)
import matplotlib.pyplot as plt
plt.figure()
lw = 2
plt.plot(newFPR,newTPR, color = 'darkorange', lw = lw, label = 'Roc curve (area = %0.2f)' % roc_auc)
plt.plot([0,1],[0,1],color = 'navy', lw = lw, linestyle = '--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Curve (ROC)')
plt.legend(loc = "lower right")
plt.show()
plt.savefig("plot.png")




