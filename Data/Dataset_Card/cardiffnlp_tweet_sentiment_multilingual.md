---
language:
- en
- ar
- fr
- de
- hi
- it
- pt
- es
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-tweet-datasets
task_categories:
- text-classification
task_ids:
- sentiment-classification
paperswithcode_id: tweet_sentiment_multilingual
pretty_name: Tweet Sentiment Multilingual
train-eval-index:
- config: sentiment
  task: text-classification
  task_id: multi_class_classification
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    text: text
    label: target
  metrics:
  - type: accuracy
    name: Accuracy
  - type: f1
    name: F1 macro
    args:
      average: macro
  - type: f1
    name: F1 micro
    args:
      average: micro
  - type: f1
    name: F1 weighted
    args:
      average: weighted
  - type: precision
    name: Precision macro
    args:
      average: macro
  - type: precision
    name: Precision micro
    args:
      average: micro
  - type: precision
    name: Precision weighted
    args:
      average: weighted
  - type: recall
    name: Recall macro
    args:
      average: macro
  - type: recall
    name: Recall micro
    args:
      average: micro
  - type: recall
    name: Recall weighted
    args:
      average: weighted
configs:
- arabic
- english
- french
- german
- hindi
- italian
- portuguese
- spanish
dataset_info:
- config_name: sentiment
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          0: negative
          1: neutral
          2: positive
---

# Dataset Card for cardiffnlp/tweet_sentiment_multilingual

## Dataset Description

- **Homepage:** [https://github.com/cardiffnlp/xlm-t](https://github.com/cardiffnlp/xlm-t)
- **Repository:** - **Homepage:** [https://github.com/cardiffnlp/xlm-t](https://github.com/cardiffnlp/xlm-t)
- **Paper:** [https://aclanthology.org/2022.lrec-1.27/](https://aclanthology.org/2022.lrec-1.27/)
- **Point of Contact:** [Asahi Ushio](https://asahiushio.com/)

### Dataset Summary

Tweet Sentiment Multilingual consists of sentiment analysis dataset on Twitter in 8 different lagnuages.

- arabic
- english
- french
- german
- hindi
- italian
- portuguese
- spanish

### Supported Tasks and Leaderboards

- `text_classification`: The dataset can be trained using a SentenceClassification model from HuggingFace transformers.

## Dataset Structure

### Data Instances

An instance from `sentiment` config:

```
{'label': 2, 'text': '"QT @user In the original draft of the 7th book, Remus Lupin survived the Battle of Hogwarts. #HappyBirthdayRemusLupin"'}
```

### Data Fields

For `sentiment` config:

- `text`: a `string` feature containing the tweet.

- `label`: an `int` classification label with the following mapping:

    `0`: negative

    `1`: neutral

    `2`: positive


### Data Splits


- arabic
- english
- french
- german
- hindi
- italian
- portuguese
- spanish

| name            | train | validation | test  |
| --------------- | ----- | ---------- | ----- |
| arabic          | 1838  | 323        | 869   |
| english         | 1838  | 323        | 869   |
| french          | 1838  | 323        | 869   |
| german          | 1838  | 323        | 869   |
| hindi           | 1838  | 323        | 869   |
| italian         | 1838  | 323        | 869   |
| portuguese      | 1838  | 323        | 869   |
| spanish         | 1838  | 323        | 869   |

### Dataset Curators

Francesco Barbieri, Jose Camacho-Collados, Luis Espiinosa-Anke and Leonardo Neves through Cardiff NLP.

### Licensing Information

[Creative Commons Attribution 3.0 Unported License](https://groups.google.com/g/semevaltweet/c/k5DDcvVb_Vo/m/zEOdECFyBQAJ), and all of the datasets require complying with Twitter [Terms Of Service](https://twitter.com/tos) and Twitter API [Terms Of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy)


### Citation Information

```
@inproceedings{barbieri-etal-2022-xlm,
    title = "{XLM}-{T}: Multilingual Language Models in {T}witter for Sentiment Analysis and Beyond",
    author = "Barbieri, Francesco  and
      Espinosa Anke, Luis  and
      Camacho-Collados, Jose",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.27",
    pages = "258--266",
    abstract = "Language models are ubiquitous in current NLP, and their multilingual capacity has recently attracted considerable attention. However, current analyses have almost exclusively focused on (multilingual variants of) standard benchmarks, and have relied on clean pre-training and task-specific corpora as multilingual signals. In this paper, we introduce XLM-T, a model to train and evaluate multilingual language models in Twitter. In this paper we provide: (1) a new strong multilingual baseline consisting of an XLM-R (Conneau et al. 2020) model pre-trained on millions of tweets in over thirty languages, alongside starter code to subsequently fine-tune on a target task; and (2) a set of unified sentiment analysis Twitter datasets in eight different languages and a XLM-T model trained on this dataset.",
}
```

