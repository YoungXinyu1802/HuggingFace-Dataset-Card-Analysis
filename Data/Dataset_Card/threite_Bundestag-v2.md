---
annotations_creators: []
language:
- de
language_creators:
- expert-generated
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Bundestag-v2
size_categories:
- 100K<n<1M
source_datasets: []
tags: ['Bundestag', 'ParlSpeech']
task_categories:
- text-classification
task_ids:
- entity-linking-classification
---

# Dataset Card for Bundestag-v2

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
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
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

- Homepage: https://doi.org/10.7910/DVN/L4OAKN

### Dataset Summary

This dataset was generated from the [ParlSpeech V2](https://doi.org/10.7910/DVN/L4OAKN) dataset. It contains speeches from the german parliament from 1990 until 2020 labelled with the party of the speaker.

### Supported Tasks

Text Classification

### Languages

German

## Dataset Structure

### Data Fields

- text: Transcript of the speech in german
- party: Party of the speaker

### Data Splits

- train
- validation
- test

## Dataset Creation

### Curation Rationale

Created to train a language model, which is able to classify speeches by party.

### Source Data

#### Initial Data Collection and Normalization

- [ParlSpeech V2](https://doi.org/10.7910/DVN/L4OAKN)

## Considerations for Using the Data

### Social Impact of Dataset

These are political speeches, therefor the content can be controversial and potentially harmful.

## Additional Information

### Licensing Information

[CCO 1.0](http://creativecommons.org/publicdomain/zero/1.0)

### Citation Information

Bibtex entry:
```
@data{DVN/L4OAKN_2020,
author = {Rauh, Christian and Schwalbach, Jan},
publisher = {Harvard Dataverse},
title = {{The ParlSpeech V2 data set: Full-text corpora of 6.3 million parliamentary speeches in the key legislative chambers of nine representative democracies}},
year = {2020},
version = {V1},
doi = {10.7910/DVN/L4OAKN},
url = {https://doi.org/10.7910/DVN/L4OAKN}
}
```