---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license:
- gpl-3.0
multilinguality:
- monolingual
pretty_name: Social Media Abuse
size_categories:
- n<1K
source_datasets:
- original
tags:
- 'abuse classification

  text classification'
task_categories:
- text-classification
task_ids:
- hate-speech-detection
- sentiment-classification
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 948
    num_examples: 22
  - name: validation
    num_bytes: 129.27272727272728
    num_examples: 3
  download_size: 1240
  dataset_size: 1077.2727272727273
---

# Dataset Card for Social Media Abuse

<!-- ## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** -->

### Dataset Summary

This is a dataset to use with a **SetFit** model to generate more examples of online social media abuse. This replicates a dataset you would see from a moderation company, such as Crisp Thinking (https://www.crispthinking.com/) who have data trained on billions of various risk types on social media. 

The dataset here is a mocked example of this to prove the efficacy of the SetFit model on a sentiment classification task. 

### Supported Tasks and Leaderboards

This is to be used for *text-classification*. 

### Languages

Contains only `en` abusive sentiments. 

## Dataset Structures

### Data Fields

This contains 2 fields:
1. text
2. label

### Data Splits

This contains a single training split, as the volumes are low 8 positive examples and 8 negative examples. 

<!-- ## Dataset Creation -->

<!-- ### Curation Rationale

[More Information Needed] -->

<!-- ### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed] -->

<!-- ### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed] -->

## Considerations for Using the Data

### Social Impact of Dataset

This dataset, or similar, could be used for social media moderation and risk detection purposes. 

### Discussion of Biases

Biased to a fixed number of examples and have been dummy generated. 

## Additional Information

### Dataset Curators

Gary Hutson

### Licensing Information

GNU V3 Public Licence. 

### Citation Information

Hutson, G. (2023). *Social Media Abuse dataset*.

### Contributions

Thanks to [StatsGary](https://github.com/StatsGary) for adding this dataset.