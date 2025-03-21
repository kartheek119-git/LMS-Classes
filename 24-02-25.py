# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fedhZyzlCvx3N4unYHpy0Dm6kPnFTP1S
"""

import pandas as pd
import numpy as np
reviews_datasets = pd.read_csv("/content/Reviews.csv")
reviews_datasets = reviews_datasets.head(20000)
reviews_datasets.dropna()

reviews_datasets['Text'][350]

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = count_vect.fit_transform(reviews_datasets['Text'].values.astype('U'))

CountVectorizer?

print(doc_term_matrix)

from sklearn.decomposition import LatentDirichletAllocation
LDA = LatentDirichletAllocation(n_components=5, random_state=42)
LDA.fit(doc_term_matrix)

import random
for i in range(10):
    random_id = random.randint(0,len(count_vect.get_feature_names_out()))
    print(count_vect.get_feature_names_out()[random_id])

first_topic = LDA.components_[0] # topic 0

top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(count_vect.get_feature_names_out()[i])

for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([count_vect.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
    print('\n')

