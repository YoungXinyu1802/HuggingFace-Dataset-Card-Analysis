---
language:
- multilingual
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- other
- object-detection
- text-retrieval
- token-classification
- text-generation
task_ids: []
pretty_name: Mario Maker 2 ninji levels
tags:
- text-mining
---

# Mario Maker 2 ninji levels
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 ninji levels dataset consists of 21 ninji levels from Nintendo's online service and aids `TheGreatRambler/mm2_ninji`. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_ninji_level", split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 12171034,
 'name': 'Rolling Snowballs',
 'description': 'Make your way through the snowfields, and keep an eye\nout for Spikes and Snow Pokeys! Stomping on Snow Pokeys\nwill turn them into small snowballs, which you can pick up\nand throw. Play this course as many times as you want,\nand see if you can find the fastest way to the finish!',
 'uploaded': 1575532800,
 'ended': 1576137600,
 'gamestyle': 3,
 'theme': 6,
 'medal_time': 26800,
 'clear_condition': 0,
 'clear_condition_magnitude': 0,
 'unk3_0': 1309513,
 'unk3_1': 62629737,
 'unk3_2': 4355893,
 'unk5': 1,
 'unk6': 0,
 'unk9': 0,
 'level_data': [some binary data]
}
```
Each row is a ninji level denoted by `data_id`. `TheGreatRambler/mm2_ninji` refers to these levels. `level_data` is the same format used in `TheGreatRambler/mm2_level` and the provided Kaitai struct file and `level.py` can be used to decode it:

```python
from datasets import load_dataset
from kaitaistruct import KaitaiStream
from io import BytesIO
from level import Level
import zlib

ds = load_dataset("TheGreatRambler/mm2_ninji_level", split="train")
level_data = next(iter(ds))["level_data"]
level = Level(KaitaiStream(BytesIO(zlib.decompress(level_data))))

# NOTE level.overworld.objects is a fixed size (limitation of Kaitai struct)
# must iterate by object_count or null objects will be included
for i in range(level.overworld.object_count):
	obj = level.overworld.objects[i]
	print("X: %d Y: %d ID: %s" % (obj.x, obj.y, obj.id))

#OUTPUT:
X: 1200 Y: 400 ID: ObjId.block
X: 1360 Y: 400 ID: ObjId.block
X: 1360 Y: 240 ID: ObjId.block
X: 1520 Y: 240 ID: ObjId.block
X: 1680 Y: 240 ID: ObjId.block
X: 1680 Y: 400 ID: ObjId.block
X: 1840 Y: 400 ID: ObjId.block
X: 2000 Y: 400 ID: ObjId.block
X: 2160 Y: 400 ID: ObjId.block
X: 2320 Y: 400 ID: ObjId.block
X: 2480 Y: 560 ID: ObjId.block
X: 2480 Y: 720 ID: ObjId.block
X: 2480 Y: 880 ID: ObjId.block
X: 2160 Y: 880 ID: ObjId.block
```

## Data Structure

### Data Instances

```python
{
 'data_id': 12171034,
 'name': 'Rolling Snowballs',
 'description': 'Make your way through the snowfields, and keep an eye\nout for Spikes and Snow Pokeys! Stomping on Snow Pokeys\nwill turn them into small snowballs, which you can pick up\nand throw. Play this course as many times as you want,\nand see if you can find the fastest way to the finish!',
 'uploaded': 1575532800,
 'ended': 1576137600,
 'gamestyle': 3,
 'theme': 6,
 'medal_time': 26800,
 'clear_condition': 0,
 'clear_condition_magnitude': 0,
 'unk3_0': 1309513,
 'unk3_1': 62629737,
 'unk3_2': 4355893,
 'unk5': 1,
 'unk6': 0,
 'unk9': 0,
 'level_data': [some binary data]
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|The data ID of this ninji level|
|name|string|Name|
|description|string|Description|
|uploaded|int|UTC timestamp of when this was uploaded|
|ended|int|UTC timestamp of when this event ended|
|gamestyle|int|Gamestyle, enum below|
|theme|int|Theme, enum below|
|medal_time|int|Time to get a medal in milliseconds|
|clear_condition|int|Clear condition, enum below|
|clear_condition_magnitude|int|If applicable, the magnitude of the clear condition|
|unk3_0|int|Unknown|
|unk3_1|int|Unknown|
|unk3_2|int|Unknown|
|unk5|int|Unknown|
|unk6|int|Unknown|
|unk9|int|Unknown|
|level_data|bytes|The GZIP compressed decrypted level data, a kaitai struct file is provided to read this|
|one_screen_thumbnail|bytes|The one screen course thumbnail, as a JPEG binary|
|one_screen_thumbnail_url|string|The old URL of this thumbnail|
|one_screen_thumbnail_size|int|The filesize of this thumbnail|
|one_screen_thumbnail_filename|string|The filename of this thumbnail|
|entire_thumbnail|bytes|The entire course thumbnail, as a JPEG binary|
|entire_thumbnail_url|string|The old URL of this thumbnail|
|entire_thumbnail_size|int|The filesize of this thumbnail|
|entire_thumbnail_filename|string|The filename of this thumbnail|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. They match those used by `TheGreatRambler/mm2_level` for the most part, but they are reproduced below:

```python
GameStyles = {
	0: "SMB1",
	1: "SMB3",
	2: "SMW",
	3: "NSMBU",
	4: "SM3DW"
}

CourseThemes = {
	0: "Overworld",
	1: "Underground",
	2: "Castle",
	3: "Airship",
	4: "Underwater",
	5: "Ghost house",
	6: "Snow",
	7: "Desert",
	8: "Sky",
	9: "Forest"
}

ClearConditions = {
	137525990: "Reach the goal without landing after leaving the ground.",
	199585683: "Reach the goal after defeating at least/all (n) Mechakoopa(s).",
	272349836: "Reach the goal after defeating at least/all (n) Cheep Cheep(s).",
	375673178: "Reach the goal without taking damage.",
	426197923: "Reach the goal as Boomerang Mario.",
	436833616: "Reach the goal while wearing a Shoe.",
	713979835: "Reach the goal as Fire Mario.",
	744927294: "Reach the goal as Frog Mario.",
	751004331: "Reach the goal after defeating at least/all (n) Larry(s).",
	900050759: "Reach the goal as Raccoon Mario.",
	947659466: "Reach the goal after defeating at least/all (n) Blooper(s).",
	976173462: "Reach the goal as Propeller Mario.",
	994686866: "Reach the goal while wearing a Propeller Box.",
	998904081: "Reach the goal after defeating at least/all (n) Spike(s).",
	1008094897: "Reach the goal after defeating at least/all (n) Boom Boom(s).",
	1051433633: "Reach the goal while holding a Koopa Shell.",
	1061233896: "Reach the goal after defeating at least/all (n) Porcupuffer(s).",
	1062253843: "Reach the goal after defeating at least/all (n) Charvaargh(s).",
	1079889509: "Reach the goal after defeating at least/all (n) Bullet Bill(s).",
	1080535886: "Reach the goal after defeating at least/all (n) Bully/Bullies.",
	1151250770: "Reach the goal while wearing a Goomba Mask.",
	1182464856: "Reach the goal after defeating at least/all (n) Hop-Chops.",
	1219761531: "Reach the goal while holding a Red POW Block. OR Reach the goal after activating at least/all (n) Red POW Block(s).",
	1221661152: "Reach the goal after defeating at least/all (n) Bob-omb(s).",
	1259427138: "Reach the goal after defeating at least/all (n) Spiny/Spinies.",
	1268255615: "Reach the goal after defeating at least/all (n) Bowser(s)/Meowser(s).",
	1279580818: "Reach the goal after defeating at least/all (n) Ant Trooper(s).",
	1283945123: "Reach the goal on a Lakitu's Cloud.",
	1344044032: "Reach the goal after defeating at least/all (n) Boo(s).",
	1425973877: "Reach the goal after defeating at least/all (n) Roy(s).",
	1429902736: "Reach the goal while holding a Trampoline.",
	1431944825: "Reach the goal after defeating at least/all (n) Morton(s).",
	1446467058: "Reach the goal after defeating at least/all (n) Fish Bone(s).",
	1510495760: "Reach the goal after defeating at least/all (n) Monty Mole(s).",
	1656179347: "Reach the goal after picking up at least/all (n) 1-Up Mushroom(s).",
	1665820273: "Reach the goal after defeating at least/all (n) Hammer Bro(s.).",
	1676924210: "Reach the goal after hitting at least/all (n) P Switch(es). OR Reach the goal while holding a P Switch.",
	1715960804: "Reach the goal after activating at least/all (n) POW Block(s). OR Reach the goal while holding a POW Block.",
	1724036958: "Reach the goal after defeating at least/all (n) Angry Sun(s).",
	1730095541: "Reach the goal after defeating at least/all (n) Pokey(s).",
	1780278293: "Reach the goal as Superball Mario.",
	1839897151: "Reach the goal after defeating at least/all (n) Pom Pom(s).",
	1969299694: "Reach the goal after defeating at least/all (n) Peepa(s).",
	2035052211: "Reach the goal after defeating at least/all (n) Lakitu(s).",
	2038503215: "Reach the goal after defeating at least/all (n) Lemmy(s).",
	2048033177: "Reach the goal after defeating at least/all (n) Lava Bubble(s).",
	2076496776: "Reach the goal while wearing a Bullet Bill Mask.",
	2089161429: "Reach the goal as Big Mario.",
	2111528319: "Reach the goal as Cat Mario.",
	2131209407: "Reach the goal after defeating at least/all (n) Goomba(s)/Galoomba(s).",
	2139645066: "Reach the goal after defeating at least/all (n) Thwomp(s).",
	2259346429: "Reach the goal after defeating at least/all (n) Iggy(s).",
	2549654281: "Reach the goal while wearing a Dry Bones Shell.",
	2694559007: "Reach the goal after defeating at least/all (n) Sledge Bro(s.).",
	2746139466: "Reach the goal after defeating at least/all (n) Rocky Wrench(es).",
	2749601092: "Reach the goal after grabbing at least/all (n) 50-Coin(s).",
	2855236681: "Reach the goal as Flying Squirrel Mario.",
	3036298571: "Reach the goal as Buzzy Mario.",
	3074433106: "Reach the goal as Builder Mario.",
	3146932243: "Reach the goal as Cape Mario.",
	3174413484: "Reach the goal after defeating at least/all (n) Wendy(s).",
	3206222275: "Reach the goal while wearing a Cannon Box.",
	3314955857: "Reach the goal as Link.",
	3342591980: "Reach the goal while you have Super Star invincibility.",
	3346433512: "Reach the goal after defeating at least/all (n) Goombrat(s)/Goombud(s).",
	3348058176: "Reach the goal after grabbing at least/all (n) 10-Coin(s).",
	3353006607: "Reach the goal after defeating at least/all (n) Buzzy Beetle(s).",
	3392229961: "Reach the goal after defeating at least/all (n) Bowser Jr.(s).",
	3437308486: "Reach the goal after defeating at least/all (n) Koopa Troopa(s).",
	3459144213: "Reach the goal after defeating at least/all (n) Chain Chomp(s).",
	3466227835: "Reach the goal after defeating at least/all (n) Muncher(s).",
	3481362698: "Reach the goal after defeating at least/all (n) Wiggler(s).",
	3513732174: "Reach the goal as SMB2 Mario.",
	3649647177: "Reach the goal in a Koopa Clown Car/Junior Clown Car.",
	3725246406: "Reach the goal as Spiny Mario.",
	3730243509: "Reach the goal in a Koopa Troopa Car.",
	3748075486: "Reach the goal after defeating at least/all (n) Piranha Plant(s)/Jumping Piranha Plant(s).",
	3797704544: "Reach the goal after defeating at least/all (n) Dry Bones.",
	3824561269: "Reach the goal after defeating at least/all (n) Stingby/Stingbies.",
	3833342952: "Reach the goal after defeating at least/all (n) Piranha Creeper(s).",
	3842179831: "Reach the goal after defeating at least/all (n) Fire Piranha Plant(s).",
	3874680510: "Reach the goal after breaking at least/all (n) Crates(s).",
	3974581191: "Reach the goal after defeating at least/all (n) Ludwig(s).",
	3977257962: "Reach the goal as Super Mario.",
	4042480826: "Reach the goal after defeating at least/all (n) Skipsqueak(s).",
	4116396131: "Reach the goal after grabbing at least/all (n) Coin(s).",
	4117878280: "Reach the goal after defeating at least/all (n) Magikoopa(s).",
	4122555074: "Reach the goal after grabbing at least/all (n) 30-Coin(s).",
	4153835197: "Reach the goal as Balloon Mario.",
	4172105156: "Reach the goal while wearing a Red POW Box.",
	4209535561: "Reach the Goal while riding Yoshi.",
	4269094462: "Reach the goal after defeating at least/all (n) Spike Top(s).",
	4293354249: "Reach the goal after defeating at least/all (n) Banzai Bill(s)."
}
```

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

As these 21 levels were made and vetted by Nintendo the dataset contains no harmful language or depictions.
