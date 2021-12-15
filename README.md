## Sentiment analysis of Daraz Product Reviews
Note: This is my first ML Project, so I am not very good at it.
### Introduction
Daraz is the leading online marketplace in South Asia, empowering tens of thousands of sellers to connect with millions of customers. Daraz provides immediate and easy access to 22 million products in 100+ categories to deliver more than 2 million packages every month to all corners of the country.

There are thousands of reviews for thousands of products on Daraz right now. In this project, we scrapped 27000+ reviews from Daraz for various products of the same category to find out the sentiments of the users about the category. We performed sentimental analysis by using a Multi-Layer perceptron and found the results summarized in this report. 

We were assigned the “Babies & Toys” category, but this repo contains reviews of all the categories.

### Methodology and Outcomes
We achieved this project by following these steps:
- Data Scraping using Reverse Engineering
- Data cleaning through pre-trained models
- Labeling the data
- Data Transformation
- Training the Data
- Results

#### Data Scraping using Reverse Engineering 
We set ourselves to collect over 4000 reviews in our category. Traditional web scraping is an essential tool for automatically downloading data from pages of the web. But, In the modern world. Data travels mostly over a REST API. We reversed Daraz’s REST API to scrap/download reviews with much faster speeds. 

##### Getting Product List
First, we grabbed our category’s subcategory URLs. From the request patterns seen in the Network Panel of Chrome. We discovered `?ajax=true` query tag. When we place this query tag after our’s subcategory’s URL. Daraz sends back JSON containing the products of the category. 
```
e.g, https://www.daraz.pk/baby-toddler-diapers-potties/?ajax=true
```
This JSON contains product IDs (`itemId`).

##### Getting Review List

We got our reviews in JSON by requesting the following URL.

```
https://my.daraz.pk/pdp/review/getReviewList?itemId={item_id}&pageSize={page_size}&filter=0&sort=0&pageNo={page_no}
```

Here,  
- **item_id**: This refers to unique identifier of the Product we want reviews for. We know this from above.
- **page_size**: The number of reviews we want to get received in one request. 
- **page_no**: The page number of the reviews, we don’t need this as we will be getting all the reviews in one go.

Please refer to `src/sraping.py` in the attached resources. The row data is available at `data/scrapped_data.csv`

#### Data cleaning through pre-trained models
We set out to only deal with only English reviews. We needed to filter reviews only English reviews from the scrapped data. Note that scrapper also performs a language check before it downloads a review but it’s based on a small model which is not very accurate. For performance reasons, we didn’t add a bigger model at the scrapping level.

We cleaned the data following these steps:
- Cleaning text and removing punctuation, emojis, replacing extra spaces and newlines with a single space, and anything that is not an alphanumeric character with space.
- Removed non-English reviews by using `spacy-langdetect` [1]
- Fixed spelling mistakes using the amazing neuspell’s `BertChecker`. [2]
- Removed stopwords using nltk’s `stopwords` dataset. [3]
- Performed lemmatization using spacy’s `lemmatizer`. 

Cleaned data (unlabeled) is available at `data/cleaned_data.csv`.
#### Labeling the data
The data was labeled by nltk’s `SentimentIntensityAnalyzer`.
#### Data transformation 
scikit-learn’s `CountVectorizer` [4] was used for extracting features from our review text. We are using a limit of 1000 features.
#### Training Multi-Layer Perceptron Classifier
We split our data into 80% training data and 20% data. We used the MLPClassifier from scikit-learn and trained it with our dataset. 





