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
- text-classification
task_ids:
- sentiment-classification
pretty_name: TweetTopicSingle
---

# Dataset Card for "cardiffnlp/tweet_topic_multi"

## Dataset Description

- **Paper:** [https://arxiv.org/abs/2209.09824](https://arxiv.org/abs/2209.09824)
- **Dataset:** Tweet Topic Dataset
- **Domain:** Twitter
- **Number of Class:** 19


### Dataset Summary
This is the official repository of TweetTopic (["Twitter Topic Classification
, COLING main conference 2022"](https://arxiv.org/abs/2209.09824)), a topic classification dataset on Twitter with 19 labels.
Each instance of TweetTopic comes with a timestamp which distributes from September 2019 to August 2021.
See [cardiffnlp/tweet_topic_single](https://huggingface.co/datasets/cardiffnlp/tweet_topic_single) for single label version of TweetTopic.
The tweet collection used in TweetTopic is same as what used in [TweetNER7](https://huggingface.co/datasets/tner/tweetner7).
The dataset is integrated in [TweetNLP](https://tweetnlp.org/) too.

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

### Data Splits

| split                   | number of texts | description |
|:------------------------|-----:|------:|
| test_2020               |  573 | test dataset from September 2019 to August 2020 |
| test_2021               | 1679 | test dataset from September 2020 to August 2021 |
| train_2020              | 4585 | training dataset from September 2019 to August 2020 |
| train_2021              | 1505 | training dataset from September 2020 to August 2021 |
| train_all               | 6090 | combined training dataset of `train_2020` and `train_2021` |
| validation_2020         |  573 | validation dataset from September 2019 to August 2020 |
| validation_2021         |  188 | validation dataset from September 2020 to August 2021 | 
| train_random            | 4564 | randomly sampled training dataset with the same size as `train_2020` from `train_all` |
| validation_random       |  573 | randomly sampled training dataset with the same size as `validation_2020` from `validation_all` |
| test_coling2022_random  | 5536 | random split used in the COLING 2022 paper |
| train_coling2022_random | 5731 | random split used in the COLING 2022 paper |
| test_coling2022         | 5536 | temporal split used in the COLING 2022 paper |
| train_coling2022        | 5731 | temporal split used in the COLING 2022 paper |

For the temporal-shift setting, model should be trained on `train_2020` with `validation_2020` and evaluate on `test_2021`.
In general, model would be trained on `train_all`, the most representative training set with `validation_2021` and evaluate on `test_2021`.

**IMPORTANT NOTE:** To get a result that is comparable with the results of the COLING 2022 Tweet Topic paper, please use `train_coling2022` and `test_coling2022` for temporal-shift, and `train_coling2022_random` and `test_coling2022_random` fir random split (the coling2022 split does not have validation set).

### Models

| model                                                                                                                                                     | training data     |       F1 |   F1 (macro) |   Accuracy |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|---------:|-------------:|-----------:|
| [cardiffnlp/roberta-large-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/roberta-large-tweet-topic-multi-all)                                   | all (2020 + 2021) | 0.763104 |     0.620257 |   0.536629 |
| [cardiffnlp/roberta-base-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/roberta-base-tweet-topic-multi-all)                                     | all (2020 + 2021) | 0.751814 |     0.600782 |   0.531864 |
| [cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-multi-all)   | all (2020 + 2021) | 0.762513 |     0.603533 |   0.547945 |
| [cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-multi-all)     | all (2020 + 2021) | 0.759917 |     0.59901  |   0.536033 |
| [cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-all)     | all (2020 + 2021) | 0.764767 |     0.618702 |   0.548541 |
| [cardiffnlp/roberta-large-tweet-topic-multi-2020](https://huggingface.co/cardiffnlp/roberta-large-tweet-topic-multi-2020)                                 | 2020 only         | 0.732366 |     0.579456 |   0.493746 |
| [cardiffnlp/roberta-base-tweet-topic-multi-2020](https://huggingface.co/cardiffnlp/roberta-base-tweet-topic-multi-2020)                                   | 2020 only         | 0.725229 |     0.561261 |   0.499107 |
| [cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-multi-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-multi-2020) | 2020 only         | 0.73671  |     0.565624 |   0.513401 |
| [cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-multi-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-multi-2020)   | 2020 only         | 0.729446 |     0.534799 |   0.50268  |
| [cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-multi-2020)   | 2020 only         | 0.731106 |     0.532141 |   0.509827 |


Model fine-tuning script can be found [here](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multi/blob/main/lm_finetuning.py).

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```python
{
    "date": "2021-03-07",
    "text": "The latest The Movie theater Daily! {{URL}} Thanks to {{USERNAME}} {{USERNAME}} {{USERNAME}} #lunchtimeread #amc1000",
    "id": "1368464923370676231",
    "label": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "label_name": ["film_tv_&_video"]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/tweet_topic_multi/raw/main/dataset/label.multi.json).
```python
{
    "arts_&_culture": 0,
    "business_&_entrepreneurs": 1,
    "celebrity_&_pop_culture": 2,
    "diaries_&_daily_life": 3,
    "family": 4,
    "fashion_&_style": 5,
    "film_tv_&_video": 6,
    "fitness_&_health": 7,
    "food_&_dining": 8,
    "gaming": 9,
    "learning_&_educational": 10,
    "music": 11,
    "news_&_social_concern": 12,
    "other_hobbies": 13,
    "relationships": 14,
    "science_&_technology": 15,
    "sports": 16,
    "travel_&_adventure": 17,
    "youth_&_student_life": 18
 }
```


### Citation Information

```
@inproceedings{dimosthenis-etal-2022-twitter,
    title = "{T}witter {T}opic {C}lassification",
    author = "Antypas, Dimosthenis  and
    Ushio, Asahi  and
    Camacho-Collados, Jose  and
    Neves, Leonardo  and
    Silva, Vitor  and
    Barbieri, Francesco",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics"
}
```