---
annotations_creators:
- Jordan Painter, Diptesh Kanojia
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: 'Utilising Weak Supervision to create S3D: A Sarcasm Annotated Dataset'
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
---

## Table of Contents
- [Dataset Description](#dataset-description)

- 
# Utilising Weak Supervision to Create S3D: A Sarcasm Annotated Dataset
This is the repository for the S3D dataset published at EMNLP 2022. The dataset can help build sarcasm detection models.

# S3D-v2 Summary
The S3D-v2 dataset is our silver standard dataset of 100,000 tweets labelled for sarcasm using weak supervision by a majority voting system of fine-tuned sarcasm detection models. The models used are 
our [roberta-large-finetuned-SARC-combined-DS](https://huggingface.co/surrey-nlp/roberta-large-finetuned-SARC-combined-DS), [bertweet-base-finetuned-SARC-DS](https://huggingface.co/surrey-nlp/bertweet-base-finetuned-SARC-DS)
and [bertweet-base-finetuned-SARC-combined-DS](https://huggingface.co/surrey-nlp/bertweet-base-finetuned-SARC-combined-DS) models.

S3D contains 13016 tweets labelled as sarcastic, and 86904 tweets labelled as not being sarcastic.

# Data Fields
- Text: The preprocessed tweet
- Label: A label to denote if a given tweet is sarcastic

# Data Splits
- Train: 70,000
- Valid: 15,000
- Test: 15,000