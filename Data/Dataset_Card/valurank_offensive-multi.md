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
This dataset contains a collection of text labeled as offensive (class 1) or not (class 0).

## Dataset Creation
The dataset was creating by aggregating multiple publicly available datasets.

### Source Data
The following datasets were used:
* https://huggingface.co/datasets/hate_speech_offensive - Tweet text cleaned by lower casing, removing mentions and urls. Dropped instanced labeled as 'hate speech'
* https://sites.google.com/site/offensevalsharedtask/olid - Tweet text cleaned by lower casing, removing mentions and urls. Used 'subtask_a' column for labeling.
