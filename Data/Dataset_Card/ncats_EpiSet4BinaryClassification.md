---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- unknown
paperswithcode_id: glue
pretty_name: GLUE (General Language Understanding Evaluation benchmark)
---

# DOCUMENTATION UPDATES IN PROGRESS! IGNORE BELOW

# Dataset Card for GLUE

## Table of Contents
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
  - [Annotations](#annotations)
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

- **Homepage:** [https://nyu-mll.github.io/CoLA/](https://nyu-mll.github.io/CoLA/)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 955.33 MB
- **Size of the generated dataset:** 229.68 MB
- **Total amount of disk used:** 1185.01 MB

### Dataset Summary

GLUE, the General Language Understanding Evaluation benchmark (https://gluebenchmark.com/) is a collection of resources for training, evaluating, and analyzing natural language understanding systems.

### Supported Tasks and Leaderboards

The leaderboard for the GLUE benchmark can be found [at this address](https://gluebenchmark.com/). It comprises the following tasks:

#### cola

The Corpus of Linguistic Acceptability consists of English acceptability judgments drawn from books and journal articles on linguistic theory. Each example is a sequence of words annotated with whether it is a grammatical English sentence.

### Languages

The language data in  is in English 

## Dataset Structure

### Data Instances

#### cola

- **Size of downloaded dataset files:** 0.36 MB
- **Size of the generated dataset:** 0.58 MB
- **Total amount of disk used:** 0.94 MB

An example of 'train' looks as follows.
```
{
  "sentence": "Our friends won't buy this analysis, let alone the next one we propose.",
  "label": 1,
  "id": 0
}
```


### Data Fields

The data fields are the same among all splits.

#### cola
- `abstract`: a `string` feature.
- `label`: a classification label, with possible values including `unacceptable` (0), `acceptable` (1).
- `idx`: a `int32` feature.

### Data Splits

|train|validation|test|
|----:|---------:|---:|
| 8551|      1043|1063|

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

Rare Disease Curators from the [National Institutes of Health (NIH) Genetic and Rare Diseases Information Center (GARD)](https://rarediseases.info.nih.gov/)

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

Rare Disease Curators from the [National Institutes of Health (NIH) Genetic and Rare Diseases Information Center (GARD)](https://rarediseases.info.nih.gov/)

### Licensing Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information
```
@inproceedings{john2021recurrent,
  title={Recurrent Neural Networks to Automatically Identify Rare Disease Epidemiologic Studies from PubMed},
  author={John, Jennifer N and Sid, Eric and Zhu, Qian},
  booktitle={AMIA Annual Symposium Proceedings},
  volume={2021},
  pages={325},
  year={2021},
  organization={American Medical Informatics Association}
}
```


### Contributions

Thanks to [@patpizio](https://github.com/patpizio), [@jeswan](https://github.com/jeswan), [@thomwolf](https://github.com/thomwolf), [@patrickvonplaten](https://github.com/patrickvonplaten), [@mariamabarham](https://github.com/mariamabarham) for adding this dataset.

```
from datasets import load_dataset
epiclassify = load_dataset("ncats/EpiSet4BinaryClassification")
```