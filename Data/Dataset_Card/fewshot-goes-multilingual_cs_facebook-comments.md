---
annotations_creators:
- found
language:
- cs
language_creators:
- found
license:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
pretty_name: Czech Facebook comments
size_categories:
- 10K<n<100K
source_datasets:
- original
tags: []
task_categories:
- text-classification
task_ids:
- sentiment-classification
---


# Dataset Card for Czech Facebook comments


## Dataset Description

The dataset contains user comments from Facebook. Each comment contains text, sentiment (positive/negative/neutral).
The dataset has in total (train+validation+test) 6,600 reviews. The data is balanced.


## Dataset Features

Each sample contains:
- `comment_id`: unique string identifier of the comment.
- `sentiment_str`: string representation of the rating - "pozitivní" / "neutrální" / "negativní"
- `sentiment_int`: integer representation of the rating (1=positive, 0=neutral, -1=negative)
- `comment`: the string of the comment


## Dataset Source

The data is a processed adaptation of [Facebook CZ Corpus](https://liks.fav.zcu.cz/sentiment/).
This adaptation is label-balanced.
