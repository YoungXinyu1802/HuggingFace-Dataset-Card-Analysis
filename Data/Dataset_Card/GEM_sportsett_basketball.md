---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- mit
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: sportsett_basketball
tags:
- data-to-text
---

# Dataset Card for GEM/sportsett_basketball

## Dataset Description

- **Homepage:** https://github.com/nlgcat/sport_sett_basketball
- **Repository:** https://github.com/nlgcat/sport_sett_basketball
- **Paper:** https://aclanthology.org/2020.intellang-1.4/
- **Leaderboard:** N/A
- **Point of Contact:** Craig Thomson

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/sportsett_basketball).

### Dataset Summary 

The sportsett dataset is an English data-to-text dataset in the basketball domain. The inputs are statistics summarizing an NBA game and the outputs are high-quality descriptions of the game in natural language. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/sportsett_basketball')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/sportsett_basketball).

#### website
[Github](https://github.com/nlgcat/sport_sett_basketball)

#### paper
[ACL Anthology](https://aclanthology.org/2020.intellang-1.4/)

#### authors
Craig Thomson, Ashish Upadhyay

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Github](https://github.com/nlgcat/sport_sett_basketball)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/nlgcat/sport_sett_basketball)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.intellang-1.4/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{thomson-etal-2020-sportsett,
    title = "{S}port{S}ett:Basketball - A robust and maintainable data-set for Natural Language Generation",
    author = "Thomson, Craig  and
      Reiter, Ehud  and
      Sripada, Somayajulu",
    booktitle = "Proceedings of the Workshop on Intelligent Information Processing and Natural Language Generation",
    month = sep,
    year = "2020",
    address = "Santiago de Compostela, Spain",
    publisher = "Association for Computational Lingustics",
    url = "https://aclanthology.org/2020.intellang-1.4",
    pages = "32--40",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Craig Thomson

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
c.thomson@abdn.ac.uk

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
American English

One dialect, one language.

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
American sports writers

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
mit: MIT License

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Maintain a robust and scalable Data-to-Text generation resource with structured data and textual summaries

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
A model trained on this dataset should summarise the statistical and other information from a basketball game.  This will be focused on a single game, although facts from prior games, or aggregate statistics over many games can and should be used for comparison where appropriate.  There no single common narrative, although summaries usually start with who player, when, where, and the score.  They then provide high level commentary on what the difference in the game was (why the winner won).  breakdowns of statistics for prominent players follow, winning team first.  Finally, the upcoming schedule for both teams is usually included.  There are, however, other types of fact that can be included, and other narrative structures.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of Aberdeen, Robert Gordon University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Craig Thomson, Ashish Upadhyay

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
EPSRC

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Craig Thomson, Ashish Upadhyay


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
Each instance in the dataset has five fields. 

1. "sportsett_id": This is a unique id as used in the original SportSett database. It starts with '1' with the first instance in the train-set and ends with '6150' with the last instance in test-set.

2. "gem_id": This is a unique id created as per GEM's requirement which follows the `GEM-${DATASET_NAME}-${SPLIT-NAME}-${id}` pattern.

3. "game": This field contains a dictionary with information about current game. It has information such as date on which the game was played alongwith the stadium, city, state  where it was played.

4. "teams": This filed is a dictionary of multiple nested dictionaries. On the highest level, it has two keys: 'home' and 'vis', which provide the stats for home team and visiting team of the game. Both are dictionaries with same structure. Each dictionary will contain team's information such as name of the team, their total wins/losses in current season, their conference standing, the SportSett ids for their current and previous games. Apart from these general information, they also have the box- and line- scores for the team in the game. Box score is the stats of players from the team at the end of the game, while line score along with the whole game stats is divided into quarters and halves as well as the extra-time (if happened in the game). After these scores, there is another field of next-game, which gives general information about team's next game such as the place and opponent's name of the next game.

5. "summaries": This is a list of summaries for each game. Some games will have more than one summary, in that case, the list will have more than one entries. Each summary in the list is a string which can be tokenised by a space, following the practices in RotoWire-FG dataset ([Wang, 2019](https://www.aclweb.org/anthology/W19-8639)).

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure mostly follows the original structure defined in RotoWire dataset ([Wiseman et. al. 2017](https://aclanthology.org/D17-1239/)) with some modifications (such as game and next-game keys) address the problem of information gap between input and output data ([Thomson et. al. 2020](https://aclanthology.org/2020.inlg-1.6/)).

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
Similar to RotoWire dataset ([Wiseman et. al. 2017](https://aclanthology.org/D17-1239/))

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
	"sportsett_id": "1",
	"gem_id": "GEM-sportsett_basketball-train-0",
	"game": {
		"day": "1",
		"month": "November",
		"year": "2014",
		"dayname": "Saturday",
		"season": "2014",
		"stadium": "Wells Fargo Center",
		"city": "Philadelphia",
		"state": "Pennsylvania",
		"attendance": "19753",
		"capacity": "20478",
		"game_id": "1"
	},
	"teams": {
		"home": {
			"name": "76ers",
			"place": "Philadelphia",
			"conference": "Eastern Conference",
			"division": "Atlantic",
			"wins": "0",
			"losses": "3",
			"conference_standing": 15,
			"game_number": "3",
			"previous_game_id": "42",
			"next_game_id": "2",
			"line_score": {
				"game": {
					"FG3A": "23",
					"FG3M": "7",
					"FG3_PCT": "30",
					"FGA": "67",
					"FGM": "35",
					"FG_PCT": "52",
					"FTA": "26",
					"FTM": "19",
					"FT_PCT": "73",
					"DREB": "33",
					"OREB": "4",
					"TREB": "37",
					"BLK": "10",
					"AST": "28",
					"STL": "9",
					"TOV": "24",
					"PF": "21",
					"PTS": "96",
					"MIN": "4"
				},
				"H1": {
					"FG3A": "82",
					"FG3M": "30",
					"FG3_PCT": "37",
					"FGA": "2115",
					"FGM": "138",
					"FG_PCT": "7",
					"FTA": "212",
					"FTM": "18",
					"FT_PCT": "8",
					"DREB": "810",
					"OREB": "21",
					"TREB": "831",
					"BLK": "51",
					"AST": "107",
					"STL": "21",
					"TOV": "64",
					"PTS": "3024",
					"MIN": "6060"
				},
				"H2": {
					"FG3A": "85",
					"FG3M": "40",
					"FG3_PCT": "47",
					"FGA": "1615",
					"FGM": "104",
					"FG_PCT": "6",
					"FTA": "66",
					"FTM": "55",
					"FT_PCT": "83",
					"DREB": "96",
					"OREB": "10",
					"TREB": "106",
					"BLK": "22",
					"AST": "92",
					"STL": "24",
					"TOV": "68",
					"PTS": "2913",
					"MIN": "6060"
				},
				"Q1": {
					"FG3A": "8",
					"FG3M": "3",
					"FG3_PCT": "38",
					"FGA": "21",
					"FGM": "13",
					"FG_PCT": "62",
					"FTA": "2",
					"FTM": "1",
					"FT_PCT": "50",
					"DREB": "8",
					"OREB": "2",
					"TREB": "10",
					"BLK": "5",
					"AST": "10",
					"STL": "2",
					"TOV": "6",
					"PTS": "30",
					"MIN": "60"
				},
				"Q2": {
					"FG3A": "2",
					"FG3M": "0",
					"FG3_PCT": "0",
					"FGA": "15",
					"FGM": "8",
					"FG_PCT": "53",
					"FTA": "12",
					"FTM": "8",
					"FT_PCT": "67",
					"DREB": "10",
					"OREB": "1",
					"TREB": "11",
					"BLK": "1",
					"AST": "7",
					"STL": "1",
					"TOV": "4",
					"PTS": "24",
					"MIN": "60"
				},
				"Q3": {
					"FG3A": "8",
					"FG3M": "4",
					"FG3_PCT": "50",
					"FGA": "16",
					"FGM": "10",
					"FG_PCT": "62",
					"FTA": "6",
					"FTM": "5",
					"FT_PCT": "83",
					"DREB": "9",
					"OREB": "1",
					"TREB": "10",
					"BLK": "2",
					"AST": "9",
					"STL": "2",
					"TOV": "6",
					"PTS": "29",
					"MIN": "60"
				},
				"Q4": {
					"FG3A": "5",
					"FG3M": "0",
					"FG3_PCT": "0",
					"FGA": "15",
					"FGM": "4",
					"FG_PCT": "27",
					"FTA": "6",
					"FTM": "5",
					"FT_PCT": "83",
					"DREB": "6",
					"OREB": "0",
					"TREB": "6",
					"BLK": "2",
					"AST": "2",
					"STL": "4",
					"TOV": "8",
					"PTS": "13",
					"MIN": "60"
				},
				"OT": {
					"FG3A": "0",
					"FG3M": "0",
					"FG3_PCT": "0",
					"FGA": "0",
					"FGM": "0",
					"FG_PCT": "0",
					"FTA": "0",
					"FTM": "0",
					"FT_PCT": "0",
					"DREB": "0",
					"OREB": "0",
					"TREB": "0",
					"BLK": "0",
					"AST": "0",
					"STL": "0",
					"TOV": "0",
					"PTS": "0",
					"MIN": "0"
				}
			},
			"box_score": [
				{
					"first_name": "Tony",
					"last_name": "Wroten",
					"name": "Tony Wroten",
					"starter": "True",
					"MIN": "33",
					"FGM": "6",
					"FGA": "11",
					"FG_PCT": "55",
					"FG3M": "1",
					"FG3A": "4",
					"FG3_PCT": "25",
					"FTM": "8",
					"FTA": "11",
					"FT_PCT": "73",
					"OREB": "0",
					"DREB": "3",
					"TREB": "3",
					"AST": "10",
					"STL": "1",
					"BLK": "1",
					"TOV": "4",
					"PF": "1",
					"PTS": "21",
					"+/-": "-11",
					"DOUBLE": "double"
				},
				{
					"first_name": "Hollis",
					"last_name": "Thompson",
					"name": "Hollis Thompson",
					"starter": "True",
					"MIN": "32",
					"FGM": "4",
					"FGA": "8",
					"FG_PCT": "50",
					"FG3M": "2",
					"FG3A": "5",
					"FG3_PCT": "40",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "1",
					"TREB": "1",
					"AST": "2",
					"STL": "0",
					"BLK": "3",
					"TOV": "2",
					"PF": "2",
					"PTS": "10",
					"+/-": "-17",
					"DOUBLE": "none"
				},
				{
					"first_name": "Henry",
					"last_name": "Sims",
					"name": "Henry Sims",
					"starter": "True",
					"MIN": "27",
					"FGM": "4",
					"FGA": "9",
					"FG_PCT": "44",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "1",
					"FTA": "2",
					"FT_PCT": "50",
					"OREB": "1",
					"DREB": "3",
					"TREB": "4",
					"AST": "2",
					"STL": "0",
					"BLK": "1",
					"TOV": "0",
					"PF": "1",
					"PTS": "9",
					"+/-": "-10",
					"DOUBLE": "none"
				},
				{
					"first_name": "Nerlens",
					"last_name": "Noel",
					"name": "Nerlens Noel",
					"starter": "True",
					"MIN": "25",
					"FGM": "1",
					"FGA": "4",
					"FG_PCT": "25",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "5",
					"TREB": "5",
					"AST": "3",
					"STL": "1",
					"BLK": "1",
					"TOV": "3",
					"PF": "1",
					"PTS": "2",
					"+/-": "-19",
					"DOUBLE": "none"
				},
				{
					"first_name": "Luc",
					"last_name": "Mbah a Moute",
					"name": "Luc Mbah a Moute",
					"starter": "True",
					"MIN": "19",
					"FGM": "4",
					"FGA": "10",
					"FG_PCT": "40",
					"FG3M": "0",
					"FG3A": "2",
					"FG3_PCT": "0",
					"FTM": "1",
					"FTA": "2",
					"FT_PCT": "50",
					"OREB": "3",
					"DREB": "4",
					"TREB": "7",
					"AST": "3",
					"STL": "1",
					"BLK": "0",
					"TOV": "6",
					"PF": "3",
					"PTS": "9",
					"+/-": "-12",
					"DOUBLE": "none"
				},
				{
					"first_name": "Brandon",
					"last_name": "Davies",
					"name": "Brandon Davies",
					"starter": "False",
					"MIN": "23",
					"FGM": "7",
					"FGA": "9",
					"FG_PCT": "78",
					"FG3M": "1",
					"FG3A": "2",
					"FG3_PCT": "50",
					"FTM": "3",
					"FTA": "4",
					"FT_PCT": "75",
					"OREB": "0",
					"DREB": "3",
					"TREB": "3",
					"AST": "0",
					"STL": "3",
					"BLK": "0",
					"TOV": "3",
					"PF": "3",
					"PTS": "18",
					"+/-": "-1",
					"DOUBLE": "none"
				},
				{
					"first_name": "Chris",
					"last_name": "Johnson",
					"name": "Chris Johnson",
					"starter": "False",
					"MIN": "21",
					"FGM": "2",
					"FGA": "4",
					"FG_PCT": "50",
					"FG3M": "1",
					"FG3A": "3",
					"FG3_PCT": "33",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "2",
					"TREB": "2",
					"AST": "0",
					"STL": "3",
					"BLK": "0",
					"TOV": "2",
					"PF": "5",
					"PTS": "5",
					"+/-": "3",
					"DOUBLE": "none"
				},
				{
					"first_name": "K.J.",
					"last_name": "McDaniels",
					"name": "K.J. McDaniels",
					"starter": "False",
					"MIN": "20",
					"FGM": "2",
					"FGA": "4",
					"FG_PCT": "50",
					"FG3M": "1",
					"FG3A": "3",
					"FG3_PCT": "33",
					"FTM": "3",
					"FTA": "4",
					"FT_PCT": "75",
					"OREB": "0",
					"DREB": "1",
					"TREB": "1",
					"AST": "2",
					"STL": "0",
					"BLK": "3",
					"TOV": "2",
					"PF": "3",
					"PTS": "8",
					"+/-": "-10",
					"DOUBLE": "none"
				},
				{
					"first_name": "Malcolm",
					"last_name": "Thomas",
					"name": "Malcolm Thomas",
					"starter": "False",
					"MIN": "19",
					"FGM": "4",
					"FGA": "4",
					"FG_PCT": "100",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "9",
					"TREB": "9",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "0",
					"PF": "2",
					"PTS": "8",
					"+/-": "-6",
					"DOUBLE": "none"
				},
				{
					"first_name": "Alexey",
					"last_name": "Shved",
					"name": "Alexey Shved",
					"starter": "False",
					"MIN": "14",
					"FGM": "1",
					"FGA": "4",
					"FG_PCT": "25",
					"FG3M": "1",
					"FG3A": "4",
					"FG3_PCT": "25",
					"FTM": "3",
					"FTA": "3",
					"FT_PCT": "100",
					"OREB": "0",
					"DREB": "1",
					"TREB": "1",
					"AST": "6",
					"STL": "0",
					"BLK": "0",
					"TOV": "2",
					"PF": "0",
					"PTS": "6",
					"+/-": "-7",
					"DOUBLE": "none"
				},
				{
					"first_name": "JaKarr",
					"last_name": "Sampson",
					"name": "JaKarr Sampson",
					"starter": "False",
					"MIN": "2",
					"FGM": "0",
					"FGA": "0",
					"FG_PCT": "0",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "1",
					"TREB": "1",
					"AST": "0",
					"STL": "0",
					"BLK": "1",
					"TOV": "0",
					"PF": "0",
					"PTS": "0",
					"+/-": "0",
					"DOUBLE": "none"
				},
				{
					"first_name": "Michael",
					"last_name": "Carter-Williams",
					"name": "Michael Carter-Williams",
					"starter": "False",
					"MIN": "0",
					"FGM": "0",
					"FGA": "0",
					"FG_PCT": "0",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "0",
					"TREB": "0",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "0",
					"PF": "0",
					"PTS": "0",
					"+/-": "0",
					"DOUBLE": "none"
				}
			],
			"next_game": {
				"day": "3",
				"month": "November",
				"year": "2014",
				"dayname": "Monday",
				"stadium": "Wells Fargo Center",
				"city": "Philadelphia",
				"opponent_name": "Rockets",
				"opponent_place": "Houston",
				"is_home": "True"
			}
		},
		"vis": {
			"name": "Heat",
			"place": "Miami",
			"conference": "Eastern Conference",
			"division": "Southeast",
			"wins": "2",
			"losses": "0",
			"conference_standing": 1,
			"game_number": "2",
			"previous_game_id": "329",
			"next_game_id": "330",
			"line_score": {
				"game": {
					"FG3A": "24",
					"FG3M": "12",
					"FG3_PCT": "50",
					"FGA": "83",
					"FGM": "41",
					"FG_PCT": "49",
					"FTA": "29",
					"FTM": "20",
					"FT_PCT": "69",
					"DREB": "26",
					"OREB": "9",
					"TREB": "35",
					"BLK": "0",
					"AST": "33",
					"STL": "16",
					"TOV": "16",
					"PF": "20",
					"PTS": "114",
					"MIN": "4"
				},
				"H1": {
					"FG3A": "69",
					"FG3M": "44",
					"FG3_PCT": "64",
					"FGA": "2321",
					"FGM": "1110",
					"FG_PCT": "48",
					"FTA": "106",
					"FTM": "64",
					"FT_PCT": "60",
					"DREB": "35",
					"OREB": "23",
					"TREB": "58",
					"BLK": "00",
					"AST": "88",
					"STL": "53",
					"TOV": "34",
					"PTS": "3228",
					"MIN": "6060"
				},
				"H2": {
					"FG3A": "45",
					"FG3M": "22",
					"FG3_PCT": "49",
					"FGA": "1920",
					"FGM": "1010",
					"FG_PCT": "53",
					"FTA": "85",
					"FTM": "55",
					"FT_PCT": "65",
					"DREB": "612",
					"OREB": "22",
					"TREB": "634",
					"BLK": "00",
					"AST": "98",
					"STL": "35",
					"TOV": "36",
					"PTS": "2727",
					"MIN": "6060"
				},
				"Q1": {
					"FG3A": "6",
					"FG3M": "4",
					"FG3_PCT": "67",
					"FGA": "23",
					"FGM": "11",
					"FG_PCT": "48",
					"FTA": "10",
					"FTM": "6",
					"FT_PCT": "60",
					"DREB": "3",
					"OREB": "2",
					"TREB": "5",
					"BLK": "0",
					"AST": "8",
					"STL": "5",
					"TOV": "3",
					"PTS": "32",
					"MIN": "60"
				},
				"Q2": {
					"FG3A": "9",
					"FG3M": "4",
					"FG3_PCT": "44",
					"FGA": "21",
					"FGM": "10",
					"FG_PCT": "48",
					"FTA": "6",
					"FTM": "4",
					"FT_PCT": "67",
					"DREB": "5",
					"OREB": "3",
					"TREB": "8",
					"BLK": "0",
					"AST": "8",
					"STL": "3",
					"TOV": "4",
					"PTS": "28",
					"MIN": "60"
				},
				"Q3": {
					"FG3A": "4",
					"FG3M": "2",
					"FG3_PCT": "50",
					"FGA": "19",
					"FGM": "10",
					"FG_PCT": "53",
					"FTA": "8",
					"FTM": "5",
					"FT_PCT": "62",
					"DREB": "6",
					"OREB": "2",
					"TREB": "8",
					"BLK": "0",
					"AST": "9",
					"STL": "3",
					"TOV": "3",
					"PTS": "27",
					"MIN": "60"
				},
				"Q4": {
					"FG3A": "5",
					"FG3M": "2",
					"FG3_PCT": "40",
					"FGA": "20",
					"FGM": "10",
					"FG_PCT": "50",
					"FTA": "5",
					"FTM": "5",
					"FT_PCT": "100",
					"DREB": "12",
					"OREB": "2",
					"TREB": "14",
					"BLK": "0",
					"AST": "8",
					"STL": "5",
					"TOV": "6",
					"PTS": "27",
					"MIN": "60"
				},
				"OT": {
					"FG3A": "0",
					"FG3M": "0",
					"FG3_PCT": "0",
					"FGA": "0",
					"FGM": "0",
					"FG_PCT": "0",
					"FTA": "0",
					"FTM": "0",
					"FT_PCT": "0",
					"DREB": "0",
					"OREB": "0",
					"TREB": "0",
					"BLK": "0",
					"AST": "0",
					"STL": "0",
					"TOV": "0",
					"PTS": "0",
					"MIN": "0"
				}
			},
			"box_score": [
				{
					"first_name": "Chris",
					"last_name": "Bosh",
					"name": "Chris Bosh",
					"starter": "True",
					"MIN": "33",
					"FGM": "9",
					"FGA": "17",
					"FG_PCT": "53",
					"FG3M": "2",
					"FG3A": "5",
					"FG3_PCT": "40",
					"FTM": "10",
					"FTA": "11",
					"FT_PCT": "91",
					"OREB": "3",
					"DREB": "5",
					"TREB": "8",
					"AST": "4",
					"STL": "2",
					"BLK": "0",
					"TOV": "3",
					"PF": "2",
					"PTS": "30",
					"+/-": "10",
					"DOUBLE": "none"
				},
				{
					"first_name": "Dwyane",
					"last_name": "Wade",
					"name": "Dwyane Wade",
					"starter": "True",
					"MIN": "32",
					"FGM": "4",
					"FGA": "18",
					"FG_PCT": "22",
					"FG3M": "0",
					"FG3A": "1",
					"FG3_PCT": "0",
					"FTM": "1",
					"FTA": "3",
					"FT_PCT": "33",
					"OREB": "1",
					"DREB": "2",
					"TREB": "3",
					"AST": "10",
					"STL": "3",
					"BLK": "0",
					"TOV": "6",
					"PF": "1",
					"PTS": "9",
					"+/-": "13",
					"DOUBLE": "none"
				},
				{
					"first_name": "Luol",
					"last_name": "Deng",
					"name": "Luol Deng",
					"starter": "True",
					"MIN": "29",
					"FGM": "7",
					"FGA": "11",
					"FG_PCT": "64",
					"FG3M": "1",
					"FG3A": "3",
					"FG3_PCT": "33",
					"FTM": "0",
					"FTA": "1",
					"FT_PCT": "0",
					"OREB": "2",
					"DREB": "2",
					"TREB": "4",
					"AST": "2",
					"STL": "2",
					"BLK": "0",
					"TOV": "1",
					"PF": "0",
					"PTS": "15",
					"+/-": "4",
					"DOUBLE": "none"
				},
				{
					"first_name": "Shawne",
					"last_name": "Williams",
					"name": "Shawne Williams",
					"starter": "True",
					"MIN": "29",
					"FGM": "5",
					"FGA": "9",
					"FG_PCT": "56",
					"FG3M": "3",
					"FG3A": "5",
					"FG3_PCT": "60",
					"FTM": "2",
					"FTA": "2",
					"FT_PCT": "100",
					"OREB": "0",
					"DREB": "4",
					"TREB": "4",
					"AST": "4",
					"STL": "1",
					"BLK": "0",
					"TOV": "1",
					"PF": "4",
					"PTS": "15",
					"+/-": "16",
					"DOUBLE": "none"
				},
				{
					"first_name": "Norris",
					"last_name": "Cole",
					"name": "Norris Cole",
					"starter": "True",
					"MIN": "27",
					"FGM": "4",
					"FGA": "7",
					"FG_PCT": "57",
					"FG3M": "2",
					"FG3A": "4",
					"FG3_PCT": "50",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "1",
					"TREB": "1",
					"AST": "4",
					"STL": "2",
					"BLK": "0",
					"TOV": "0",
					"PF": "1",
					"PTS": "10",
					"+/-": "6",
					"DOUBLE": "none"
				},
				{
					"first_name": "Mario",
					"last_name": "Chalmers",
					"name": "Mario Chalmers",
					"starter": "False",
					"MIN": "25",
					"FGM": "6",
					"FGA": "9",
					"FG_PCT": "67",
					"FG3M": "2",
					"FG3A": "2",
					"FG3_PCT": "100",
					"FTM": "6",
					"FTA": "10",
					"FT_PCT": "60",
					"OREB": "0",
					"DREB": "2",
					"TREB": "2",
					"AST": "4",
					"STL": "4",
					"BLK": "0",
					"TOV": "0",
					"PF": "1",
					"PTS": "20",
					"+/-": "18",
					"DOUBLE": "none"
				},
				{
					"first_name": "Shabazz",
					"last_name": "Napier",
					"name": "Shabazz Napier",
					"starter": "False",
					"MIN": "20",
					"FGM": "2",
					"FGA": "3",
					"FG_PCT": "67",
					"FG3M": "1",
					"FG3A": "2",
					"FG3_PCT": "50",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "3",
					"TREB": "3",
					"AST": "4",
					"STL": "2",
					"BLK": "0",
					"TOV": "1",
					"PF": "4",
					"PTS": "5",
					"+/-": "11",
					"DOUBLE": "none"
				},
				{
					"first_name": "Chris",
					"last_name": "Andersen",
					"name": "Chris Andersen",
					"starter": "False",
					"MIN": "17",
					"FGM": "0",
					"FGA": "2",
					"FG_PCT": "0",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "1",
					"DREB": "2",
					"TREB": "3",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "0",
					"PF": "2",
					"PTS": "0",
					"+/-": "6",
					"DOUBLE": "none"
				},
				{
					"first_name": "Josh",
					"last_name": "McRoberts",
					"name": "Josh McRoberts",
					"starter": "False",
					"MIN": "11",
					"FGM": "1",
					"FGA": "3",
					"FG_PCT": "33",
					"FG3M": "0",
					"FG3A": "1",
					"FG3_PCT": "0",
					"FTM": "1",
					"FTA": "2",
					"FT_PCT": "50",
					"OREB": "0",
					"DREB": "3",
					"TREB": "3",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "2",
					"PF": "3",
					"PTS": "3",
					"+/-": "1",
					"DOUBLE": "none"
				},
				{
					"first_name": "James",
					"last_name": "Ennis",
					"name": "James Ennis",
					"starter": "False",
					"MIN": "7",
					"FGM": "2",
					"FGA": "3",
					"FG_PCT": "67",
					"FG3M": "1",
					"FG3A": "1",
					"FG3_PCT": "100",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "1",
					"DREB": "1",
					"TREB": "2",
					"AST": "1",
					"STL": "0",
					"BLK": "0",
					"TOV": "0",
					"PF": "1",
					"PTS": "5",
					"+/-": "2",
					"DOUBLE": "none"
				},
				{
					"first_name": "Justin",
					"last_name": "Hamilton",
					"name": "Justin Hamilton",
					"starter": "False",
					"MIN": "5",
					"FGM": "1",
					"FGA": "1",
					"FG_PCT": "100",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "1",
					"DREB": "1",
					"TREB": "2",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "1",
					"PF": "0",
					"PTS": "2",
					"+/-": "3",
					"DOUBLE": "none"
				},
				{
					"first_name": "Andre",
					"last_name": "Dawkins",
					"name": "Andre Dawkins",
					"starter": "False",
					"MIN": "1",
					"FGM": "0",
					"FGA": "0",
					"FG_PCT": "0",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "0",
					"TREB": "0",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "1",
					"PF": "1",
					"PTS": "0",
					"+/-": "0",
					"DOUBLE": "none"
				},
				{
					"first_name": "Shannon",
					"last_name": "Brown",
					"name": "Shannon Brown",
					"starter": "False",
					"MIN": "0",
					"FGM": "0",
					"FGA": "0",
					"FG_PCT": "0",
					"FG3M": "0",
					"FG3A": "0",
					"FG3_PCT": "0",
					"FTM": "0",
					"FTA": "0",
					"FT_PCT": "0",
					"OREB": "0",
					"DREB": "0",
					"TREB": "0",
					"AST": "0",
					"STL": "0",
					"BLK": "0",
					"TOV": "0",
					"PF": "0",
					"PTS": "0",
					"+/-": "0",
					"DOUBLE": "none"
				}
			],
			"next_game": {
				"day": "2",
				"month": "November",
				"year": "2014",
				"dayname": "Sunday",
				"stadium": "American Airlines Arena",
				"city": "Miami",
				"opponent_name": "Raptors",
				"opponent_place": "Toronto",
				"is_home": "True"
			}
		}
	},
	"summaries": [
		"The Miami Heat ( 20 ) defeated the Philadelphia 76ers ( 0 - 3 ) 114 - 96 on Saturday . Chris Bosh scored a game - high 30 points to go with eight rebounds in 33 minutes . Josh McRoberts made his Heat debut after missing the entire preseason recovering from toe surgery . McRoberts came off the bench and played 11 minutes . Shawne Williams was once again the starter at power forward in McRoberts ' stead . Williams finished with 15 points and three three - pointers in 29 minutes . Mario Chalmers scored 18 points in 25 minutes off the bench . Luc Richard Mbah a Moute replaced Chris Johnson in the starting lineup for the Sixers on Saturday . Hollis Thompson shifted down to the starting shooting guard job to make room for Mbah a Moute . Mbah a Moute finished with nine points and seven rebounds in 19 minutes . K.J . McDaniels , who suffered a minor hip flexor injury in Friday 's game , was available and played 21 minutes off the bench , finishing with eight points and three blocks . Michael Carter-Williams is expected to be out until Nov. 13 , but Tony Wroten continues to put up impressive numbers in Carter-Williams ' absence . Wroten finished with a double - double of 21 points and 10 assists in 33 minutes . The Heat will complete a back - to - back set at home Sunday against the Tornoto Raptors . The Sixers ' next game is at home Monday against the Houston Rockets ."
	]
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- Train: NBA seasons - 2014, 2015, & 2016; total instances - 3690
- Validation: NBA seasons - 2017; total instances - 1230
- Test: NBA seasons - 2018; total instances - 1230

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The splits were created as per different NBA seasons. All the games in regular season (no play-offs) are added in the dataset



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset contains a data analytics problem in the classic sense ([Reiter, 2007](https://aclanthology.org/W07-2315)).  That is, there is a large amount of data from which insights need to be selected.  Further, the insights should be both from simple shallow queries (such as dirext transcriptions of the properties of a subject, i.e., a player and their statistics), as well as aggregated (how a player has done over time).  There is far more on the data side than is required to be realised, and indeed, could be practically realised.  This depth of data analytics problem does not exist in other datasets.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Many, if not all aspects of data-to-text systems can be measured with this dataset.  It has complex data analytics, meaninful document planning (10-15 sentence documents with a narrative structure), as well as microplanning and realisation requirements.  Finding models to handle this volume of data, as well as methods for meaninfully evaluate generations is a very open question.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
For dataset discussion see [Thomson et al, 2020](https://aclanthology.org/2020.intellang-1.4/)

For evaluation see:
- [Thomson & Reiter 2020, Thomson & Reiter (2021)](https://aclanthology.org/2021.inlg-1.23)
- [Kasner et al (2021)](https://aclanthology.org/2021.inlg-1.25)

For a system using the relational database form of SportSett, see:
- [Thomson et al (2020)](https://aclanthology.org/2020.inlg-1.6/)

For recent systems using the Rotowire dataset, see:
- [Puduppully & Lapata (2021)](https://github.com/ratishsp/data2text-macro-plan-py)
- [Rebuffel et all (2020)](https://github.com/KaijuML/data-to-text-hierarchical)



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Many, if not all aspects of data-to-text systems can be measured with this dataset.  It has complex data analytics, meaninful document planning (10-15 sentence documents with a narrative structure), as well as microplanning and realisation requirements.  Finding models to handle this volume of data, as well as methods for meaninfully evaluate generations is a very open question.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
BLEU is the only off-the-shelf metric commonly used.  Works have also used custom metrics like RG ([Wiseman et al, 2017](https://aclanthology.org/D17-1239)), and a recent shared task explored other metrics and their corrolation with human evaluation ([Thomson & Reiter, 2021](https://aclanthology.org/2021.inlg-1.23)).

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Most results from prior works use the original Rotowire dataset, which has train/validation/test contamination.  For results of BLEU and RG on the relational database format of SportSett, as a guide, see [Thomson et al, 2020](https://aclanthology.org/2020.inlg-1.6).

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
The results on this dataset are largely unexplored, as is the selection of suitable metrics that correlate with human judgment.  See Thomson et al, 2021 (https://aclanthology.org/2021.inlg-1.23) for an overview, and  Kasner et al (2021) for the best performing metric at the time of writing (https://aclanthology.org/2021.inlg-1.25).



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The references texts were taken from the existing dataset RotoWire-FG ([Wang, 2019](https://www.aclweb.org/anthology/W19-8639)), which is in turn based on Rotowire ([Wiseman et al, 2017](https://aclanthology.org/D17-1239)).  The rationale behind this dataset was to re-structure the data such that aggregate statistics over multiple games, as well as upcoming game schedules could be included, moving the dataset from snapshots of single games, to a format where almost everything that could be present in the reference texts could be found in the data.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Create a summary of a basketball, with insightful facts about the game, teams, and players, both within the game, withing periods during the game, and over the course of seasons/careers where appropriate.  This is a data-to-text problem in the classic sense ([Reiter, 2007](https://aclanthology.org/W07-2315)) in that it has a difficult data analystics state, in addition to ordering and transcription of selected facts.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
RotoWire-FG (https://www.rotowire.com).
Wikipedia (https://en.wikipedia.org/wiki/Main_Page)
Basketball Reference (https://www.basketball-reference.com)



### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Multiple websites`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
None

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Summaries of basketball games (in the NBA).

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
It retains the original tokenization scheme employed by Wang 2019

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
manually

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Games from the 2014 through 2018 seasons were selected.  Within these seasons games are not filtered, all are present, but this was an arbitrary solution from the original RotoWirte-FG dataset.


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
The dataset consits of a pre-existing dataset, as well as publically available facts.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
unlikely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
yes

#### Links and Summaries of Analysis Work

<!-- info: Provide links to and summaries of works analyzing these biases. -->
<!-- scope: microscope -->
Unaware of any work, but, this is a dataset considting solely of summaries of mens professional basketball games.  It does not cover different levels of the sport, or different genders, and all pronouns are likely to be male unless a specific player is referred to by other pronouns in the training text.  This makes it difficult to train systems where gender can be specified as an attribute, although it is an interesting, open problem that could be investigated using the dataset.

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
No, it is very specifically American English from the sports journalism domain.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
All information relating to persons is of public record.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`public domain`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
SportSett resolved the major overlap problems of RotoWire, although some overlap is unavoidable.  For example, whilst it is not possible to find career totals and other historic information for all players (the data only goes back to 2014), it is possible to do so for some players.  It is unavoidable that some data which is aggregated, exists in its base form in previous partitions.  The season-based partition scheme heavily constrains this however.

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Factual accuray continues to be a problem, systems may incorrectly represent the facts of the game.  

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
Using the RG metric to maximise the number of true facts in a generate summary is not nececeraly  


