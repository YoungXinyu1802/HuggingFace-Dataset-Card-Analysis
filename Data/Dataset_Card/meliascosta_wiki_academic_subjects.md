---
license: cc-by-3.0
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- crowdsourced
multilinguality:
- monolingual
paperswithcode_id: wikitext-2
pretty_name: Wikipedia Outline of Academic Disciplines
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- hierarchical
- academic
- tree
- dag
- topics
- subjects
task_categories:
- text-classification
task_ids:
- multi-label-classification
---

# Dataset Card for Wiki Academic Disciplines`

## Table of Contents
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
- **Point of Contact:**

### Dataset Summary

This dataset was created from the [English wikipedia](https://meta.wikimedia.org/wiki/Data_dump_torrents#English_Wikipedia) dump of January 2022.
The main goal was to train a hierarchical classifier of academic subjects using [HiAGM](https://github.com/Alibaba-NLP/HiAGM). 

### Supported Tasks and Leaderboard

Text classification - No leaderboard at the moment.

### Languages

English

## Dataset Structure

The dataset consists of groups of labeled text chunks (tokenized by spaces and with stopwords removed). 
Labels are organized in a hieararchy (a DAG with a special Root node) of academic subjects.
Nodes correspond to entries in the [outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines) article from Wikipedia.

### Data Instances

Data is split in train/test/val each on a separate `.jsonl` file. Label hierarchy is listed a as TAB separated adjacency list on a `.taxonomy` file.
### Data Fields

JSONL files contain only two fields: a "token" field which holds the text tokens and a "label" field which holds a list of labels for that text.

### Data Splits

80/10/10 TRAIN/TEST/VAL schema

## Dataset Creation

All texts where extracted following the linked articles on [outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines)

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Wiki Dump

#### Who are the source language producers?

Wikipedia community.

### Annotations

#### Annotation process

Texts where automatically assigned to their linked academic discipline 

#### Who are the annotators?

Wikipedia Community.

### Personal and Sensitive Information

All information is public.

## Considerations for Using the Data

### Social Impact of Dataset



### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

Creative Commons 3.0 (see [Wikipedia:Copyrights](https://en.wikipedia.org/wiki/Wikipedia:Copyrights))

### Citation Information

1. Zhou, Jie, et al. "Hierarchy-aware global model for hierarchical text classification." Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. 2020.

### Contributions

Thanks to [@meliascosta](https://github.com/meliascosta) for adding this dataset.
