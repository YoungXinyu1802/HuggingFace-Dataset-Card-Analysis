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
pretty_name: Yandex.Q
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

# Dataset Card for Yandex.Q

## Table of Contents
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
  - [Citation Information](#citation-information)

## Dataset Description

- **Repository:** https://github.com/its5Q/yandex-q

### Dataset Summary

This is a dataset of questions and answers scraped from [Yandex.Q](https://yandex.ru/q/). There are 836810 answered questions out of the total of 1297670.
The full dataset that includes all metadata returned by Yandex.Q APIs and contains unanswered questions can be found in `full.jsonl.gz`

### Languages

The dataset is mostly in Russian, but there may be other languages present

## Dataset Structure

### Data Fields

The dataset consists of 3 fields:
- `question` - question title (`string`)
- `description` - question description (`string` or `null`)
- `answer` - answer to the question (`string`)

### Data Splits

All 836810 examples are in the train split, there is no validation split.

## Dataset Creation

The data was scraped through some "hidden" APIs using several scripts, located in [my GitHub repository](https://github.com/its5Q/yandex-q)

## Additional Information

### Dataset Curators

- https://github.com/its5Q
