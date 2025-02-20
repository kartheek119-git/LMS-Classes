# -*- coding: utf-8 -*-
"""5-02-25

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TeVDfngqHmpOhkUI7U_ruU3w60WG4wpF
"""

import pandas as pd
dataset = pd.read_csv('/content/hate_speech.csv')
dataset.head()

dataset.shape

dataset.label.value_counts()

for index, tweet in enumerate(dataset["tweet"][10:15]):
    print(index+1,"-",tweet)

import re
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\']', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = text.lower()
    return text

dataset['clean_text'] = dataset.tweet.apply(lambda x: clean_text(x))

dataset.head(10)

from nltk.corpus import stopwords
len(stopwords.words('english'))

stop = stopwords.words('english')

stopwords = ["is", "an", "the", "to", "and", "in", "on", "at", "for", "with", "a", "of", "this", "that", "it", "by"]

#Generate word frequency
def gen_freq(text):
    word_list = []
    for tw_words in text.split():
        word_list.extend(tw_words)
    word_freq = pd.Series(word_list).value_counts()
    word_freq = word_freq.drop(stop, errors='ignore')
    return word_freq

#Check whether a negation term is present in the text
def any_neg(words):
    for word in words:
        if word in ['n', 'no', 'non', 'not'] or re.search(r"\wn't", word):
            return 1
        else:
            return 0

#Check whether one of the 100 rare words is present in the text
def any_rare(words, rare_100):
    for word in words:
        if word in rare_100:
            return 1
        else:
            return 0

#Check whether prompt words are present
def is_question(words):
    for word in words:
        if word in ['when', 'what', 'how', 'why', 'who', 'where']:
            return 1
        else:
            return 0

word_freq = gen_freq(dataset.clean_text.str)
rare_100 = word_freq[-100:] # last 100 rows/words
dataset['word_count'] = dataset.clean_text.str.split().apply(lambda x: len(x))
dataset['any_neg'] = dataset.clean_text.str.split().apply(lambda x: any_neg(x))
dataset['is_question'] = dataset.clean_text.str.split().apply(lambda x: is_question(x))
dataset['any_rare'] = dataset.clean_text.str.split().apply(lambda x: any_rare(x, rare_100))
dataset['char_count'] = dataset.clean_text.apply(lambda x: len(x))

