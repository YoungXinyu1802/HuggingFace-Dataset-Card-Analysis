---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- sk
license:
- unknown
multilinguality:
- monolingual
pretty_name: 'conll-2003-sk-ner'
size_categories:
- 10K<n<100K
source_datasets:
- extended|conll2003
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
- part-of-speech-tagging
---

# Dataset Card for [Dataset Name]

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Source Data](#source-data)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)




## Dataset Description
This is translated version of the original CONLL2003 dataset (translated from English to Slovak via Google translate) Annotation was done mostly automatically with word matching scripts. Records where some tags were not matched, were annotated manually (10%) Unlike the original Conll2003 dataset, this one contains only NER tags

- **Point of Contact: [@ju-bezdek](https://github.com/ju-bezdek) **


### Supported Tasks and Leaderboards

NER

labels:

- 0: O
- 1: B-PER
- 2: I-PER
- 3: B-ORG
- 4: I-ORG
- 5: B-LOC
- 6: I-LOC
- 7: B-MISC
- 8: I-MISC

### Languages

sk

## Dataset Structure

### Data Splits

train, test, val

## Dataset Creation

### Source Data
https://huggingface.co/datasets/conll2003

### Annotations

#### Annotation process

- Machine Translation
- Machine pairing tags with reverse translation, and hardcoded rules (including phrase regex matching etc.)
- Manual annotation of records that couldn't be automatically matched
