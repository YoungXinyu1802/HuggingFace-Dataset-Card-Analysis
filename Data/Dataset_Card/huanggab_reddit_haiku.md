---
annotations_creators:
- found
language:
- en
language_creators:
- found
license:
- unknown
multilinguality:
- monolingual
pretty_name: English haiku dataset scraped from Reddit's /r/haiku with topics extracted
  using KeyBERT
size_categories:
- 10K<n<100K
source_datasets:
- extended|other
tags:
- haiku
- poem
- poetry
- reddit
- keybert
- generation
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Dataset Card for "Reddit Haiku"

This dataset contains haikus from the subreddit [/r/haiku](https://www.reddit.com/r/haiku/) scraped and filtered between October 19th and 10th 2022, combined with a [previous dump](https://zissou.infosci.cornell.edu/convokit/datasets/subreddit-corpus/corpus-zipped/hackintosh_ja~-~hamsters/) of that same subreddit packaged by [ConvoKit](https://convokit.cornell.edu/documentation/subreddit.html) as part of the Subreddit Corpus, which is itself a subset of [pushshift.io](https://pushshift.io/)'s big dump.

A main motivation for this dataset was to collect an alternative haiku dataset for evaluation, in particular for evaluating Fabian Mueller's Deep Haiku [model](fabianmmueller/deep-haiku-gpt-j-6b-8bit) which was trained on the Haiku datasets of [hjhalani30](https://www.kaggle.com/datasets/hjhalani30/haiku-dataset) and [bfbarry](https://www.kaggle.com/datasets/bfbarry/haiku-dataset), which are also available on [huggingface hub](https://huggingface.co/datasets/statworx/haiku).

## Fields
The fields are post id (`id`), the content of the haiku (`processed_title`), upvotes (`ups`), and topic keywords (`keywords`). Topic keywords for each haiku have been extracted with the [KeyBERT library](https://maartengr.github.io/KeyBERT/guides/quickstart.html) and truncated to top-5 keywords.

## Usage

This dataset is intended for evaluation, hence there is only one split which is `test`.

```python
from datasets import load_dataset

d=load_dataset('huanggab/reddit_haiku', data_files='test':'merged_with_keywords.csv'})  # use data_files or it will result in error
>>> print(d['train'][0])
#{'Unnamed: 0': 0, 'id': '1020ac', 'processed_title': "There's nothing inside/There is nothing outside me/I search on in hope.", 'ups': 5, 'keywords': "[('inside', 0.5268), ('outside', 0.3751), ('search', 0.3367), ('hope', 0.272)]"}
```

There is code for scraping and processing in `processing_code`, and a subset of the data with more fields such as author Karma, downvotes and posting time at `processing_code/reddit-2022-10-20-dump.csv`.