---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1k<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: TweetNER7
---

# Dataset Card for "tner/tweetner7"

## Dataset Description

- **Repository:** [https://github.com/asahi417/tner/tree/master/examples/tweetner7_paper](https://github.com/asahi417/tner/tree/master/examples/tweetner7_paper)
- **Paper:** [https://arxiv.org/abs/2210.03797](https://arxiv.org/abs/2210.03797)
- **Dataset:** TweetNER7
- **Domain:** Twitter
- **Number of Entity:** 7


### Dataset Summary
This is the official repository of TweetNER7 (["Named Entity Recognition in Twitter:
A Dataset and Analysis on Short-Term Temporal Shifts, AACL main conference 2022"](https://arxiv.org/abs/2210.03797)), an NER dataset on Twitter with 7 entity labels. Each instance of TweetNER7 comes with a timestamp which distributes from September 2019 to August 2021.
The tweet collection used in TweetNER7 is same as what used in [TweetTopic](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multi).
The dataset is integrated in [TweetNLP](https://tweetnlp.org/) too.
- Entity Types: `corperation`, `creative_work`, `event`, `group`, `location`, `product`, `person` 

### Preprocessing
We pre-process tweets before the annotation to normalize some artifacts, converting URLs into a special token `{{URL}}` and non-verified usernames into `{{USERNAME}}`.
For verified usernames, we replace its display name (or account name) with symbols `{@}`.
For example, a tweet

```
Get the all-analog Classic Vinyl Edition
of "Takin' Off" Album from @herbiehancock
via @bluenoterecords link below: 
http://bluenote.lnk.to/AlbumOfTheWeek
```

is transformed into the following text.
```
Get the all-analog Classic Vinyl Edition
of "Takin' Off" Album from {@herbiehancock@}
via {@bluenoterecords@} link below: {{URL}}
```

A simple function to format tweet follows below.

```python
import re
from urlextract import URLExtract
extractor = URLExtract()

def format_tweet(tweet):
    # mask web urls
    urls = extractor.find_urls(tweet)
    for url in urls:
        tweet = tweet.replace(url, "{{URL}}")
    # format twitter account
    tweet = re.sub(r"\b(\s*)(@[\S]+)\b", r'\1{\2@}', tweet)
    return tweet

target = """Get the all-analog Classic Vinyl Edition of "Takin' Off" Album from @herbiehancock via @bluenoterecords link below: http://bluenote.lnk.to/AlbumOfTheWeek"""
target_format = format_tweet(target)
print(target_format)
'Get the all-analog Classic Vinyl Edition of "Takin\' Off" Album from {@herbiehancock@} via {@bluenoterecords@} link below: {{URL}}'
```


We ask annotators to ignore those special tokens but label the verified users' mentions.


### Data Split

| split             | number of instances | description |
|:------------------|------:|------:|
| train_2020        |  4616 | training dataset from September 2019 to August 2020 |
| train_2021        |  2495 | training dataset from September 2020 to August 2021 |
| train_all         |  7111 | combined training dataset of `train_2020` and `train_2021` |
| validation_2020   |   576 | validation dataset from September 2019 to August 2020 |
| validation_2021   |   310 | validation dataset from September 2020 to August 2021 | 
| test_2020         |   576 | test dataset from September 2019 to August 2020 |
| test_2021         |  2807 | test dataset from September 2020 to August 2021 |
| train_random      |  4616 | randomly sampled training dataset with the same size as `train_2020` from `train_all` |
| validation_random |   576 | randomly sampled training dataset with the same size as `validation_2020` from `validation_all` |
| extra_2020        | 87880 | extra tweet without annotations from September 2019 to August 2020 |
| extra_2021        | 93594 | extra tweet without annotations from September 2020 to August 2021 |

For the temporal-shift setting, model should be trained on `train_2020` with `validation_2020` and evaluate on `test_2021`.
In general, model would be trained on `train_all`, the most representative training set with `validation_2021` and evaluate on `test_2021`.

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```
{
    'tokens': ['Morning', '5km', 'run', 'with', '{{USERNAME}}', 'for', 'breast', 'cancer', 'awareness', '#', 'pinkoctober', '#', 'breastcancerawareness', '#', 'zalorafit', '#', 'zalorafitxbnwrc', '@', 'The', 'Central', 'Park', ',', 'Desa', 'Parkcity', '{{URL}}'],
    'tags': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 2, 14, 2, 14, 14, 14, 14, 14, 14, 4, 11, 11, 11, 11, 14],
    'id': '1183344337016381440',
    'date': '2019-10-13'
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/tweetner7/raw/main/dataset/label.json).
```python
{
    "B-corporation": 0,
    "B-creative_work": 1,
    "B-event": 2,
    "B-group": 3,
    "B-location": 4,
    "B-person": 5,
    "B-product": 6,
    "I-corporation": 7,
    "I-creative_work": 8,
    "I-event": 9,
    "I-group": 10,
    "I-location": 11,
    "I-person": 12,
    "I-product": 13,
    "O": 14
}
```


## Models
See full evaluation metrics [here](https://github.com/asahi417/tner/blob/master/MODEL_CARD.md#models-for-tweetner7).

### Main Models

| Model (link)                                                                                                                                | Data                                                          | Language Model                                                                                                                                      |   Micro F1 (2021) |   Macro F1 (2021) |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|------------------:|------------------:|
| [`tner/roberta-large-tweetner7-all`](https://huggingface.co/tner/roberta-large-tweetner7-all)                                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large)                                                                                             |             65.75 |             61.25 |
| [`tner/roberta-base-tweetner7-all`](https://huggingface.co/tner/roberta-base-tweetner7-all)                                                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-base`](https://huggingface.co/roberta-base)                                                                                               |             65.16 |             60.81 |
| [`tner/twitter-roberta-base-2019-90m-tweetner7-all`](https://huggingface.co/tner/twitter-roberta-base-2019-90m-tweetner7-all)               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-2019-90m`](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m)                                       |             65.68 |             61    |
| [`tner/twitter-roberta-base-dec2020-tweetner7-all`](https://huggingface.co/tner/twitter-roberta-base-dec2020-tweetner7-all)                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2020`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020)                                         |             65.26 |             60.7  |
| [`tner/bertweet-large-tweetner7-all`](https://huggingface.co/tner/bertweet-large-tweetner7-all)                                             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large) |             66.46 |             61.87 |
| [`tner/bertweet-base-tweetner7-all`](https://huggingface.co/tner/bertweet-base-tweetner7-all)                                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`vinai/bertweet-base`](https://huggingface.co/vinai/bertweet-base)                                                                                 |             65.36 |             60.52 |
| [`tner/bert-large-tweetner7-all`](https://huggingface.co/tner/bert-large-tweetner7-all)                                                     | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-large`](https://huggingface.co/bert-large)                                                                                                   |             63.58 |             59    |
| [`tner/bert-base-tweetner7-all`](https://huggingface.co/tner/bert-base-tweetner7-all)                                                       | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-base`](https://huggingface.co/bert-base)                                                                                                     |             62.3  |             57.59 |
| [`tner/roberta-large-tweetner7-continuous`](https://huggingface.co/tner/roberta-large-tweetner7-continuous)                                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large)                                                                                             |             66.02 |             60.9  |
| [`tner/roberta-base-tweetner7-continuous`](https://huggingface.co/tner/roberta-base-tweetner7-continuous)                                   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-base`](https://huggingface.co/roberta-base)                                                                                               |             65.47 |             60.01 |
| [`tner/twitter-roberta-base-2019-90m-tweetner7-continuous`](https://huggingface.co/tner/twitter-roberta-base-2019-90m-tweetner7-continuous) | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-2019-90m`](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m)                                       |             65.87 |             61.07 |
| [`tner/twitter-roberta-base-dec2020-tweetner7-continuous`](https://huggingface.co/tner/twitter-roberta-base-dec2020-tweetner7-continuous)   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2020`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020)                                         |             65.51 |             60.57 |
| [`tner/bertweet-large-tweetner7-continuous`](https://huggingface.co/tner/bertweet-large-tweetner7-continuous)                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large) |             66.41 |             61.66 |
| [`tner/bertweet-base-tweetner7-continuous`](https://huggingface.co/tner/bertweet-base-tweetner7-continuous)                                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`vinai/bertweet-base`](https://huggingface.co/vinai/bertweet-base)                                                                                 |             65.84 |             61.02 |
| [`tner/bert-large-tweetner7-continuous`](https://huggingface.co/tner/bert-large-tweetner7-continuous)                                       | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-large`](https://huggingface.co/bert-large)                                                                                                   |             63.2  |             57.67 |
| [`tner/roberta-large-tweetner7-2021`](https://huggingface.co/tner/roberta-large-tweetner7-2021)                                             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large)                                                                                             |             64.05 |             59.11 |
| [`tner/roberta-base-tweetner7-2021`](https://huggingface.co/tner/roberta-base-tweetner7-2021)                                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-base`](https://huggingface.co/roberta-base)                                                                                               |             61.76 |             57    |
| [`tner/twitter-roberta-base-dec2020-tweetner7-2021`](https://huggingface.co/tner/twitter-roberta-base-dec2020-tweetner7-2021)               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2020`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020)                                         |             63.98 |             58.91 |
| [`tner/bertweet-large-tweetner7-2021`](https://huggingface.co/tner/bertweet-large-tweetner7-2021)                                           | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large) |             62.9  |             58.13 |
| [`tner/bertweet-base-tweetner7-2021`](https://huggingface.co/tner/bertweet-base-tweetner7-2021)                                             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`vinai/bertweet-base`](https://huggingface.co/vinai/bertweet-base)                                                                                 |             63.09 |             57.35 |
| [`tner/bert-large-tweetner7-2021`](https://huggingface.co/tner/bert-large-tweetner7-2021)                                                   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-large`](https://huggingface.co/bert-large)                                                                                                   |             59.75 |             53.93 |
| [`tner/bert-base-tweetner7-2021`](https://huggingface.co/tner/bert-base-tweetner7-2021)                                                     | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-base`](https://huggingface.co/bert-base)                                                                                                     |             60.67 |             55.5  |
| [`tner/roberta-large-tweetner7-2020`](https://huggingface.co/tner/roberta-large-tweetner7-2020)                                             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large)                                                                                             |             64.76 |             60    |
| [`tner/roberta-base-tweetner7-2020`](https://huggingface.co/tner/roberta-base-tweetner7-2020)                                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-base`](https://huggingface.co/roberta-base)                                                                                               |             64.21 |             59.11 |
| [`tner/twitter-roberta-base-2019-90m-tweetner7-2020`](https://huggingface.co/tner/twitter-roberta-base-2019-90m-tweetner7-2020)             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-2019-90m`](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m)                                       |             64.28 |             59.31 |
| [`tner/twitter-roberta-base-dec2020-tweetner7-2020`](https://huggingface.co/tner/twitter-roberta-base-dec2020-tweetner7-2020)               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2020`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020)                                         |             62.87 |             58.26 |
| [`tner/bertweet-large-tweetner7-2020`](https://huggingface.co/tner/bertweet-large-tweetner7-2020)                                           | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large) |             64.01 |             59.47 |
| [`tner/bertweet-base-tweetner7-2020`](https://huggingface.co/tner/bertweet-base-tweetner7-2020)                                             | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`vinai/bertweet-base`](https://huggingface.co/vinai/bertweet-base)                                                                                 |             64.06 |             59.44 |
| [`tner/bert-large-tweetner7-2020`](https://huggingface.co/tner/bert-large-tweetner7-2020)                                                   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-large`](https://huggingface.co/bert-large)                                                                                                   |             61.43 |             56.14 |
| [`tner/bert-base-tweetner7-2020`](https://huggingface.co/tner/bert-base-tweetner7-2020)                                                     | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-base`](https://huggingface.co/bert-base)                                                                                                     |             60.09 |             54.67 |

Model description follows below.
* Model with suffix `-all`: Model fine-tuned on `train_all` and validated on `validation_2021`.
* Model with suffix `-continuous`: Model fine-tuned on `train_2021` continuously after fine-tuning on `train_2020` and validated on `validation_2021`.
* Model with suffix `-2021`: Model fine-tuned only on `train_2021` and validated on `validation_2021`. 
* Model with suffix `-2020`:  Model fine-tuned only on `train_2021` and validated on `validation_2020`.


### Sub Models (used in ablation study)

- Model fine-tuned only on `train_random` and validated on `validation_2020`.

| Model (link)                                                                                                                        | Data                                                          | Language Model                                                                                                                                      |   Micro F1 (2021) |   Macro F1 (2021) |
|:------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|------------------:|------------------:|
| [`tner/roberta-large-tweetner7-random`](https://huggingface.co/tner/roberta-large-tweetner7-random)                                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large)                                                                                             |             66.33 |             60.96 |
| [`tner/twitter-roberta-base-2019-90m-tweetner7-random`](https://huggingface.co/tner/twitter-roberta-base-2019-90m-tweetner7-random) | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-2019-90m`](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m)                                       |             63.29 |             58.5  |
| [`tner/roberta-base-tweetner7-random`](https://huggingface.co/tner/roberta-base-tweetner7-random)                                   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-base`](https://huggingface.co/roberta-base)                                                                                               |             64.04 |             59.23 |
| [`tner/twitter-roberta-base-dec2020-tweetner7-random`](https://huggingface.co/tner/twitter-roberta-base-dec2020-tweetner7-random)   | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2020`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020)                                         |             64.72 |             59.97 |
| [`tner/bertweet-large-tweetner7-random`](https://huggingface.co/tner/bertweet-large-tweetner7-random)                               | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large`](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021vinai/bertweet-large) |             64.86 |             60.49 |
| [`tner/bertweet-base-tweetner7-random`](https://huggingface.co/tner/bertweet-base-tweetner7-random)                                 | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`vinai/bertweet-base`](https://huggingface.co/vinai/bertweet-base)                                                                                 |             65.55 |             59.58 |
| [`tner/bert-large-tweetner7-random`](https://huggingface.co/tner/bert-large-tweetner7-random)                                       | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-large`](https://huggingface.co/bert-large)                                                                                                   |             62.39 |             57.54 |
| [`tner/bert-base-tweetner7-random`](https://huggingface.co/tner/bert-base-tweetner7-random)                                         | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`bert-base`](https://huggingface.co/bert-base)                                                                                                     |             60.91 |             55.92 |

- Model fine-tuned on the self-labeled dataset on `extra_{2020,2021}` and validated on `validation_2020`.

| Model (link)                                                                                                                            | Data                                                          | Language Model                                          |   Micro F1 (2021) |   Macro F1 (2021) |
|:----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|:--------------------------------------------------------|------------------:|------------------:|
| [`tner/roberta-large-tweetner7-selflabel2020`](https://huggingface.co/tner/roberta-large-tweetner7-selflabel2020)                       | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             64.56 |             59.63 |
| [`tner/roberta-large-tweetner7-selflabel2021`](https://huggingface.co/tner/roberta-large-tweetner7-selflabel2021)                       | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             64.6  |             59.45 |
| [`tner/roberta-large-tweetner7-2020-selflabel2020-all`](https://huggingface.co/tner/roberta-large-tweetner7-2020-selflabel2020-all)     | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             65.46 |             60.39 |
| [`tner/roberta-large-tweetner7-2020-selflabel2021-all`](https://huggingface.co/tner/roberta-large-tweetner7-2020-selflabel2021-all)     | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             64.52 |             59.45 |
| [`tner/roberta-large-tweetner7-selflabel2020-continuous`](https://huggingface.co/tner/roberta-large-tweetner7-selflabel2020-continuous) | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             65.15 |             60.23 |
| [`tner/roberta-large-tweetner7-selflabel2021-continuous`](https://huggingface.co/tner/roberta-large-tweetner7-selflabel2021-continuous) | [`tweetner7`](https://huggingface.co/datasets/tner/tweetner7) | [`roberta-large`](https://huggingface.co/roberta-large) |             64.48 |             59.41 |


Model description follows below.
* Model with suffix `-self2020`: Fine-tuning on the self-annotated data of `extra_2020` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7).           
* Model with suffix `-self2021`: Fine-tuning on the self-annotated data of `extra_2021` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7).                                                              
* Model with suffix `-2020-self2020-all`: Fine-tuning on the self-annotated data of `extra_2020` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7). Combined training dataset of `extra_2020` and `train_2020`.  
* Model with suffix `-2020-self2021-all`: Fine-tuning on the self-annotated data of `extra_2021` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7). Combined training dataset of `extra_2021` and `train_2020`.  
* Model with suffix `-2020-self2020-continuous`: Fine-tuning on the self-annotated data of `extra_2020` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7). Fine-tuning on `train_2020` and continuing fine-tuning on `extra_2020`. 
* Model with suffix `-2020-self2021-continuous`: Fine-tuning on the self-annotated data of `extra_2021` split of [tweetner7](https://huggingface.co/datasets/tner/tweetner7). Fine-tuning on `train_2020` and continuing fine-tuning on `extra_2020`. 

### Reproduce Experimental Result

To reproduce the experimental result on our AACL paper, please see the repository 
[https://github.com/asahi417/tner/tree/master/examples/tweetner7_paper](https://github.com/asahi417/tner/tree/master/examples/tweetner7_paper).


## Citation Information

```
@inproceedings{ushio-etal-2022-tweet,
    title = "{N}amed {E}ntity {R}ecognition in {T}witter: {A} {D}ataset and {A}nalysis on {S}hort-{T}erm {T}emporal {S}hifts",
    author = "Ushio, Asahi  and
        Neves, Leonardo  and
        Silva, Vitor  and
        Barbieri, Francesco. and
        Camacho-Collados, Jose",
    booktitle = "The 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing",
    month = nov,
    year = "2022",
    address = "Online",
    publisher = "Association for Computational Linguistics",
}
```
