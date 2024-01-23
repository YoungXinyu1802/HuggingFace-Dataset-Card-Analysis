---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 super world levels
tags:
- text-mining
---

# Mario Maker 2 super world levels
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 super world levels dataset consists of 3.3 million super world levels from Nintendo's online service and adds onto `TheGreatRambler/mm2_world`. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_world_levels", split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'pid': '14510618610706594411',
 'data_id': 19170881,
 'ninjis': 23
}
```
Each row is a level within a super world owned by player `pid` that is denoted by `data_id`. Each level contains some number of ninjis `ninjis`, a rough metric for their popularity.

## Data Structure

### Data Instances

```python
{
 'pid': '14510618610706594411',
 'data_id': 19170881,
 'ninjis': 23
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|pid|string|The player ID of the user who created the super world with this level|
|data_id|int|The data ID of the level|
|ninjis|int|Number of ninjis shown on this level|

### Data Splits

The dataset only contains a train split.

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
