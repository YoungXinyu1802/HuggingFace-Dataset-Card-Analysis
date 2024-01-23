---
language:
- en
language_creators:
- found
license: unknown
multilinguality:
- monolingual
pretty_name: Blue
size_categories:
- 10K<n<100K
source_datasets:
- extended|app_reviews
tags:
- reviews
- ratings
- ordinal
- text
task_categories:
- text-classification
task_ids:
- text-scoring
- sentiment-scoring
---

This dataset is a quick-and-dirty benchmark for predicting ratings across
different domains and on different rating scales based on text. It pulls in a
bunch of rating datasets, takes at most 1000 instances from each and combines
them into a big dataset.

Requires the `kaggle` library to be installed, and kaggle API keys passed
through environment variables or in ~/.kaggle/kaggle.json. See [the Kaggle
docs](https://www.kaggle.com/docs/api#authentication).
