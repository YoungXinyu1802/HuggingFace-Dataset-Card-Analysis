---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 100M<n<1B
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 level deaths
tags:
- text-mining
---

# Mario Maker 2 level deaths
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 level deaths dataset consists of 564 million level deaths from Nintendo's online service totaling around 2.5GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 level deaths dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_level_deaths", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 3000382,
 'x': 696,
 'y': 0,
 'is_subworld': 0
}
```
Each row is a unique death in the level denoted by the `data_id` that occurs at the provided coordinates. `is_subworld` denotes whether the death happened in the main world or the subworld.

You can also download the full dataset. Note that this will download ~2.5GB:
```python
ds = load_dataset("TheGreatRambler/mm2_level_deaths", split="train")
```

## Data Structure

### Data Instances

```python
{
 'data_id': 3000382,
 'x': 696,
 'y': 0,
 'is_subworld': 0
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|The data ID of the level this death occured in|
|x|int|X coordinate of death|
|y|int|Y coordinate of death|
|is_subworld|bool|Whether the death happened in the main world or the subworld|

### Data Splits

The dataset only contains a train split.

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
