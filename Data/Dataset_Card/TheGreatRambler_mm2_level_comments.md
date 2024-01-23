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
pretty_name: Mario Maker 2 level comments
tags:
- text-mining
---

# Mario Maker 2 level comments
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 level comment dataset consists of 31.9 million level comments from Nintendo's online service totaling around 20GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 level comment dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_level_comments", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 3000006,
 'comment_id': '20200430072710528979_302de3722145c7a2_2dc6c6',
 'type': 2,
 'pid': '3471680967096518562',
 'posted': 1561652887,
 'clear_required': 0,
 'text': '',
 'reaction_image_id': 10,
 'custom_image': [some binary data],
 'has_beaten': 0,
 'x': 557,
 'y': 64,
 'reaction_face': 0,
 'unk8': 0,
 'unk10': 0,
 'unk12': 0,
 'unk14': [some binary data],
 'unk17': 0
}
```
Comments can be one of three types: text, reaction image or custom image. `type` can be used with the enum below to identify different kinds of comments. Custom images are binary PNGs.

You can also download the full dataset. Note that this will download ~20GB:
```python
ds = load_dataset("TheGreatRambler/mm2_level_comments", split="train")
```

## Data Structure

### Data Instances

```python
{
 'data_id': 3000006,
 'comment_id': '20200430072710528979_302de3722145c7a2_2dc6c6',
 'type': 2,
 'pid': '3471680967096518562',
 'posted': 1561652887,
 'clear_required': 0,
 'text': '',
 'reaction_image_id': 10,
 'custom_image': [some binary data],
 'has_beaten': 0,
 'x': 557,
 'y': 64,
 'reaction_face': 0,
 'unk8': 0,
 'unk10': 0,
 'unk12': 0,
 'unk14': [some binary data],
 'unk17': 0
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|The data ID of the level this comment appears on|
|comment_id|string|Comment ID|
|type|int|Type of comment, enum below|
|pid|string|Player ID of the comment creator|
|posted|int|UTC timestamp of when this comment was created|
|clear_required|bool|Whether this comment requires a clear to view|
|text|string|If the comment type is text, the text of the comment|
|reaction_image_id|int|If this comment is a reaction image, the id of the reaction image, enum below|
|custom_image|bytes|If this comment is a custom drawing, the custom drawing as a PNG binary|
|has_beaten|int|Whether the user had beaten the level when they created the comment|
|x|int|The X position of the comment in game|
|y|int|The Y position of the comment in game|
|reaction_face|int|The reaction face of the mii of this user, enum below|
|unk8|int|Unknown|
|unk10|int|Unknown|
|unk12|int|Unknown|
|unk14|bytes|Unknown|
|unk17|int|Unknown|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. This can be used to convert back to their string equivalents:

```python
CommentType = {
	0: "Custom Image",
	1: "Text",
	2: "Reaction Image"
}

CommentReactionImage = {
	0: "Nice!",
	1: "Good stuff!",
	2: "So tough...",
	3: "EASY",
	4: "Seriously?!",
	5: "Wow!",
	6: "Cool idea!",
	7: "SPEEDRUN!",
	8: "How?!",
	9: "Be careful!",
	10: "So close!",
	11: "Beat it!"
}

CommentReactionFace = {
	0: "Normal",
	16: "Wink",
	1: "Happy",
	4: "Surprised",
	18: "Scared",
	3: "Confused"
}
```

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset consists of comments from many different Mario Maker 2 players globally and as such their text could contain harmful language. Harmful depictions could also be present in the custom images.
