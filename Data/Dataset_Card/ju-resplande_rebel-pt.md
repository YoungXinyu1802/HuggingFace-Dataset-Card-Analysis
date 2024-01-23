---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- pt
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- extended|rebel-dataset
task_categories:
- text-retrieval
- text2text-generation
task_ids: []
pretty_name: rebel-portuguese
tags:
- relation-extraction
- conditional-text-generation
---
# Dataset Card for REBEL-Portuguese

## Table of Contents

- [Dataset Card for REBEL-Portuguese](#dataset-card-for-rebel)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Repository:** [https://github.com/Babelscape/rebel](https://github.com/Babelscape/rebel)
- **Paper:** [https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf)
- **Point of Contact:** [julianarsg13@gmail.com](julianarsg13@gmail.com)

### Dataset Summary

Dataset adapted to Portuguese from [REBEL-dataset](https://huggingface.co/datasets/Babelscape/rebel-dataset) .

### Supported Tasks and Leaderboards

- `text-retrieval-other-relation-extraction`: The dataset can be used to train a model for Relation Extraction, which consists in extracting triplets from raw text, made of subject, object and relation type.

### Languages

The dataset is in Portuguese, from the Portuguese Wikipedia.

## Dataset Structure

### Data Instances

### Data Fields

### Data Splits

## Dataset Creation

### Curation Rationale

### Source Data

Data comes from Wikipedia text before the table of contents, as well as Wikidata for the triplets annotation.

#### Initial Data Collection and Normalization

For the data collection, the dataset extraction pipeline [cRocoDiLe: Automati**c** **R**elati**o**n Extra**c**ti**o**n **D**ataset w**i**th N**L**I filt**e**ring](https://github.com/Babelscape/crocodile) insipired by [T-REx Pipeline](https://github.com/hadyelsahar/RE-NLG-Dataset) more details found at: [T-REx Website](https://hadyelsahar.github.io/t-rex/). The starting point is a Wikipedia dump as well as a Wikidata one.
After the triplets are extracted, an NLI system was used to filter out those not entailed by the text.

#### Who are the source language producers?

Any Wikipedia and Wikidata contributor.

### Annotations

#### Annotation process

The dataset extraction pipeline [cRocoDiLe: Automati**c** **R**elati**o**n Extra**c**ti**o**n **D**ataset w**i**th N**L**I filt**e**ring](https://github.com/ju-resplande/crocodile).

#### Who are the annotators?

Automatic annottations

### Personal and Sensitive Information

All text is from Wikipedia, any Personal or Sensitive Information there may be present in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

Not for now

## Additional Information

### Dataset Curators

### Licensing Information

### Citation Information

### Contributions

Thanks to [@ju-resplande](https://github.com/ju-resplade) for adding this dataset.
