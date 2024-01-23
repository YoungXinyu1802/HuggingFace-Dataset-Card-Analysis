---
annotations_creators:
- expert-created
language_creators:
- unknown
language:
- fi
license:
- cc-by-nc-sa-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: turku_hockey_data2text
tags:
- data-to-text
---

# Dataset Card for GEM/turku_hockey_data2text

## Dataset Description

- **Homepage:** https://turkunlp.org/hockey_data2text.html
- **Repository:** https://github.com/TurkuNLP/Turku-hockey-data2text
- **Paper:** https://aclanthology.org/W19-6125/
- **Leaderboard:** N/A
- **Point of Contact:** Jenna Kanerva, Filip Ginter

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/turku_hockey_data2text).

### Dataset Summary 

This is a Finnish data-to-text dataset in which the input is structured information about a hockey game and the output a description of the game.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/turku_hockey_data2text')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/turku_hockey_data2text).

#### website
[Website](https://turkunlp.org/hockey_data2text.html)

#### paper
[ACL anthology](https://aclanthology.org/W19-6125/)

#### authors
Jenna Kanerva, Samuel Rönnqvist, Riina Kekki, Tapio Salakoski, Filip Ginter (TurkuNLP / University of Turku)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://turkunlp.org/hockey_data2text.html)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/TurkuNLP/Turku-hockey-data2text)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL anthology](https://aclanthology.org/W19-6125/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{kanerva2019newsgen,
  Title = {Template-free Data-to-Text Generation of Finnish Sports News},
  Author = {Jenna Kanerva and Samuel R{\"o}nnqvist and Riina Kekki and Tapio Salakoski and Filip Ginter},
  booktitle = {Proceedings of the 22nd Nordic Conference on Computational Linguistics (NoDaLiDa’19)},
  year={2019}
  }
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Jenna Kanerva, Filip Ginter

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
jmnybl@utu.fi, figint@utu.fi

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
written standard language

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Finnish`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The original news articles are written by professional journalists. The text passages extracted in the annotation may be slightly edited compared to the original language during the corpus annotation.

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-nc-sa-4.0: Creative Commons Attribution Non Commercial Share Alike 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
This dataset was developed as a benchmark for evaluating template-free, machine learning methods on Finnish news generation in the area of ice hockey reporting.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Describe an event from an ice hockey game based on the given structural data.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
University of Turku

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Jenna Kanerva, Samuel Rönnqvist, Riina Kekki, Tapio Salakoski, Filip Ginter (TurkuNLP / University of Turku)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
The project was supported by the Google Digital News Innovation Fund.

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Jenna Kanerva, Filip Ginter (TurkuNLP / University of Turku)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
The dataset is constructed of games, where each game is a list of events. If the event was annotated (corresponding sentence was found from the news article), it includes `text` field with value other than empty string ("").

For each game (dict), there are keys `gem_id` (string), `id` (string), `news_article` (string), and `events` (list).

For each event (dict), there are different, relevant keys available with non empty values depending on the event type (e.g. goal or penalty). The mandatory keys for each event are `event_id` (string), `event_type` (string), `text` (string, empty string if not annotated), and `multi_reference` (bool). The keys not relevant for the specific event type are left empty.

The relevant keys in the event dictionary are:

For each event type, the following keys are relevant:
  `event_id`: Identifier of the event, unique to the game but not globally, in chronological order (string)
  `event_type`: Type of the event, possible values are `game result`, `goal`, `penalty`, or `saves` (string)
  `text`: Natural language description of the event, or empty string if not available (string)
  `multi_reference`: Does this event refer to a text passage describing multiple events? (bool)


The rest of the fields are specific to the event type. The relevant fields for each event type are:

game result:
  `event_id`: Identifier of the event, unique to the game but not globally, in chronological order (string)
  `event_type`: Type of the event (string)
  `home_team`: Name of the home team (string)
  `guest_team`: Name of the guest team (string)
  `score`: Final score of the game, in the form of home–guest (string)
  `periods`: Scores for individual periods, each in the form of home–guest score in that period (list of strings)
  `features`: Additional features, such as overtime win or shoot out (list of strings)
  `text`: Natural language description of the event, or empty string if not available (string)
  `multi_reference`: Does this event refer to a text passage describing multiple events? (bool)

goal:
  `event_id`: Identifier of the event, unique to the game but not globally, in chronological order (string)
  `event_type`: Type of the event (string)
  `player`: Name of the player scoring (string)
  `assist`: Names of the players assisting, at most two players (list of strings)
  `team`: Team scoring with possible values of `home` or `guest` (string)
  `team_name`: Name of the team scoring (string)
  `score`: Score after the goal, in the form of home–guest (string)
  `time`: Time of the goal, minutes and seconds from the beginning (string)
  `features`: Additional features, such as power play or short-handed goal (list of strings)
  `text`: Natural language description of the event, or empty string if not available (string)
  `multi_reference`: Does this event refer to a text passage describing multiple events? (bool)

penalty:
  `event_id`: Identifier of the event, unique to the game but not globally, in chronological order (string)
  `event_type`: Type of the event (string)
  `player`: Name of the player getting the penalty (string)
  `team`: Team getting the penalty with possible values of `home` or `guest` (string)
  `team_name`: Name of the team getting the penalty (string)
  `penalty_minutes`: Penalty minutes (string)
  `time`: Time of the penalty, minutes and seconds from the beginning (string)
  `text`: Natural language description of the event, or empty string if not available (string)
  `multi_reference`: Does this event refer to a text passage describing multiple events? (bool)

saves:
 `event_id`: Identifier of the event, unique to the game but not globally, in chronological order (string)
  `event_type`: Type of the event (string)
  `player`: Name of the goalkeeper (string)
  `team`: Team of the goalkeeper with possible values of `home` or `guest` (string)
  `team_name`: Name of the team (string)
  `saves`: Number of saves in the game (string)
  `text`: Natural language description of the event, or empty string if not available (string)
  `multi_reference`: Does this event refer to a text passage describing multiple events? (bool)


Text passages describing multiple events (multi_reference):

Some text passages refer to multiple events in such way that separating them to individual statements is not adequate (e.g. "The home team received two penalties towards the end of the first period."). In these cases, multiple events are aligned to the same text passage so that the first event (in chronological order) include the annotated text passage, while the rest of the events referring to the same text passage include the identifier of the first event in the annotated text field (e.g. `text`: "E4").

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  'gem_id': 'gem-turku_hockey_data2text-train-0',
  'id': '20061031-TPS-HPK',
  'news_article': 'HPK:n hyvä syysvire jatkuu jääkiekon SM-liigassa. Tiistaina HPK kukisti mainiolla liikkeellä ja tehokkaalla ylivoimapelillä TPS:n vieraissa 1–0 (1–0, 0–0, 0–0).\nHPK hyödynsi ylivoimaa mennen jo ensimmäisessä erässä Mikko Mäenpään maalilla 1–0 -johtoon.\nToisessa ja kolmannessa erässä HPK tarjosi edelleen TPS:lle runsaasti tilanteita, mutta maalia eivät turkulaiset millään ilveellä saaneet. Pahin este oli loistavan pelin Hämeenlinnan maalilla pelannut Mika Oksa.\nTPS:n maalissa Jani Hurme ei osumille mitään mahtanut. Joukkueen suuri yksinäinen kenttäpelaaja oli Kai Nurminen, mutta hänelläkään ei ollut onnea maalitilanteissa.',
  'events':
    {
      'event_id': ['E1', 'E2', 'E3'],
      'event_type': ['game result', 'penalty', 'goal'],
      'text': ['HPK kukisti TPS:n vieraissa 1–0 (1–0, 0–0, 0–0).', '', 'HPK hyödynsi ylivoimaa mennen jo ensimmäisessä erässä Mikko Mäenpään maalilla 1–0 -johtoon.'],
      'home_team': ['TPS', '', ''],
      'guest_team': ['HPK', '', ''],
      'score': ['0–1', '', '0–1'],
      'periods': [['0–1', '0–0', '0–0'], [], []],
      'features': [[], [], ['power play']],
      'player': ['', 'Fredrik Svensson', 'Mikko Mäenpää'],
      'assist': [[], [], ['Jani Keinänen', 'Toni Mäkiaho']],
      'team': ['', 'guest', 'guest'],
      'team_name': ['', 'HPK', 'HPK'],
      'time': ['', '9.28', '14.57'],
      'penalty_minutes': ['', '2', ''],
      'saves': ['', '', ''],
      'multi_reference': [false, false, false]
    }
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The corpus include 3 splits: train, validation, and test.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The dataset was created to develop machine learned text generation models for Finnish ice hockey news, where the generation would reflect the natural language variation found from the game reports written by professional journalists. While the original game reports often include additional information not derivable from the game statistics, the corpus was fully manually curated to remove all such  information from the natural language descriptions. The rationale of such curation was to prevent model 'hallucinating' additional facts.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
yes

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
This is the only data2text corpus for Finnish in GEM.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
morphological inflection, language variation


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points modified`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
Structural data was translated into English.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task




## Previous Results

### Previous Results

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `METEOR`, `ROUGE`, `WER`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Automatic evaluation: BLEU, NIST, METEOR, ROUGE-L, CIDEr
Manual evaluation: factual mistakes, grammatical errors, minimum edit distance to an acceptable game report (using WER)

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset is designed for text generation (data2text), where the original source of natural language descriptions is news articles written by journalists. While the link between structural data (ice hockey game statistics) and the news articles describing the game  was quite weak (news articles including a lot of information not derivable from the statistics, while leaving many events unmentioned), the corpus includes full manual annotation aligning the events extracted from game statistics and the corresponding natural language passages extracted from the news articles.

Each event is manually aligned into a sentence-like passage, and in case a suitable passage was not found, the annotation is left empty (with value `None`). The extracted passages were manually modified not to include additional information not derivable from the game statistics, or not considered as world knowledge. The manual curation of passages is designed to prevent model hallucination, i.e. model learning to generate facts not derivable from the input data.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Describing the given events (structural data) in natural language, and therefore generating ice hockey game reports.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Other`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The initial data, both game statistics and news articles, were obtained from the Finnish News Agency STT news archives released for academic use (http://urn.fi/urn:nbn:fi:lb-2019041501). The original news articles are written by professional journalists.

We (TurkuNLP) gratefully acknowledge the collaboration of Maija Paikkala, Salla Salmela and Pihla Lehmusjoki from the Finnish News Agency STT while creating the corpus.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Ice hockey, news

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Include only games, where both game statistics and a news article describing the game were available (based on timestamps and team names).


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
expert created

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
1

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Members of the TurkuNLP research group, native speakers of Finnish.

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
1

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
1

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
Manual alignment of events and their natural language descriptions. Removing information not derivable from the input data or world knowledge in order to prevent the model 'hallucination'.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by data curators

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Manual inspection of examples during the initial annotation training phrase.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
The corpus license was agreed with the providers of the source material.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
yes/very likely

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
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The dataset represents only written standard language. 



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
None


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`non-commercial use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`non-commercial use only`


### Known Technical Limitations



