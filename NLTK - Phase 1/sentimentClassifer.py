import nltk
import re


positive = []
negative = []
all = []
isFirst = True
#with open("sentimentData.txt",'r', encoding='utf-8', errors='ignore') as source:
with open("smallData.txt",'r', encoding='utf-8', errors='ignore') as source:
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
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# training_set = nltk.classify.apply_features(extract_features, tweets)
# print("ABOUT TO START TRAINING")
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# print("Finished")
# import pickle
# pickle.dump(classifier, open("classify.p", "wb"))
import pickle
classifier = pickle.load(open("classify.p","rb"))
print(classifier.show_most_informative_features(32))

#outputted positive, correct
corPos = 0
#outputted negative, correct
corNeg = 0
#outputted positive, incorrect
wrongPos = 0
#outputted negative, incorrect
wrongNeg = 0
count = 0
for item in test_tweets:
    count += 1
    #print(item)
    answer = classifier.classify(extract_features(item[0]))
    #print(answer)
    if(answer == "positive" and item[1] == "positive"):
        corPos += 1
    elif(answer == "positive"):
        wrongPos += 1
    elif(item[1] == "positive"):
        wrongNeg += 1
    else:
        corNeg += 1
    if(count % 1000 == 0):
        print(corPos, corNeg, wrongPos, wrongNeg)

answerOutput = open("answer.txt", "w")
answerOutput.write(str(corPos)+ " " + str(corNeg) + " " + str(wrongPos) + " " + str(wrongNeg))
