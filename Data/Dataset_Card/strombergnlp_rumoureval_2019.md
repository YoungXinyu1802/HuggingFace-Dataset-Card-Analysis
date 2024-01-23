---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- text-classification
task_ids:
- fact-checking
pretty_name: RumourEval 2019
tags:
- stance-detection
---



# Dataset Card for "rumoureval_2019"

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

- **Homepage:** [https://competitions.codalab.org/competitions/19938](https://competitions.codalab.org/competitions/19938)
- **Repository:** [https://figshare.com/articles/dataset/RumourEval_2019_data/8845580](https://figshare.com/articles/dataset/RumourEval_2019_data/8845580)
- **Paper:** [https://aclanthology.org/S19-2147/](https://aclanthology.org/S19-2147/), [https://arxiv.org/abs/1809.06683](https://arxiv.org/abs/1809.06683)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:**  

### Dataset Summary

Stance prediction task in English. The goal is to predict whether a given reply to a claim either supports, denies, questions, or simply comments on the claim. Ran as a SemEval task in 2019.

### Supported Tasks and Leaderboards

* SemEval 2019 task 1

### Languages

English of various origins, bcp47: `en`

## Dataset Structure

### Data Instances

#### polstance

An example of 'train' looks as follows.

```
{
	'id': '0', 
	'source_text': 'Appalled by the attack on Charlie Hebdo in Paris, 10 - probably journalists - now confirmed dead. An attack on free speech everywhere.', 
	'reply_text': '@m33ryg @tnewtondunn @mehdirhasan Of course it is free speech, that\'s the definition of "free speech" to openly make comments or draw a pic!', 
	'label': 3
}
```


### Data Fields

- `id`: a `string` feature.
- `source_text`: a `string` expressing a claim/topic.
- `reply_text`: a `string` to be classified for its stance to the source.
- `label`: a class label representing the stance the text expresses towards the target. Full tagset with indices:

```
                            0: "support",
                            1: "deny",
                            2: "query",
                            3: "comment"
```
- `quoteID`: a `string` of the internal quote ID.
- `party`: a `string` describing the party affiliation of the quote utterer at the time of utterance.
- `politician`: a `string` naming the politician who uttered the quote.

### Data Splits

|  name   |instances|
|---------|----:|
|train|7 005|
|dev|2 425|
|test|2 945|

## Dataset Creation

### Curation Rationale


### Source Data

#### Initial Data Collection and Normalization


#### Who are the source language producers?

Twitter users

### Annotations

#### Annotation process

Detailed in [Analysing How People Orient to and Spread Rumours in Social Media by Looking at Conversational Threads](https://journals.plos.org/plosone/article/authors?id=10.1371/journal.pone.0150989)

#### Who are the annotators?


### Personal and Sensitive Information


## Considerations for Using the Data

### Social Impact of Dataset


### Discussion of Biases


### Other Known Limitations

## Additional Information

### Dataset Curators

The dataset is curated by the paper's authors.

### Licensing Information

The authors distribute this data under Creative Commons attribution license, CC-BY 4.0. 

### Citation Information

```
@inproceedings{gorrell-etal-2019-semeval,
    title = "{S}em{E}val-2019 Task 7: {R}umour{E}val, Determining Rumour Veracity and Support for Rumours",
    author = "Gorrell, Genevieve  and
      Kochkina, Elena  and
      Liakata, Maria  and
      Aker, Ahmet  and
      Zubiaga, Arkaitz  and
      Bontcheva, Kalina  and
      Derczynski, Leon",
    booktitle = "Proceedings of the 13th International Workshop on Semantic Evaluation",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/S19-2147",
    doi = "10.18653/v1/S19-2147",
    pages = "845--854",
}
```


### Contributions

Author-added dataset [@leondz](https://github.com/leondz)
