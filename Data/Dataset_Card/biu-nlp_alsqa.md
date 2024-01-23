---
pretty_name: ALSQA
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license: apache-2.0
multilinguality:
- monolingual
size_categories:
- <1000
source_datasets:
- original
task_categories:
- question-answering
- text-classification
task_ids:
- open-domain-qa
- extractive-qa
paperswithcode_id: alsqa
dataset_info:
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  config_name: alsqa
---

# Dataset Card for "alsqa"

## Table of Contents
- [Dataset Card for "alsqa"](#dataset-card-for-alsqa)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [squad_v2](#squad_v2)
    - [Data Fields](#data-fields)
      - [squad_v2](#squad_v2-1)
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

- **Homepage:** [https://github.com/elronbandel/lexical-generalization](https://github.com/elronbandel/lexical-generalization)
- **Repository:** [https://github.com/elronbandel/lexical-generalization](https://github.com/elronbandel/lexical-generalization)
- **Paper:** [Lexical Generalization Improves with Larger Models and Longer Training](https://arxiv.org/abs/2210.12673)
- **Point of Contact:** [https://github.com/elronbandel/lexical-generalization](https://github.com/elronbandel/lexical-generalization)
- **Size of downloaded dataset files:** 100 KB
- **Size of the generated dataset:** 1 MB
- **Total amount of disk used:** 1 MB

### Dataset Summary

To test the lexical overlap heuristic utilization in Reading Comprehension models, we create a new test set: Analyzing Lexically Similar QA (ALSQA).
We augment the SQuAD 2.0 dataset (Rajpurkar et al., 2018) by asking crowdworkers to generate questions with high context-overlap from questions with low overlap (These questions are paraphrases of the original questions).
In the case of un-answerable questions, annotators were asked to re-write the question without changing its meaning and maintain the unanswerability reason.3 ALSQA contains 365 questions pairs, 190 with an- swer and 174 without answer.

## Dataset Structure

Identical to squad v2

#
### Data Fields

The data fields are the same among all splits.

#### alsqa
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

### Data Splits

| name     |  test |
| -------- | -----: | 
| squad_v2 | 365 |  

## Dataset Creation

### Curation Rationale

### Source Data
squad_v2
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

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
@misc{https://doi.org/10.48550/arxiv.2210.12673,
  doi = {10.48550/ARXIV.2210.12673},
  url = {https://arxiv.org/abs/2210.12673},
  author = {Bandel, Elron and Goldberg, Yoav and Elazar, Yanai},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Lexical Generalization Improves with Larger Models and Longer Training},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```


### Contributions

Thanks to [@elronbandel](https://github.com/elronbandel) for adding this dataset.