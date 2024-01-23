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
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
---
# Utilising Weak Supervision to Create S3D: A Sarcasm Annotated Dataset
This is the repository for the S3D dataset published at EMNLP 2022. The dataset can help build sarcasm detection models.

# SAD
The SAD dataset is our gold standard dataset of tweets labelled for sarcasm. These tweets were scraped by observing a '#sarcasm' hashtag and then manually annotated by three annotators.
There are a total of 1170 pairs of a sarcastic and non-sarcastic tweets which were both posted by the same user, resulting in a total of 2340 tweets annotated for sarcasm.
These tweets can be accessed by using the Twitter API so that they can be used for other experiments.

# Data Fields
- Tweet ID: The ID of the labelled tweet
- Label: A label to denote if a given tweet is sarcastic

# Data Splits
- Train: 1638
- Valid: 351
- Test: 351