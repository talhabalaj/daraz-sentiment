import csv
import json
from glob import glob
import re
import importlib
# from nltk.sentiment import SentimentIntensityAnalyzer
# from nltk import download as nltk_download

# nltk_download('vader_lexicon')
# sia = SentimentIntensityAnalyzer()

import configuration as config


def clean_text(text):
  text = re.sub(r'\n', ' ', text)
  text = re.sub(r'[^\w\s]', ' ', text)
  text = re.sub(r'\s+', ' ', text)
  text = text.lower()
  return text


data = []

file = open(f'scrapped_{config.data_dir}.csv', 'w')
c = 0
t = 0

file.write('reviews\n')

reviews = []
all_reviews_json = []

print('Loading reviews...')
for each in glob(f'{config.data_dir}/*.json'):
  with open(each, 'r') as f:
    product_reviews = json.load(f)
    for review in product_reviews:
      all_reviews_json.append(review)

all_reviews_json_len = len(all_reviews_json)

print('Processing JSON')
for review in all_reviews_json:
  text = review['reviewContent']
  reviews.append([text])
  print(f'{c}/{all_reviews_json_len}', end='\r')


csv.writer(file).writerows(reviews)
