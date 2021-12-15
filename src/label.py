import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm

sia = SentimentIntensityAnalyzer()


data = csv.reader(open('./../data/cleaned_data.csv', 'r'))
new_data = [['reviews', 'cleaned_reviews', 'label']]


def normalize(s):
  if (s > .33):
    return 1
  elif (s < -.33):
    return -1
  else:
    return 0


for idx, each in tqdm(enumerate(data)):
  if idx == 0:
    continue
  review, cleaned = each
  ss = sia.polarity_scores(review)
  new_data.append([review, cleaned, normalize(ss['compound'])])

csv.writer(open('../data/cleaned_data_labeled.csv', 'w')).writerows(new_data)
