---
language:
- en
dataset_info:
  splits:
  - name: test
    num_examples: 785
  - name: train
    num_examples: 4446
annotations_creators:
- expert-generated
license:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
pretty_name: financial_news_sentiment_mixte_with_phrasebank_75
size_categories:
- 1K<n<10K
tags: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
- sentiment-classification
---
# Dataset Card for "financial_news_sentiment_mixte_with_phrasebank_75"

This is a customized version of the phrasebank dataset in which I kept only sentences validated by at least 75% annotators.  
In addition I added ~2000 articles of Canadian news where sentiment was validated manually.

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


## References
Original dataset is available here:
[https://huggingface.co/datasets/financial_phrasebank]


