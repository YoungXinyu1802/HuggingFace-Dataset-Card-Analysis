---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- extended|qa_srl
task_categories:
- text-retrieval
task_ids: []
pretty_name: LSOIE
tags:
- Open Information Extraction
---

# Dataset Card for LSOIE

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://github.com/Jacobsolawetz/large-scale-oie
- **Repository:** https://github.com/Jacobsolawetz/large-scale-oie
- **Paper:** https://arxiv.org/abs/2101.11177
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The Large Scale Open Information Extraction Dataset (LSOIE), is a dataset 20 times larger than the next largest human-annotated Open Information Extraction (OIE) dataset. LSOIE is a built upon the QA-SRL 2.0 dataset by transforming the list of Questions and answers for each predicate to a tuple representing a fact.

### Supported Tasks and Leaderboards

Open Information Extraction

### Languages

The text in this dataset is english.

## Dataset Structure

### Data Instances

A datapoint comprises one fact together with the sentence it was extracted from. There can be multiple facts for each Sentence. Each fact is represented by a tuple $(a_0, p, a_1,\dots a_n)$ where $a_0$ is the head entity $p$ is the predicate and $a_1, \dots,a_n$ represent the tail.

### Data Fields

- word_ids : sequence of indices (int) representing tokens in a sentence,
- words : a sequence of strings, the tokens in the sentence,
- pred : the predicate of the fact,
- pred_ids : ids of the tokens in the predicate,
- head_pred_id : id of the head token in the predicate,
- sent_id : sentence id,
- run_id : ,
- label : Sequence of tags (BIO) representing the fact, e.g. if the fact is given by $(a_0, p, a_1, \dots, a_n) $

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]