---
language:
- en
language_creators:
- found
license: cc0-1.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
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

Cleaned up version of the rotten tomatoes critic reviews dataset. The original
is obtained from Kaggle:
https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset

Data has been scraped from the publicly available website
https://www.rottentomatoes.com as of 2020-10-31.

The clean up process drops anything without both a review and a rating, as well
as standardising the ratings onto several integer, ordinal scales.

Requires the `kaggle` library to be installed, and kaggle API keys passed
through environment variables or in ~/.kaggle/kaggle.json. See [the Kaggle
docs](https://www.kaggle.com/docs/api#authentication).

A processed version is available at
https://huggingface.co/datasets/frankier/processed_multiscale_rt_critics
