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
pretty_name: Mall.cz Product Reviews
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


# Dataset Card for Mall.cz Product Reviews (Czech)


## Dataset Description

The dataset contains user reviews from Czech eshop <mall.cz>
Each review contains text, sentiment (positive/negative/neutral), and automatically-detected language (mostly Czech, occasionaly Slovak) using [lingua-py](https://github.com/pemistahl/lingua-py)
The dataset has in total (train+validation+test) 30,000 reviews. The data is balanced.

Train set has 8000 positive, 8000 neutral and 8000 negative reviews.
Validation and test set each have 1000 positive, 1000 neutral and 1000 negative reviews.


## Dataset Features

Each sample contains:
- `review_id`: unique string identifier of the review.
- `rating_str`: string representation of the rating - "pozitivní" / "neutrální" / "negativní"
- `rating_int`: integer representation of the rating (1=positive, 0=neutral, -1=negative)
- `comment_language`: language of the review (mostly "cs", occasionaly "sk")
- `comment`: the string of the review


## Dataset Source

The data is a processed adaptation of [Mall CZ corpus](https://liks.fav.zcu.cz/sentiment/).
The adaptation is label-balanced and adds automatically-detected language
