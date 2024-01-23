---
task_categories:
- text-classification
language:
- en
tags:
- code
size_categories:
- 1M<n<10M
---
# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

This dataset contains more than 2.1 million negative user reviews (reviews with 1 or 2 ratings) from 9775 apps across 48 categories from Google Play. Moreover, the number of votes that each review received within a month is also recorded. Those reviews having more votes can be cosidered as improtant reviews.

### Supported Tasks and Leaderboards

Detecting app issues proactively by identifying prominent app reviews.

### Languages

English

## How to use the dataset?
```
from datasets import load_dataset
import pandas as pd

# Load the dataset
dataset = load_dataset("recmeapp/thumbs-up")

# Convert to Pandas
dfs = {split: dset.to_pandas() for split, dset in dataset.items()}
dataset_df = pd.concat([dfs["train"], dfs["validation"], dfs["test"]])

# How many rows are there in the thumbs-up dataset?
print(f'There are {len(dataset_df)} rows in the thumbs-up dataset.')

# How many unique apps are there in the thumbs-up dataset?
print(f'There are {len(dataset_df["app_name"].unique())} unique apps.')

# How many categoris are there in the thumbs-up dataset?
print(f'There are {len(dataset_df["category"].unique())} unique categories.')

# What is the highest vote a review received in the thumbs-up dataset?
print(f'The highest vote a review received is {max(dataset_df["votes"])}.')
```

## Usage
This dataset was used for training the PPrior, a novel framework proposed in [this paper](https://ieeexplore.ieee.org/abstract/document/10020586). You can find the implementation in this [GitHub repository](https://github.com/MultifacetedNLP/PPrior).