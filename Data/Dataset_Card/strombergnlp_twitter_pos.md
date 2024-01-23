---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- part-of-speech
paperswithcode_id: ritter-pos
pretty_name: Twitter Part-of-speech
---

# Dataset Card for "twitter-pos"

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

- **Homepage:** [https://gate.ac.uk/wiki/twitter-postagger.html](https://gate.ac.uk/wiki/twitter-postagger.html)
- **Repository:** [https://github.com/GateNLP/gateplugin-Twitter](https://github.com/GateNLP/gateplugin-Twitter)
- **Paper:** [https://aclanthology.org/R13-1026/](https://aclanthology.org/R13-1026/)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 51.96 MiB
- **Size of the generated dataset:** 251.22 KiB
- **Total amount of disk used:** 52.05 MB

### Dataset Summary

Part-of-speech information is basic NLP task. However, Twitter text
is difficult to part-of-speech tag: it is noisy, with linguistic errors and idiosyncratic style.
This dataset contains two datasets for English PoS tagging for tweets:

* Ritter, with train/dev/test
* Foster, with dev/test

Splits defined in the Derczynski paper, but the data is from Ritter and Foster.

* Ritter: [https://aclanthology.org/D11-1141.pdf](https://aclanthology.org/D11-1141.pdf), 
* Foster: [https://www.aaai.org/ocs/index.php/ws/aaaiw11/paper/download/3912/4191](https://www.aaai.org/ocs/index.php/ws/aaaiw11/paper/download/3912/4191)

### Supported Tasks and Leaderboards

* [Part of speech tagging on Ritter](https://paperswithcode.com/sota/part-of-speech-tagging-on-ritter)

### Languages

English, non-region-specific. `bcp47:en`

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.

```
{'id': '0', 'tokens': ['Antick', 'Musings', 'post', ':', 'Book-A-Day', '2010', '#', '243', '(', '10/4', ')', '--', 'Gray', 'Horses', 'by', 'Hope', 'Larson', 'http://bit.ly/as8fvc'], 'pos_tags': [23, 23, 22, 9, 23, 12, 22, 12, 5, 12, 6, 9, 23, 23, 16, 23, 23, 51]}
```


### Data Fields

The data fields are the same among all splits.

#### twitter-pos
- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `pos_tags`: a `list` of classification labels (`int`). Full tagset with indices:

```python

```


### Data Splits

|  name   |tokens|sentences|
|---------|----:|---------:|
|ritter train|10652|551|
|ritter dev  |2242|118|
|ritter test |2291|118|
|foster dev  |2998|270|
|foster test |2841|250|

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


### Citation Information

```
@inproceedings{ritter2011named,
  title={Named entity recognition in tweets: an experimental study},
  author={Ritter, Alan and Clark, Sam and Etzioni, Oren and others},
  booktitle={Proceedings of the 2011 conference on empirical methods in natural language processing},
  pages={1524--1534},
  year={2011}
}

@inproceedings{foster2011hardtoparse,
  title={\# hardtoparse: POS Tagging and Parsing the Twitterverse},
  author={Foster, Jennifer and Cetinoglu, Ozlem and Wagner, Joachim and Le Roux, Joseph and Hogan, Stephen and Nivre, Joakim and Hogan, Deirdre and Van Genabith, Josef},
  booktitle={Workshops at the Twenty-Fifth AAAI Conference on Artificial Intelligence},
  year={2011}
}

@inproceedings{derczynski2013twitter,
  title={Twitter part-of-speech tagging for all: Overcoming sparse and noisy data},
  author={Derczynski, Leon and Ritter, Alan and Clark, Sam and Bontcheva, Kalina},
  booktitle={Proceedings of the international conference recent advances in natural language processing ranlp 2013},
  pages={198--206},
  year={2013}
}

```


### Contributions

Author uploaded ([@leondz](https://github.com/leondz))