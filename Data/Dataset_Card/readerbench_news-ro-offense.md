---
license: apache-2.0
annotations_creators:
- expert-generated
language_creators:
- found
task_categories:
- text-classification
language:
- ro
multilinguality:
- monolingual
source_datasets:
- original
tags:
- hate-speech-detection
task_ids:
- hate-speech-detection
pretty_name: News-RO-Offense
size_categories:
- 1K<n<10K
extra_gated_prompt: 'Warning: this repository contains harmful content (abusive language,
  hate speech).'
---


# Dataset Card for "RO-FB-Offense"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://github.com/readerbench/news-ro-offense](https://github.com/readerbench/news-ro-offense)
- **Repository:** [https://github.com/readerbench/news-ro-offense](https://github.com/readerbench/news-ro-offense)
- **Paper:** News-RO-Offense - A Romanian Offensive Language Dataset and Baseline Models Centered on News Article Comments
- **Point of Contact:** [Andrei Paraschiv](https://github.com/AndyTheFactory)

### Dataset Summary
a novel Romanian language dataset for offensive message detection with manually 
annotated comment from a local Romanian news website (stiri de cluj) into five classes:

* non-offensive
* targeted insults
* racist
* homophobic
* sexist

Resulting in 4052 annotated messages

### Languages

Romanian

## Dataset Structure


### Data Instances


An example of 'train' looks as follows.

```
{
  'comment_id': 5,
  'reply_to_comment_id':2,
  'comment_nr': 1,
  'content_id': 23,
  'comment_text':'PLACEHOLDER TEXT',
  'LABEL': 3
}
```


### Data Fields

- `comment_id`: The unique comment ID,
- `reply_to_comment_id`: contains the header comment, if part of a conversation tree, otherwise empty
- `comment_nr`: the comments current number on the article
- `content_id`: the article ID
- `comment_text`: full comment text
- `LABEL`: 0 = Non-offensive, 1 = Targeted insult, 2 = Racist, 3 = Homophobic, 4 = Sexist

### Data Splits

|  name   |train|test|
|---------|----:|---:|
|ro|x|x|


## Dataset Creation

### Curation Rationale

Collecting data for abusive language classification for Romanian Language.

### Source Data

News Articles comments

#### Initial Data Collection and Normalization



#### Who are the source language producers?

News Article readers

### Annotations


#### Annotation process



#### Who are the annotators?

Native speakers

### Personal and Sensitive Information

The data was public at the time of collection. No PII removal has been performed.

## Considerations for Using the Data



### Social Impact of Dataset

The data definitely contains abusive language. The data could be used to develop and propagate offensive language against every target group involved, i.e. ableism, racism, sexism, ageism, and so on.

### Discussion of Biases


### Other Known Limitations


## Additional Information


### Dataset Curators


### Licensing Information

This data is available and distributed under Apache-2.0 license

### Citation Information

```
@misc{cojocaru2022news,
	title        = {News-RO-Offense - A Romanian Offensive Language Dataset and Baseline Models Centered on News Article Comments},
	author       = {Cojocaru, Andreea and Paraschiv, Andrei and Dascălu, Mihai},
	year         = 2022,
	journal      = {RoCHI - International Conference on Human-Computer Interaction},
	publisher    = {MATRIX ROM},
	doi          = {10.37789/rochi.2022.1.1.12},
	url          = {http://dx.doi.org/10.37789/rochi.2022.1.1.12}
}


```


### Contributions
