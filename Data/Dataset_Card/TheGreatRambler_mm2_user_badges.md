---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 1k<10K
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 user badges
tags:
- text-mining
---

# Mario Maker 2 user badges
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 user badges dataset consists of 9328 user badges (they are capped to 10k globally) from Nintendo's online service and adds onto `TheGreatRambler/mm2_user`. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_user_badges", split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'pid': '1779763691699286988',
 'type': 4,
 'rank': 6
}
```
Each row is a badge awarded to the player denoted by `pid`. `TheGreatRambler/mm2_user` contains these players.

## Data Structure

### Data Instances

```python
{
 'pid': '1779763691699286988',
 'type': 4,
 'rank': 6
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|pid|string|Player ID|
|type|int|The kind of badge, enum below|
|rank|int|The rank of badge, enum below|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. This can be used to convert back to their string equivalents:

```python
BadgeTypes = {
	0: "Maker Points (All-Time)",
	1: "Endless Challenge (Easy)",
	2: "Endless Challenge (Normal)",
	3: "Endless Challenge (Expert)",
	4: "Endless Challenge (Super Expert)",
	5: "Multiplayer Versus",
	6: "Number of Clears",
	7: "Number of First Clears",
	8: "Number of World Records",
	9: "Maker Points (Weekly)"
}

BadgeRanks = {
	6: "Bronze",
	5: "Silver",
	4: "Gold",
	3: "Bronze Ribbon",
	2: "Silver Ribbon",
	1: "Gold Ribbon"
}
```

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
