---
language:
- en
dataset_info:
  splits:
  - name: test
    num_examples: 267
  - name: train
    num_examples: 1512
annotations_creators:
- expert-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: financial_news_sentiment
size_categories:
- 1K<n<10K
tags: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
- sentiment-classification
---
# Dataset Card for "financial_news_sentiment"

Manually validated sentiment for ~2000 Canadian news articles.

The dataset also include a column topic which contains one of the following value:
* acquisition
* other
* quaterly financial release
* appointment to new position
* dividend
* corporate update
* drillings results
* conference
* share repurchase program
* grant of stocks

This was generated automatically using a zero-shot classification model and **was not** reviewed manually.