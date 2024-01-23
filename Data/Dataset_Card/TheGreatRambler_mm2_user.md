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
pretty_name: Mario Maker 2 users
tags:
- text-mining
---

# Mario Maker 2 users
Part of the [Mario Maker 2 Dataset Collection](https://tgrcode.com/posts/mario_maker_2_datasets)

## Dataset Description
The Mario Maker 2 users dataset consists of 6 million users from Nintendo's online service totaling around 1.2GB of data. The dataset was created using the self-hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api) over the course of 1 month in February 2022.

### How to use it
The Mario Maker 2 users dataset is a very large dataset so for most use cases it is recommended to make use of the streaming API of `datasets`. You can load and iterate through the dataset with the following code:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_user", streaming=True, split="train")
print(next(iter(ds)))

#OUTPUT:
{
 'pid': '14608829447232141607',
 'data_id': 1,
 'region': 0,
 'name': 'げんまい',
 'country': 'JP',
 'last_active': 1578384457,
 'mii_data': [some binary data],
 'mii_image': '000f165d6574777a7881949e9da1acc1cac7cacad3dad9e0eff2f9faf900430a151c25384258637084878e8b96a0b0',
 'pose': 0,
 'hat': 0,
 'shirt': 0,
 'pants': 0,
 'wearing_outfit': 0,
 'courses_played': 12,
 'courses_cleared': 10,
 'courses_attempted': 23,
 'courses_deaths': 13,
 'likes': 0,
 'maker_points': 0,
 'easy_highscore': 0,
 'normal_highscore': 0,
 'expert_highscore': 0,
 'super_expert_highscore': 0,
 'versus_rating': 0,
 'versus_rank': 1,
 'versus_won': 0,
 'versus_lost': 1,
 'versus_win_streak': 0,
 'versus_lose_streak': 1,
 'versus_plays': 1,
 'versus_disconnected': 0,
 'coop_clears': 1,
 'coop_plays': 1,
 'recent_performance': 1383,
 'versus_kills': 0,
 'versus_killed_by_others': 0,
 'multiplayer_unk13': 286,
 'multiplayer_unk14': 5999927,
 'first_clears': 0,
 'world_records': 0,
 'unique_super_world_clears': 0,
 'uploaded_levels': 0,
 'maximum_uploaded_levels': 100,
 'weekly_maker_points': 0,
 'last_uploaded_level': 1561555201,
 'is_nintendo_employee': 0,
 'comments_enabled': 1,
 'tags_enabled': 0,
 'super_world_id': '',
 'unk3': 0,
 'unk12': 0,
 'unk16': 0
}
```
Each row is a unique play in the level denoted by the `data_id` done by the player denoted by the `pid`, `pid` is a 64 bit integer stored within a string from database limitations. `cleared` and `liked` denote if the player successfully cleared the level during their play and/or liked the level during their play. Every level has only one unique play per player.

Each row is a unique user associated denoted by the `pid`. `data_id` is not used by Nintendo but, like levels, it counts up sequentially and can be used to determine account age. `mii_data` is a `charinfo` type Switch Mii. `mii_image` can be used with Nintendo's online studio API to generate images:

```python
from datasets import load_dataset

ds = load_dataset("TheGreatRambler/mm2_user", streaming=True, split="train")

mii_image = next(iter(ds))["mii_image"]
print("Face: https://studio.mii.nintendo.com/miis/image.png?data=%s&type=face&width=512&instanceCount=1" % mii_image)
print("Body: https://studio.mii.nintendo.com/miis/image.png?data=%s&type=all_body&width=512&instanceCount=1" % mii_image)
print("Face (x16): https://studio.mii.nintendo.com/miis/image.png?data=%s&type=face&width=512&instanceCount=16" % mii_image)
print("Body (x16): https://studio.mii.nintendo.com/miis/image.png?data=%s&type=all_body&width=512&instanceCount=16" % mii_image)
```

`pose`, `hat`, `shirt` and `pants` has associated enums described below. `last_active` and `last_uploaded_level` are UTC timestamps. `super_world_id`, if not empty, provides the ID of a super world in `TheGreatRambler/mm2_world`.

You can also download the full dataset. Note that this will download ~1.2GB:
```python
ds = load_dataset("TheGreatRambler/mm2_user", split="train")
```

## Data Structure

### Data Instances

```python
{
 'pid': '14608829447232141607',
 'data_id': 1,
 'region': 0,
 'name': 'げんまい',
 'country': 'JP',
 'last_active': 1578384457,
 'mii_data': [some binary data],
 'mii_image': '000f165d6574777a7881949e9da1acc1cac7cacad3dad9e0eff2f9faf900430a151c25384258637084878e8b96a0b0',
 'pose': 0,
 'hat': 0,
 'shirt': 0,
 'pants': 0,
 'wearing_outfit': 0,
 'courses_played': 12,
 'courses_cleared': 10,
 'courses_attempted': 23,
 'courses_deaths': 13,
 'likes': 0,
 'maker_points': 0,
 'easy_highscore': 0,
 'normal_highscore': 0,
 'expert_highscore': 0,
 'super_expert_highscore': 0,
 'versus_rating': 0,
 'versus_rank': 1,
 'versus_won': 0,
 'versus_lost': 1,
 'versus_win_streak': 0,
 'versus_lose_streak': 1,
 'versus_plays': 1,
 'versus_disconnected': 0,
 'coop_clears': 1,
 'coop_plays': 1,
 'recent_performance': 1383,
 'versus_kills': 0,
 'versus_killed_by_others': 0,
 'multiplayer_unk13': 286,
 'multiplayer_unk14': 5999927,
 'first_clears': 0,
 'world_records': 0,
 'unique_super_world_clears': 0,
 'uploaded_levels': 0,
 'maximum_uploaded_levels': 100,
 'weekly_maker_points': 0,
 'last_uploaded_level': 1561555201,
 'is_nintendo_employee': 0,
 'comments_enabled': 1,
 'tags_enabled': 0,
 'super_world_id': '',
 'unk3': 0,
 'unk12': 0,
 'unk16': 0
}
```

### Data Fields

|Field|Type|Description|
|---|---|---|
|pid|string|The player ID of this user, an unsigned 64 bit integer as a string|
|data_id|int|The data ID of this user, while not used internally user codes are generated using this|
|region|int|User region, enum below|
|name|string|User name|
|country|string|User country as a 2 letter ALPHA-2 code|
|last_active|int|UTC timestamp of when this user was last active, not known what constitutes active|
|mii_data|bytes|The CHARINFO blob of this user's Mii|
|mii_image|string|A string that can be fed into Nintendo's studio API to generate an image|
|pose|int|Pose, enum below|
|hat|int|Hat, enum below|
|shirt|int|Shirt, enum below|
|pants|int|Pants, enum below|
|wearing_outfit|bool|Whether this user is wearing pants|
|courses_played|int|How many courses this user has played|
|courses_cleared|int|How many courses this user has cleared|
|courses_attempted|int|How many courses this user has attempted|
|courses_deaths|int|How many times this user has died|
|likes|int|How many likes this user has recieved|
|maker_points|int|Maker points|
|easy_highscore|int|Easy highscore|
|normal_highscore|int|Normal highscore|
|expert_highscore|int|Expert highscore|
|super_expert_highscore|int|Super expert high score|
|versus_rating|int|Versus rating|
|versus_rank|int|Versus rank, enum below|
|versus_won|int|How many courses this user has won in versus|
|versus_lost|int|How many courses this user has lost in versus|
|versus_win_streak|int|Versus win streak|
|versus_lose_streak|int|Versus lose streak|
|versus_plays|int|Versus plays|
|versus_disconnected|int|Times user has disconnected in versus|
|coop_clears|int|Coop clears|
|coop_plays|int|Coop plays|
|recent_performance|int|Unknown variable relating to versus performance|
|versus_kills|int|Kills in versus, unknown what activities constitute a kill|
|versus_killed_by_others|int|Deaths in versus from other users, little is known about what activities constitute a death|
|multiplayer_unk13|int|Unknown, relating to multiplayer|
|multiplayer_unk14|int|Unknown, relating to multiplayer|
|first_clears|int|First clears|
|world_records|int|World records|
|unique_super_world_clears|int|Super world clears|
|uploaded_levels|int|Number of uploaded levels|
|maximum_uploaded_levels|int|Maximum number of levels this user may upload|
|weekly_maker_points|int|Weekly maker points|
|last_uploaded_level|int|UTC timestamp of when this user last uploaded a level|
|is_nintendo_employee|bool|Whether this user is an official Nintendo account|
|comments_enabled|bool|Whether this user has comments enabled on their levels|
|tags_enabled|bool|Whether this user has tags enabled on their levels|
|super_world_id|string|The ID of this user's super world, blank if they do not have one|
|unk3|int|Unknown|
|unk12|int|Unknown|
|unk16|int|Unknown|

### Data Splits

The dataset only contains a train split.

## Enums

The dataset contains some enum integer fields. This can be used to convert back to their string equivalents:

```python
Regions = {
	0: "Asia",
	1: "Americas",
	2: "Europe",
	3: "Other"
}

MultiplayerVersusRanks = {
	1: "D",
	2: "C",
	3: "B",
	4: "A",
	5: "S",
	6: "S+"
}

UserPose = {
	0: "Normal",
	15: "Fidgety",
	17: "Annoyed",
	18: "Buoyant",
	19: "Thrilled",
	20: "Let's go!",
	21: "Hello!",
	29: "Show-Off",
	31: "Cutesy",
	39: "Hyped!"
}

UserHat = {
	0: "None",
	1: "Mario Cap",
	2: "Luigi Cap",
	4: "Mushroom Hairclip",
	5: "Bowser Headpiece",
	8: "Princess Peach Wig",
	11: "Builder Hard Hat",
	12: "Bowser Jr. Headpiece",
	13: "Pipe Hat",
	15: "Cat Mario Headgear",
	16: "Propeller Mario Helmet",
	17: "Cheep Cheep Hat",
	18: "Yoshi Hat",
	21: "Faceplant",
	22: "Toad Cap",
	23: "Shy Cap",
	24: "Magikoopa Hat",
	25: "Fancy Top Hat",
	26: "Doctor Headgear",
	27: "Rocky Wrench Manhold Lid",
	28: "Super Star Barrette",
	29: "Rosalina Wig",
	30: "Fried-Chicken Headgear",
	31: "Royal Crown",
	32: "Edamame Barrette",
	33: "Superball Mario Hat",
	34: "Robot Cap",
	35: "Frog Cap",
	36: "Cheetah Headgear",
	37: "Ninji Cap",
	38: "Super Acorn Hat",
	39: "Pokey Hat",
	40: "Snow Pokey Hat"
}

UserShirt = {
	0: "Nintendo Shirt",
	1: "Mario Outfit",
	2: "Luigi Outfit",
	3: "Super Mushroom Shirt",
	5: "Blockstripe Shirt",
	8: "Bowser Suit",
	12: "Builder Mario Outfit",
	13: "Princess Peach Dress",
	16: "Nintendo Uniform",
	17: "Fireworks Shirt",
	19: "Refreshing Shirt",
	21: "Reset Dress",
	22: "Thwomp Suit",
	23: "Slobbery Shirt",
	26: "Cat Suit",
	27: "Propeller Mario Clothes",
	28: "Banzai Bill Shirt",
	29: "Staredown Shirt",
	31: "Yoshi Suit",
	33: "Midnight Dress",
	34: "Magikoopa Robes",
	35: "Doctor Coat",
	37: "Chomp-Dog Shirt",
	38: "Fish Bone Shirt",
	40: "Toad Outfit",
	41: "Googoo Onesie",
	42: "Matrimony Dress",
	43: "Fancy Tuxedo",
	44: "Koopa Troopa Suit",
	45: "Laughing Shirt",
	46: "Running Shirt",
	47: "Rosalina Dress",
	49: "Angry Sun Shirt",
	50: "Fried-Chicken Hoodie",
	51: "? Block Hoodie",
	52: "Edamame Camisole",
	53: "I-Like-You Camisole",
	54: "White Tanktop",
	55: "Hot Hot Shirt",
	56: "Royal Attire",
	57: "Superball Mario Suit",
	59: "Partrick Shirt",
	60: "Robot Suit",
	61: "Superb Suit",
	62: "Yamamura Shirt",
	63: "Princess Peach Tennis Outfit",
	64: "1-Up Hoodie",
	65: "Cheetah Tanktop",
	66: "Cheetah Suit",
	67: "Ninji Shirt",
	68: "Ninji Garb",
	69: "Dash Block Hoodie",
	70: "Fire Mario Shirt",
	71: "Raccoon Mario Shirt",
	72: "Cape Mario Shirt",
	73: "Flying Squirrel Mario Shirt",
	74: "Cat Mario Shirt",
	75: "World Wear",
	76: "Koopaling Hawaiian Shirt",
	77: "Frog Mario Raincoat",
	78: "Phanto Hoodie"
}

UserPants = {
	0: "Black Short-Shorts",
	1: "Denim Jeans",
	5: "Denim Skirt",
	8: "Pipe Skirt",
	9: "Skull Skirt",
	10: "Burner Skirt",
	11: "Cloudwalker",
	12: "Platform Skirt",
	13: "Parent-and-Child Skirt",
	17: "Mario Swim Trunks",
	22: "Wind-Up Shoe",
	23: "Hoverclown",
	24: "Big-Spender Shorts",
	25: "Shorts of Doom!",
	26: "Doorduroys",
	27: "Antsy Corduroys",
	28: "Bouncy Skirt",
	29: "Stingby Skirt",
	31: "Super Star Flares",
	32: "Cheetah Runners",
	33: "Ninji Slacks"
}

# Checked against user's shirt
UserIsOutfit = {
	0: False,
	1: True,
	2: True,
	3: False,
	5: False,
	8: True,
	12: True,
	13: True,
	16: False,
	17: False,
	19: False,
	21: True,
	22: True,
	23: False,
	26: True,
	27: True,
	28: False,
	29: False,
	31: True,
	33: True,
	34: True,
	35: True,
	37: False,
	38: False,
	40: True,
	41: True,
	42: True,
	43: True,
	44: True,
	45: False,
	46: False,
	47: True,
	49: False,
	50: False,
	51: False,
	52: False,
	53: False,
	54: False,
	55: False,
	56: True,
	57: True,
	59: False,
	60: True,
	61: True,
	62: False,
	63: True,
	64: False,
	65: False,
	66: True,
	67: False,
	68: True,
	69: False,
	70: False,
	71: False,
	72: False,
	73: False,
	74: False,
	75: True,
	76: False,
	77: True,
	78: False
}
```

<!-- TODO create detailed statistics -->

## Dataset Creation

The dataset was created over a little more than a month in Febuary 2022 using the self hosted [Mario Maker 2 api](https://tgrcode.com/posts/mario_maker_2_api). As requests made to Nintendo's servers require authentication the process had to be done with upmost care and limiting download speed as to not overload the API and risk a ban. There are no intentions to create an updated release of this dataset.

## Considerations for Using the Data

The dataset consists of many different Mario Maker 2 players globally and as such their names could contain harmful language. Harmful depictions could also be present in their Miis, should you choose to render it.
