---
annotations_creators:
- expert-generated
language:
- es
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: MEDDOCAN
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- clinical
- protected health information
- health records
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for "meddocan"

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
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

- **Homepage:** [https://temu.bsc.es/meddocan/index.php/datasets/](https://temu.bsc.es/meddocan/index.php/datasets/)
- **Repository:** [https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN](https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN)
- **Paper:** [http://ceur-ws.org/Vol-2421/MEDDOCAN_overview.pdf](http://ceur-ws.org/Vol-2421/MEDDOCAN_overview.pdf)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

A personal upload of the SPACC_MEDDOCAN corpus. The tokenization is made with the help of a custom [spaCy](https://spacy.io/) pipeline.

### Supported Tasks and Leaderboards

Name Entity Recognition

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Data Fields

The data fields are the same among all splits.

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|meddocan|10312|5268|5155|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

From the [SPACCC_MEDDOCAN: Spanish Clinical Case Corpus - Medical Document Anonymization](https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN) page:

> This work is licensed under a Creative Commons Attribution 4.0 International License.
>
> You are free to: Share — copy and redistribute the material in any medium or format Adapt — remix, transform, and build upon the material for any purpose, even commercially. Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
>
> For more information, please see https://creativecommons.org/licenses/by/4.0/

### Citation Information

```
@inproceedings{Marimon2019AutomaticDO,
  title={Automatic De-identification of Medical Texts in Spanish: the MEDDOCAN Track, Corpus, Guidelines, Methods and Evaluation of Results},
  author={Montserrat Marimon and Aitor Gonzalez-Agirre and Ander Intxaurrondo and Heidy Rodriguez and Jose Lopez Martin and Marta Villegas and Martin Krallinger},
  booktitle={IberLEF@SEPLN},
  year={2019}
}

```

### Contributions

Thanks to [@GuiGel](https://github.com/GuiGel) for adding this dataset.