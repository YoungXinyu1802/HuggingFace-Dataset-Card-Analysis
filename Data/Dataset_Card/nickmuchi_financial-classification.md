---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
task_categories:
- text-classification
task_ids:
- multi-class-classification
- sentiment-classification
train-eval-index:
- config: sentences_50agree
- task: text-classification
- task_ids: multi_class_classification
- splits:
    eval_split: train
- col_mapping:
    sentence: text
    label: target
size_categories:
- 1K<n<10K
tags:
- finance
---

## Dataset Creation

 This [dataset](https://huggingface.co/datasets/nickmuchi/financial-classification) combines financial phrasebank dataset and a financial text dataset from [Kaggle](https://www.kaggle.com/datasets/percyzheng/sentiment-classification-selflabel-dataset). 

Given the financial phrasebank dataset does not have a validation split, I thought this might help to validate finance models and also capture the impact of COVID on financial earnings with the more recent Kaggle dataset.