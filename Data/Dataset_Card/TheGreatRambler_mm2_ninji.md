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
pretty_name: Mario Maker 2 ninjis
tags:
- text-mining
---

# Mario Maker 2 ninjis
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 ninjis dataset consists of 3 million ninji replays from Nintendo's online service totaling around 12.5GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 ninjis dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_ninji", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 12171034,
 'pid': '4748613890518923485',
 'time': 83388,
 'replay': [some binary data]
}
```
Each row is a ninji run in the level denoted by the `data_id` done by the player denoted by the `pid`, The length of this ninji run is `time` in milliseconds.

`replay` is a gzip compressed binary file format describing the animation frames and coordinates of the player throughout the run. Parsing the replay is as follows:

```python
from datasets import load_dataset
import zlib
import struct

ds = load_dataset("TheGreatRambler/mm2_ninji", streaming=True, split="train")
row = next(iter(ds))
replay = zlib.decompress(row["replay"])

frames = struct.unpack(">I", replay[0x10:0x14])[0]
character = replay[0x14]

character_mapping = {
	0: "Mario",
	1: "Luigi",
	2: "Toad",
	3: "Toadette"
}

# player_state is between 0 and 14 and varies between gamestyles
# as outlined below. Determining the gamestyle of a particular run
# and rendering the level being played requires TheGreatRambler/mm2_ninji_level
player_state_base = {
	0: "Run/Walk",
	1: "Jump",
	2: "Swim",
	3: "Climbing",
	5: "Sliding",
	7: "Dry bones shell",
	8: "Clown car",
	9: "Cloud",
	10: "Boot",
	11: "Walking cat"
}

player_state_nsmbu = {
	4: "Sliding",
	6: "Turnaround",
	10: "Yoshi",
	12: "Acorn suit",
	13: "Propeller active",
	14: "Propeller neutral"
}

player_state_sm3dw = {
	4: "Sliding",
	6: "Turnaround",
	7: "Clear pipe",
	8: "Cat down attack",
	13: "Propeller active",
	14: "Propeller neutral"
}

player_state_smb1 = {
	4: "Link down slash",
	5: "Crouching"
}

player_state_smw = {
	10: "Yoshi",
	12: "Cape"
}

print("Frames: %d\nCharacter: %s" % (frames, character_mapping[character]))

current_offset = 0x3C
# Ninji updates are reported every 4 frames
for i in range((frames + 2) // 4):
	flags = replay[current_offset] >> 4
	player_state = replay[current_offset] & 0x0F
	current_offset += 1

	x = struct.unpack("<H", replay[current_offset:current_offset + 2])[0]
	current_offset += 2
	y = struct.unpack("<H", replay[current_offset:current_offset + 2])[0]
	current_offset += 2

	if flags & 0b00000110:
		unk1 = replay[current_offset]
		current_offset += 1

	in_subworld = flags & 0b00001000

	print("Frame %d:\n    Flags: %s,\n    Animation state: %d,\n    X: %d,\n    Y: %d,\n    In subworld: %s"
		% (i, bin(flags), player_state, x, y, in_subworld))

#OUTPUT:
Frames: 5006
Character: Mario
Frame 0:
    Flags: 0b0,
    Animation state: 0,
    X: 2672,
    Y: 2288,
    In subworld: 0
Frame 1:
    Flags: 0b0,
    Animation state: 0,
    X: 2682,
    Y: 2288,
    In subworld: 0
Frame 2:
    Flags: 0b0,
    Animation state: 0,
    X: 2716,
    Y: 2288,
    In subworld: 0
...
Frame 1249:
    Flags: 0b0,
    Animation state: 1,
    X: 59095,
    Y: 3749,
    In subworld: 0
Frame 1250:
    Flags: 0b0,
    Animation state: 1,
    X: 59246,
    Y: 3797,
    In subworld: 0
Frame 1251:
    Flags: 0b0,
    Animation state: 1,
    X: 59402,
    Y: 3769,
    In subworld: 0
```

You can also download the full dataset. Note that this will download ~12.5GB:
```python
ds = load_dataset("TheGreatRambler/mm2_ninji", split="train")
```

## Data Structure

### Data Instances

```python
{
 'data_id': 12171034,
 'pid': '4748613890518923485',
 'time': 83388,
 'replay': [some binary data]
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|The data ID of the level this run occured in|
|pid|string|Player ID of the player|
|time|int|Length in milliseconds of the run|
|replay|bytes|Replay file of this run|

### Data Splits

The dataset only contains a train split.

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset contains no harmful language or depictions.
