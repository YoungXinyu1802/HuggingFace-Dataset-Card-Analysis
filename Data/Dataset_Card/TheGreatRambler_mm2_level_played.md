---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 1B<n<10B
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 level plays
tags:
- text-mining
---

# Mario Maker 2 level plays
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 level plays dataset consists of 1 billion level plays from Nintendo's online service totaling around 20GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 level plays dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_level_played", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 3000004,
 'pid': '6382913755133534321',
 'cleared': 1,
 'liked': 0
}
```
Each row is a unique play in the level denoted by the `data_id` done by the player denoted by the `pid`, `pid` is a 64 bit integer stored within a string from database limitations. `cleared` and `liked` denote if the player successfully cleared the level during their play and/or liked the level during their play. Every level has only one unique play per player.

You can also download the full dataset. Note that this will download ~20GB:
```python
ds = load_dataset("TheGreatRambler/mm2_level_played", split="train")
```

## Data Structure

### Data Instances

```python
{
 'data_id': 3000004,
 'pid': '6382913755133534321',
 'cleared': 1,
 'liked': 0
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|The data ID of the level this play occured in|
|pid|string|Player ID of the player|
|cleared|bool|Whether the player cleared the level during their play|
|liked|bool|Whether the player liked the level during their play|

### Data Splits

The dataset only contains a train split.

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
