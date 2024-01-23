---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- ro
license:
- apache-2.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- hate-speech-detection
pretty_name: RO-FB-Offense
extra_gated_prompt: 'Warning: this repository contains harmful content (abusive language,
  hate speech).'
tags:
- hate-speech-detection
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

- **Homepage:** [https://github.com/readerbench/ro-fb-offense](https://github.com/readerbench/ro-fb-offense)
- **Repository:** [https://github.com/readerbench/ro-fb-offense](https://github.com/readerbench/ro-fb-offense)
- **Paper:** FB-RO-Offense – A Romanian Dataset and Baseline Models for detecting Offensive Language in Facebook Comments
- **Point of Contact:** [Andrei Paraschiv](https://github.com/AndyTheFactory)

### Dataset Summary

FB-RO-Offense corpus, an offensive speech dataset containing 4,455 user-generated comments from Facebook live broadcasts available in Romanian

The annotation follows the hierarchical tagset proposed in the Germeval 2018 Dataset. 
The following Classes are available:
  * OTHER: Non-Offensive Language
  * OFFENSIVE:
    - PROFANITY
    - INSULT
    - ABUSE
    
### Languages

Romanian

## Dataset Structure


### Data Instances


An example of 'train' looks as follows.

```
{
  'sender': '$USER1208', 
  'no_reacts': 1,
  'text': 'PLACEHOLDER TEXT', 
  'label': OTHER, 
}
```


### Data Fields

- `sender`: a `string` feature.
- 'no_reacts': a `integer`
- `text`: a `string`.
- `label`: categorical `OTHER`, `PROFANITY`, `INSULT`, `ABUSE`


### Data Splits

|  name   |train|test|
|---------|----:|---:|
|ro|x|x|


## Dataset Creation

### Curation Rationale

Collecting data for abusive language classification for Romanian Language.

### Source Data

Facebook comments

#### Initial Data Collection and Normalization



#### Who are the source language producers?

Social media users

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
@inproceedings{busuioc2022fb-ro-offense,
  title={FB-RO-Offense – A Romanian Dataset and Baseline Models for detecting Offensive Language in Facebook Comments},
  author={ Busuioc, Gabriel-Razvan and Paraschiv, Andrei and Dascalu, Mihai},
  booktitle={International Symposium on Symbolic and Numeric Algorithms for Scientific Computing (SYNASC) 2022},
  year={2022}
}

```


### Contributions


