---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- other
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: cSQuAD1
size_categories: []
source_datasets: []
tags: []
task_categories:
- question-answering
task_ids: []
---

# Dataset Card for cSQuAD1

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

A contrast set generated from the eval set of SQuAD. Questions and answers were modified
to help detecting dataset artifacts. This dataset only contains a validation set, which
should only be used to evaluate a model.

### Supported Tasks

Question Answering (SQuAD).

### Languages

English

## Dataset Structure

### Data Instances

Dataset contains 100 instances

### Data Fields
| Field    | Description                                      |
|----------|--------------------------------------------------
| id       | Id of document containing context                |
| title    | Title of the document                            |
| context  | The context of the question                      |
| question | The question to answer                           |
| answers  | A list of possible answers from the context      |
| answer_start | The index in context where the answer starts |

### Data Splits

A single `eval` split is provided

## Dataset Creation

Dataset was created by modifying a sample of 100 examples from SQuAD test split.

## Additional Information

### Licensing Information

Apache 2.0 license

### Citation Information

TODO: add citations