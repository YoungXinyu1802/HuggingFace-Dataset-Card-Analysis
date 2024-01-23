---
language:
- en
paperswithcode_id: funsd
---

# Dataset Card for "FUNSD"

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

### Dataset Summary

The [FUNSD](https://guillaumejaume.github.io/FUNSD/) dataset, with one difference compared to the original dataset, each document image is resized to 224x224.

The FUNSD dataset is a collection of annotated forms.

This dataset loading script is taken from the [official LayoutLMv2 implementation](https://github.com/microsoft/unilm/blob/master/layoutlmft/layoutlmft/data/datasets/funsd.py), and updated to not include any Detectron2 dependencies.


### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

We show detailed information for up to 5 configurations of the dataset.

### Data Instances

#### conll2000

- **Size of downloaded dataset files:** 3.32 MB
- **Size of the generated dataset:** 6.25 MB
- **Total amount of disk used:** 9.57 MB

An example of 'train' looks as follows.
```
This example was too long and was cropped:

{
    "chunk_tags": [11, 13, 11, 12, 21, 22, 22, 22, 22, 11, 12, 12, 17, 11, 12, 13, 11, 0, 1, 13, 11, 11, 0, 21, 22, 22, 11, 12, 12, 13, 11, 12, 12, 11, 12, 12, 0],
    "id": "0",
    "pos_tags": [19, 14, 11, 19, 39, 27, 37, 32, 34, 11, 15, 19, 14, 19, 22, 14, 20, 5, 15, 14, 19, 19, 5, 34, 32, 34, 11, 15, 19, 14, 20, 9, 20, 24, 15, 22, 6],
    "tokens": "[\"Confidence\", \"in\", \"the\", \"pound\", \"is\", \"widely\", \"expected\", \"to\", \"take\", \"another\", \"sharp\", \"dive\", \"if\", \"trade\", \"figur..."
}
```

### Data Fields

The data fields are the same among all splits.

### Data Splits

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

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
@article{DBLP:journals/corr/abs-1905-13538,
  author    = {Guillaume Jaume and
               Hazim Kemal Ekenel and
               Jean{-}Philippe Thiran},
  title     = {{FUNSD:} {A} Dataset for Form Understanding in Noisy Scanned Documents},
  journal   = {CoRR},
  volume    = {abs/1905.13538},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.13538},
  archivePrefix = {arXiv},
  eprint    = {1905.13538},
  timestamp = {Mon, 03 Jun 2019 13:42:33 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-13538.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

```


### Contributions

Thanks to [@vblagoje](https://github.com/vblagoje), [@jplu](https://github.com/jplu) for adding this dataset.