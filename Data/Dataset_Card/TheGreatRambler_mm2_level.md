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
pretty_name: Mario Maker 2 levels
tags:
- text-mining
---

# Mario Maker 2 levels
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 levels dataset consists of 26.6 million levels from Nintendo's online service totaling around 100GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 levels dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_level", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'data_id': 3000004,
 'name': 'カベキック',
 'description': 'カベキックをとにかくするコースです。',
 'uploaded': 1561644329,
 'created': 1561674240,
 'gamestyle': 4,
 'theme': 0,
 'difficulty': 0,
 'tag1': 7,
 'tag2': 10,
 'game_version': 1,
 'world_record': 8049,
 'upload_time': 193540,
 'upload_attempts': 1,
 'num_comments': 60,
 'clear_condition': 0,
 'clear_condition_magnitude': 0,
 'timer': 300,
 'autoscroll_speed': 0,
 'clears': 1646,
 'attempts': 3168,
 'clear_rate': 51.957070707070706,
 'plays': 1704,
 'versus_matches': 80,
 'coop_matches': 27,
 'likes': 152,
 'boos': 118,
 'unique_players_and_versus': 1391,
 'weekly_likes': 0,
 'weekly_plays': 1,
 'uploader_pid': '5218390885570355093',
 'first_completer_pid': '16824392528839047213',
 'record_holder_pid': '5411258160547085075',
 'level_data': [some binary data],
 'unk2': 0,
 'unk3': [some binary data],
 'unk9': 3,
 'unk10': 4,
 'unk11': 1,
 'unk12': 1
}
```

Level data is a binary blob describing the actual level and is equivalent to the level format Nintendo uses in-game. It is gzip compressed and needs to be decompressed to be read. To read it you only need to use the provided `level.ksy` kaitai struct file and install the kaitai struct runtime to parse it into an object:

```python
from datasets import load_dataset
from kaitaistruct import KaitaiStream
from io import BytesIO
from level import Level
import zlib

ds = load_dataset("TheGreatRambler/mm2_level", streaming=True, split="train")
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
Rendering the level data into an image can be done using [Toost](https://github.com/TheGreatRambler/toost) if desired.

You can also download the full dataset. Note that this will download ~100GB:
```python
ds = load_dataset("TheGreatRambler/mm2_level", split="train")
```

## Data Structure

### Data Instances

```python
{
 'data_id': 3000004,
 'name': 'カベキック',
 'description': 'カベキックをとにかくするコースです。',
 'uploaded': 1561644329,
 'created': 1561674240,
 'gamestyle': 4,
 'theme': 0,
 'difficulty': 0,
 'tag1': 7,
 'tag2': 10,
 'game_version': 1,
 'world_record': 8049,
 'upload_time': 193540,
 'upload_attempts': 1,
 'num_comments': 60,
 'clear_condition': 0,
 'clear_condition_magnitude': 0,
 'timer': 300,
 'autoscroll_speed': 0,
 'clears': 1646,
 'attempts': 3168,
 'clear_rate': 51.957070707070706,
 'plays': 1704,
 'versus_matches': 80,
 'coop_matches': 27,
 'likes': 152,
 'boos': 118,
 'unique_players_and_versus': 1391,
 'weekly_likes': 0,
 'weekly_plays': 1,
 'uploader_pid': '5218390885570355093',
 'first_completer_pid': '16824392528839047213',
 'record_holder_pid': '5411258160547085075',
 'level_data': [some binary data],
 'unk2': 0,
 'unk3': [some binary data],
 'unk9': 3,
 'unk10': 4,
 'unk11': 1,
 'unk12': 1
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|data_id|int|Data IDs are unique identifiers, gaps in the table are due to levels deleted by users or Nintendo|
|name|string|Course name|
|description|string|Course description|
|uploaded|int|UTC timestamp for when the level was uploaded|
|created|int|Local timestamp for when the level was created|
|gamestyle|int|Gamestyle, enum below|
|theme|int|Theme, enum below|
|difficulty|int|Difficulty, enum below|
|tag1|int|The first tag, if it exists, enum below|
|tag2|int|The second tag, if it exists, enum below|
|game_version|int|The version of the game this level was made on|
|world_record|int|The world record in milliseconds|
|upload_time|int|The upload time in milliseconds|
|upload_attempts|int|The number of attempts it took the uploader to upload|
|num_comments|int|Number of comments, may not reflect the archived comments if there were more than 1000 comments|
|clear_condition|int|Clear condition, enum below|
|clear_condition_magnitude|int|If applicable, the magnitude of the clear condition|
|timer|int|The timer of the level|
|autoscroll_speed|int|A unit of how fast the configured autoscroll speed is for the level|
|clears|int|Course clears|
|attempts|int|Course attempts|
|clear_rate|float|Course clear rate as a float between 0 and 1|
|plays|int|Course plays, or "footprints"|
|versus_matches|int|Course versus matches|
|coop_matches|int|Course coop matches|
|likes|int|Course likes|
|boos|int|Course boos|
|unique_players_and_versus|int|All unique players that have ever played this level, including the number of versus matches|
|weekly_likes|int|The weekly likes on this course|
|weekly_plays|int|The weekly plays on this course|
|uploader_pid|string|The player ID of the uploader|
|first_completer_pid|string|The player ID of the user who first cleared this course|
|record_holder_pid|string|The player ID of the user who held the world record at time of archival |
|level_data|bytes|The GZIP compressed decrypted level data, kaitai struct file is provided for reading|
|unk2|int|Unknown|
|unk3|bytes|Unknown|
|unk9|int|Unknown|
|unk10|int|Unknown|
|unk11|int|Unknown|
|unk12|int|Unknown|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. This can be used to convert back to their string equivalents:

```python
GameStyles = {
	0: "SMB1",
	1: "SMB3",
	2: "SMW",
	3: "NSMBU",
	4: "SM3DW"
}

Difficulties = {
	0: "Easy",
	1: "Normal",
	2: "Expert",
	3: "Super expert"
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

TagNames = {
	0: "None",
	1: "Standard",
	2: "Puzzle solving",
	3: "Speedrun",
	4: "Autoscroll",
	5: "Auto mario",
	6: "Short and sweet",
	7: "Multiplayer versus",
	8: "Themed",
	9: "Music",
	10: "Art",
	11: "Technical",
	12: "Shooter",
	13: "Boss battle",
	14: "Single player",
	15: "Link"
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

The dataset consists of levels from many different Mario Maker 2 players globally and as such their titles and descriptions could contain harmful language. Harmful depictions could also be present in the level data, should you choose to render it.
