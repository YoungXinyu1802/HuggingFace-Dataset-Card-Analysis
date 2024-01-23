---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- crowdsourced
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: sci_NER_naacl
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- acl
- sciBERT
- sci
- acl
- '11711'
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for [naacl2022]

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

This is a named entity recognition dataset annotated for the science entity recognition task, a [project](https://github.com/neubig/nlp-from-scratch-assignment-2022) from the CMU 11-711 course.

### Supported Tasks and Leaderboards

NER task.

### Languages

English

## Dataset Structure

### Data Instances

A sample of the dataset
{'id': '0',
'tokens': ['We', 'sample', '50', 'negative', 'cases', 'from', 'T5LARGE', '+', 'GenMC', 'for', 'each', 'dataset'],
'ner_tags':['O', 'O', 'O', 'O', 'O', 'O', 'B-MethodName', 'O', 'B-MethodName', 'O', 'O', 'O']}

### Data Fields

id,tokens,ner_tags

- `id`: a `string` feature give the sample index.
- `tokens`: a `list` of `string` features give the sequence.
- `ner_tags`: a `list` of classification labels for each token in the sentence, with possible values including 
`O` (0), `B-MethodName` (1), `I-MethodName` (2), `B-HyperparameterName` (3),`I-HyperparameterName` (4),`B-HyperparameterValue` (5),`I-HyperparameterValue` (6),`B-MetricName` (7),`I-MetricName` (8),`B-MetricValue` (9),`I-MetricValue` (10),`B-TaskName` (11),`I-TaskName` (12),`B-DatasetName` (13),`I-DatasetName` (14).


### Data Splits

Data split into
train.txt
dev.txt
test.txt

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

The data is annotated by using labelstudio, the papers are collected from TACL and ACL 2022 conferences.

#### Who are the annotators?

Xiaoyue Cui and Haotian Teng annotated the datasets.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@xcui297](https://github.com/xcui297); [@haotianteng](https://github.com/haotianteng) for adding this dataset.
