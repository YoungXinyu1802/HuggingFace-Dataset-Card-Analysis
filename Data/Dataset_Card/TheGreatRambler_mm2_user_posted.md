---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 user uploaded
tags:
- text-mining
---

# Mario Maker 2 user uploaded
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 user uploaded dataset consists of 26.5 million uploaded user levels from Nintendo's online service totaling around 215MB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 user uploaded dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_user_posted", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'pid': '10491033288855085861',
 'data_id': 27359486
}
```
Each row is a unique uploaded level denoted by the `data_id` uploaded by the player denoted by the `pid`.

You can also download the full dataset. Note that this will download ~215MB:
```python
ds = load_dataset("TheGreatRambler/mm2_user_posted", split="train")
```

## Data Structure

### Data Instances

```python
{
 'pid': '10491033288855085861',
 'data_id': 27359486
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|pid|string|The player ID of this user, an unsigned 64 bit integer as a string|
|data_id|int|The data ID of the level this user uploaded|

### Data Splits

The dataset only contains a train split.

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
