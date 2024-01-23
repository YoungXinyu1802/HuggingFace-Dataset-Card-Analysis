---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
- crowdsourced
language:
- en
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-label-classification
---


# ****Dataset Card for English quotes****
# **I-Dataset Summary**
english_quotes is a dataset of all the quotes retrieved from [goodreads quotes](https://www.goodreads.com/quotes). This dataset can be used for multi-label text classification and text generation. The content of each quote is in English and concerns the domain of datasets for NLP and beyond.

# **II-Supported Tasks and Leaderboards**
- Multi-label text classification : The dataset can be used to train a model for text-classification, which consists of classifying quotes by author as well as by topic (using tags). Success on this task is typically measured by achieving a high or low accuracy.
- Text-generation : The dataset can be used to train a model to generate quotes by fine-tuning an existing pretrained model on the corpus composed of all quotes (or quotes by author).

# **III-Languages**
The texts in the dataset are in English (en).

# **IV-Dataset Structure**
#### Data Instances 
A JSON-formatted example of a typical instance in the dataset:
```python
{'author': 'Ralph Waldo Emerson',
 'quote': '“To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.”',
 'tags': ['accomplishment', 'be-yourself', 'conformity', 'individuality']}
  ```
 #### Data Fields
 - **author** : The author of the quote.
 - **quote** : The text of the quote.
 - **tags**:  The tags could be characterized as topics around the quote.
 
  #### Data Splits
I kept the dataset as one block (train), so it can be shuffled and split by users later using methods of the hugging face dataset library like the (.train_test_split()) method.

# **V-Dataset Creation**
#### Curation Rationale
I want to share my datasets (created by web scraping and additional cleaning treatments) with the HuggingFace community so that they can use them in NLP tasks to advance artificial intelligence.

#### Source Data
The source of Data is [goodreads](https://www.goodreads.com/?ref=nav_home) site: from [goodreads quotes](https://www.goodreads.com/quotes)

#### Initial Data Collection and Normalization 

The data collection process is web scraping using BeautifulSoup and Requests libraries.
The data is slightly modified after the web scraping: removing all quotes with "None" tags, and the tag "attributed-no-source" is removed from all tags, because it has not added value to the topic of the quote.

#### Who are the source Data producers ? 
The data is machine-generated (using web scraping) and subjected to human additional treatment. 

below, I provide the script I created to scrape the data (as well as my additional treatment):
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from collections import OrderedDict

page = requests.get('https://www.goodreads.com/quotes')
if page.status_code == 200:
    pageParsed = BeautifulSoup(page.content, 'html5lib')
    
# Define a function that retrieves information about each HTML quote code in a dictionary form.
def extract_data_quote(quote_html):
        quote = quote_html.find('div',{'class':'quoteText'}).get_text().strip().split('\n')[0]
        author = quote_html.find('span',{'class':'authorOrTitle'}).get_text().strip()
        if quote_html.find('div',{'class':'greyText smallText left'}) is not None:
            tags_list = [tag.get_text() for tag in quote_html.find('div',{'class':'greyText smallText left'}).find_all('a')]
            tags = list(OrderedDict.fromkeys(tags_list))
            if 'attributed-no-source' in tags:
                tags.remove('attributed-no-source')
        else:
            tags = None
        data = {'quote':quote, 'author':author, 'tags':tags}
        return data

# Define a function that retrieves all the quotes on a single page. 
def get_quotes_data(page_url):
    page = requests.get(page_url)
    if page.status_code == 200:
        pageParsed = BeautifulSoup(page.content, 'html5lib')
        quotes_html_page = pageParsed.find_all('div',{'class':'quoteDetails'})
        return [extract_data_quote(quote_html) for quote_html in quotes_html_page]

# Retrieve data from the first page.
data = get_quotes_data('https://www.goodreads.com/quotes')

# Retrieve data from all pages.
for i in range(2,101):
    print(i)
    url = f'https://www.goodreads.com/quotes?page={i}'
    data_current_page = get_quotes_data(url)
    if data_current_page is None:
        continue
    data = data + data_current_page

data_df = pd.DataFrame.from_dict(data)
for i, row in data_df.iterrows():
    if row['tags'] is None:
        data_df = data_df.drop(i)
# Produce the data in a JSON format.
data_df.to_json('C:/Users/Abir/Desktop/quotes.jsonl',orient="records", lines =True,force_ascii=False)
# Then I used the familiar process to push it to the Hugging Face hub.

```
#### Annotations 
Annotations are part of the initial data collection (see the script above).

# **VI-Additional Informations**
#### Dataset Curators
Abir ELTAIEF 


#### Licensing Information 
This work is licensed under a Creative Commons Attribution 4.0 International License (all software and libraries used for web scraping are made available under this Creative Commons Attribution license).

#### Contributions 
Thanks to [@Abirate](https://huggingface.co/Abirate)
 for adding this dataset. 