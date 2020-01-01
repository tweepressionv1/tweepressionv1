## Parts
This research broken down into three parts.
### Phase 1
The first is a Sentiment Classifier. Originally, this was attempted to be solved using a Naive Bayes Classifier, but then was improved using a Keras Dense Neural Network.
### Phase 2
The second part is an SVM, or Support Vector Machine. Using the sentiment's classified by the given Phase 1, this phase 2 process gives a final output probability on a scale of 0 to 1 of how likely the user is to have Major Depressive Disorder. 
### Phase 3
Phase 3 is the web framework. Our site is located at tweepression.com (Maybe down due to bug fixes and improvements)
### NEW Phase 4
Phase 4 is the Convolutional Neural Network. This network classifies fMRI data for an extension on the original tweepression platform. 
## Dependencies
### Installation
This Project uses Python 2.6 as well as 3.7, due to differing circumstances in servers that we used to train the network. Both are compatible, however a certian amount of frameworks are required.
* [Keras](https://keras.io/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](http://www.numpy.org/)
* [Scikit-Learn](http://scikit-learn.org/stable/)
* [Matplotlib](https://matplotlib.org/)
* [NLTK](http://www.nltk.org/)
### Datasets
It is highly reccomended to be done using an Ubuntu Server if there is a need to replicate. If the DNN wants to be replciated and re-trained for better accuracy, the Google Word2Vec dataset is required, and can be found [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)

The Twitter NLTK Naive Bayes Classifer was trained on a set of around 1.5 Million Tweets with marked sentiment values. There are many ways of obtaining similar datasets, and a quick google search of "twitter sentiment corups/dataset" will provide a sufficient dataset. 

## Acknowledgements
* The "Bag of Words Meets Bag of Popcorn" kaggle competition for it's inspiration to use a Bag of Words Approach for the Sentiment Analysis Problem
* [TJHSST CSL](https://tjhsst.fcps.edu/) for it's use of the computer system's lab
