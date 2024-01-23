---
language:
- en
license: other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- derived
task_categories:
- text-classification
---

# Dataset Card for hate-multi

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)

## Dataset Description

### Dataset Summary

This dataset contains a collection of text labeled as hate speech (class 1) or not (class 0).

## Dataset Creation

The dataset was creating by aggregating multiple publicly available datasets.

### Source Data

The following datasets were used:
* https://huggingface.co/datasets/hate_speech18 - Filtered to remove examples labeled as 'idk/skip', 'relation'
* https://huggingface.co/datasets/hate_speech_offensive - Tweet text cleaned by lower casing, removing mentions and urls. Dropped instanced labeled as 'offensive language'
* https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech - Tweet text cleaned by lower casing, removing mentions and urls. Dropped instanced with hatespeech == 1
