---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- crowdsourced
license:
- gpl
multilinguality:
- monolingual
pretty_name: InfantBooks
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- research paper
- kids
- children
- books
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Dataset Card for InfantBooks

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [https://www.mpi-inf.mpg.de/children-texts-for-commonsense](https://www.mpi-inf.mpg.de/children-texts-for-commonsense)
- **Paper:** Do Children Texts Hold The Key To Commonsense Knowledge?

### Dataset Summary

A dataset of infants/children's books.


### Languages

All the books are in English;

## Dataset Structure

### Data Instances

malis-friend_BookDash-FKB.txt,"Then a taxi driver, hooting around the yard with his wire car. Mali enjoys playing by himself..."

### Data Fields

- title: The title of the book
- content: The content of the book

## Dataset Creation

### Curation Rationale

The goal of the dataset is to study infant books, which are supposed to be easier to understand than normal texts. In particular, the original goal was to study if these texts contain more commonsense knowledge.

### Source Data

#### Initial Data Collection and Normalization

We automatically collected kids' books on the web.

#### Who are the source language producers?

Native speakers.

### Citation Information

```
Romero, J., & Razniewski, S. (2022).
Do Children Texts Hold The Key To Commonsense Knowledge?
In Proceedings of the 2022 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning.
```
