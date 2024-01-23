---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 super worlds
tags:
- text-mining
---

# Mario Maker 2 super worlds
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 super worlds dataset consists of 289 thousand super worlds from Nintendo's online service totaling around 13.5GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 super worlds dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_world", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'pid': '14510618610706594411',
 'world_id': 'c96012bef256ba6b_20200513204805563301',
 'worlds': 1,
 'levels': 5,
 'planet_type': 0,
 'created': 1589420886,
 'unk1': [some binary data],
 'unk5': 3,
 'unk6': 1,
 'unk7': 1,
 'thumbnail': [some binary data]
}
```
Each row is a unique super world denoted by the `world_id` created by the player denoted by the `pid`. Thumbnails are binary PNGs. `unk1` describes the super world itself, including the world map, but its format is unknown as of now.

You can also download the full dataset. Note that this will download ~13.5GB:
```python
ds = load_dataset("TheGreatRambler/mm2_world", split="train")
```

## Data Structure

### Data Instances

```python
{
 'pid': '14510618610706594411',
 'world_id': 'c96012bef256ba6b_20200513204805563301',
 'worlds': 1,
 'levels': 5,
 'planet_type': 0,
 'created': 1589420886,
 'unk1': [some binary data],
 'unk5': 3,
 'unk6': 1,
 'unk7': 1,
 'thumbnail': [some binary data]
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|pid|string|The player ID of the user who created this super world|
|world_id|string|World ID|
|worlds|int|Number of worlds|
|levels|int|Number of levels|
|planet_type|int|Planet type, enum below|
|created|int|UTC timestamp of when this super world was created|
|unk1|bytes|Unknown|
|unk5|int|Unknown|
|unk6|int|Unknown|
|unk7|int|Unknown|
|thumbnail|bytes|The thumbnail, as a JPEG binary|
|thumbnail_url|string|The old URL of this thumbnail|
|thumbnail_size|int|The filesize of this thumbnail|
|thumbnail_filename|string|The filename of this thumbnail|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. This can be used to convert back to their string equivalents:

```python
SuperWorldPlanetType = {
	0: "Earth",
	1: "Moon",
	2: "Sand",
	3: "Green",
	4: "Ice",
	5: "Ringed",
	6: "Red",
	7: "Spiral"
}
```

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset consists of super worlds from many different Mario Maker 2 players globally and as such harmful depictions could be present in their super world thumbnails.
