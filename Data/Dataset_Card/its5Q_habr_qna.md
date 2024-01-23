---
annotations_creators:
- crowdsourced
language:
- ru
language_creators:
- crowdsourced
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Habr QnA
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- text-generation
- question-answering
task_ids:
- language-modeling
- open-domain-qa
---

# Dataset Card for Habr QnA

## Table of Contents
- [Dataset Card for Habr QnA](#dataset-card-for-habr-qna)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)

## Dataset Description

- **Repository:** https://github.com/its5Q/habr-qna-parser

### Dataset Summary

This is a dataset of questions and answers scraped from [Habr QnA](https://qna.habr.com/). There are 723430 asked questions with answers, comments and other metadata. 

### Languages

The dataset is mostly Russian with source code in different languages.

## Dataset Structure

### Data Fields

Data fields can be previewed on the dataset card page.

### Data Splits

All 723430 examples are in the train split, there is no validation split.

## Dataset Creation

The data was scraped with a script, located in [my GitHub repository](https://github.com/its5Q/habr-qna-parser)

## Additional Information

### Dataset Curators

- https://github.com/its5Q