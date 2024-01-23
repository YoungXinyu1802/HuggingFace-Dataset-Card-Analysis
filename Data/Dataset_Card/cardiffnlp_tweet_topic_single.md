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

# Dataset Card for "cardiffnlp/tweet_topic_single"

## Dataset Description

- **Paper:** [https://arxiv.org/abs/2209.09824](https://arxiv.org/abs/2209.09824)
- **Dataset:** Tweet Topic Dataset
- **Domain:** Twitter
- **Number of Class:** 6


### Dataset Summary
This is the official repository of TweetTopic (["Twitter Topic Classification
, COLING main conference 2022"](https://arxiv.org/abs/2209.09824)), a topic classification dataset on Twitter with 6 labels.
Each instance of TweetTopic comes with a timestamp which distributes from September 2019 to August 2021.
See [cardiffnlp/tweet_topic_multi](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multi) for multi label version of TweetTopic.
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
| test_2020               |  376 | test dataset from September 2019 to August 2020 |
| test_2021               | 1693 | test dataset from September 2020 to August 2021 |
| train_2020              | 2858 | training dataset from September 2019 to August 2020 |
| train_2021              | 1516 | training dataset from September 2020 to August 2021 |
| train_all               | 4374 | combined training dataset of `train_2020` and `train_2021` |
| validation_2020         |  352 | validation dataset from September 2019 to August 2020 |
| validation_2021         |  189 | validation dataset from September 2020 to August 2021 | 
| train_random            | 2830 | randomly sampled training dataset with the same size as `train_2020` from `train_all` |
| validation_random       |  354 | randomly sampled training dataset with the same size as `validation_2020` from `validation_all` |
| test_coling2022_random  | 3399 | random split used in the COLING 2022 paper |
| train_coling2022_random | 3598 | random split used in the COLING 2022 paper |
| test_coling2022         | 3399 | temporal split used in the COLING 2022 paper |
| train_coling2022        | 3598 | temporal split used in the COLING 2022 paper |

For the temporal-shift setting, model should be trained on `train_2020` with `validation_2020` and evaluate on `test_2021`.
In general, model would be trained on `train_all`, the most representative training set with `validation_2021` and evaluate on `test_2021`.

**IMPORTANT NOTE:** To get a result that is comparable with the results of the COLING 2022 Tweet Topic paper, please use `train_coling2022` and `test_coling2022` for temporal-shift, and `train_coling2022_random` and `test_coling2022_random` fir random split (the coling2022 split does not have validation set).

### Models

| model                                                                                                                                                       | training data     |       F1 |   F1 (macro) |   Accuracy |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|---------:|-------------:|-----------:|
| [cardiffnlp/roberta-large-tweet-topic-single-all](https://huggingface.co/cardiffnlp/roberta-large-tweet-topic-single-all)                                   | all (2020 + 2021) | 0.896043 |     0.800061 |   0.896043 |
| [cardiffnlp/roberta-base-tweet-topic-single-all](https://huggingface.co/cardiffnlp/roberta-base-tweet-topic-single-all)                                     | all (2020 + 2021) | 0.887773 |     0.79793  |   0.887773 |
| [cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-single-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-single-all)   | all (2020 + 2021) | 0.892499 |     0.774494 |   0.892499 |
| [cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-single-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-single-all)     | all (2020 + 2021) | 0.890136 |     0.776025 |   0.890136 |
| [cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-single-all](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-single-all)     | all (2020 + 2021) | 0.894861 |     0.800952 |   0.894861 |
| [cardiffnlp/roberta-large-tweet-topic-single-2020](https://huggingface.co/cardiffnlp/roberta-large-tweet-topic-single-2020)                                 | 2020 only         | 0.878913 |     0.70565  |   0.878913 |
| [cardiffnlp/roberta-base-tweet-topic-single-2020](https://huggingface.co/cardiffnlp/roberta-base-tweet-topic-single-2020)                                   | 2020 only         | 0.868281 |     0.729667 |   0.868281 |
| [cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-single-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-2019-90m-tweet-topic-single-2020) | 2020 only         | 0.882457 |     0.740187 |   0.882457 |
| [cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-single-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2020-tweet-topic-single-2020)   | 2020 only         | 0.87596  |     0.746275 |   0.87596  |
| [cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-single-2020](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021-tweet-topic-single-2020)   | 2020 only         | 0.877732 |     0.746119 |   0.877732 |

Model fine-tuning script can be found [here](https://huggingface.co/datasets/cardiffnlp/tweet_topic_single/blob/main/lm_finetuning.py).

## Dataset Structure

### Data Instances
An example of `train` looks as follows.

```python
{
    "text": "Game day for {{USERNAME}} U18\u2019s against {{USERNAME}} U18\u2019s. Even though it\u2019s a \u2018home\u2019 game for the people that have settled in Mid Wales it\u2019s still a 4 hour round trip for us up to Colwyn Bay. Still enjoy it though!",
    "date": "2019-09-08",
    "label": 4,
    "id": "1170606779568463874",
    "label_name": "sports_&_gaming"
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/tweet_topic_single/raw/main/dataset/label.single.json).
```python
{
    "arts_&_culture": 0,
    "business_&_entrepreneurs": 1,
    "pop_culture": 2,
    "daily_life": 3,
    "sports_&_gaming": 4,
    "science_&_technology": 5
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