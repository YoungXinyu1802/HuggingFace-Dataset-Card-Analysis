---
annotations_creators:
- no-annotation
language:
- py
language_creators:
- found
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- code-generation
- conditional-text-generation
task_ids:
- language-modeling
- code-generation
---

# Dataset Card for notional-python

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://notional.ai/
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The Notional-python dataset contains python code files from 100 well-known repositories gathered from Google Bigquery Github Dataset. The dataset was created to test the ability of programming language models.
Follow [our repo]() to do the model evaluation using notional-python dataset.

### Languages

Python

## Dataset Creation

### Curation Rationale

Notional-python was built to provide a dataset for testing the ability of the machine to generate python code.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by filtering code from [Google Bigquery Github data](https://cloud.google.com/blog/topics/public-datasets/github-on-bigquery-analyze-all-the-open-source-code)
In order to improve the quality of the dataset, only python code files that meet the below conditions are added to the dataset:
- Code with more than 60% of executable lines
- Code with logic, not config files or comment-only files
- Code with more than 30% of attribute declaration lines (E.G.: Some files contain just only class names and their class attributes, usually used for configuration of the project, these files were not selected)
- Code without `TODO` and `FIXME`.

#### Who are the source language producers?

The producers are users of github.
