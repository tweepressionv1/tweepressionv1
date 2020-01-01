import nltk
import re


positive = []
negative = []
all = []
isFirst = True
with open("sentimentData.txt",'r', encoding='utf-8', errors='ignore') as source:
    for line in source:
      if(isFirst):
        isFirst = False
      else:
        fields = line.split('\t')
        fields[3] = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",fields[3]).split())).strip(" ")
        fields[3] = fields[3].replace("#", "")
        if(fields[1] == "1"):
            positive.append((fields[3],"positive"))
        else:
            negative.append((fields[3],"negative"))
        all.append(fields[3])

tweets = []
for (words, sentiment) in positive + negative:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

import random
import pickle
random.shuffle(tweets)
test_tweets = tweets[200000:]
#print(test_tweets)
tweets = tweets[:200000]

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    return wordlist

word_features = get_word_features(get_words_in_tweets(tweets))
print(len(word_features.keys()))
pickle.dump(word_features, open("features.p", "wb")) #REMEBER TO DO .KEYS()!!

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
