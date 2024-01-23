---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: Wikidisamb Dataset with Descriptions
size_categories:
-  100K<n<1M
source_datasets: []
task_categories:
- named-entity-disambiguation
task_ids:
- wikidata-disambiguation
---


# Dataset Card for "Widdd"


## Dataset Description

WiDDD stands for WIkiData Disambig with Descriptions. The former dataset comes from [Cetoli & al](https://arxiv.org/pdf/1810.09164.pdf)  paper, and is aimed at solving Named Entity Disambiguation. This datasets tries to extract relevant information from entities descriptions only, instead of working with graphs. In order to do so, we mapped every Wikidata id (correct id and wrong id) in the original paper with its WikiData description. If not found, row is discarded for the 1.+ versions.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

english

## Dataset Structure

We show detailed information for up to 5 configurations of the dataset.

### Data Instances

#### plain_text

- **Size of downloaded dataset files:** 46.64 MB

An example of 'train' looks as follows.
```
{'example_id': 11,
 'string': 'pausanias',
 'text': ' mention the spear, which he would indeed have touched with excitement. But it was being shown in the time of Pausanias in the second century AD. Achilles and ',
 'correct_id': 'Q192931',
 'wrong_id': 'Q941521',
 'correct_description': 'ancient Greek geographer, travel writer and mythographer',
 'wrong_description': 'Wikimedia disambiguation page'}
```

### Data Fields

The data fields are the same among all splits.

#### plain_text
- `example_id`: an `int32` feature,
- `string`: a `string` feature,
- `text`: a `string` feature,
- `correct_id`: a `string` feature,
- `wrong_id`: a `string` feature,
- `correct_description`: a `string` feature,
- `wrong_description`: a `string` feature,


### Data Splits

|   name   |train|validation|test|
|----------|----:|-----:|-----:|
|plain_text|96523|9609|9584|

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


### Contributions
