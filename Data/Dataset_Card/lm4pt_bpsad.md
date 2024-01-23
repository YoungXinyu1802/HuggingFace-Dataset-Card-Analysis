---
annotations_creators: []
language:
- pt
language_creators:
- other
license:
- unknown
multilinguality:
- monolingual
pretty_name: bpsad
size_categories:
- 1M<n<10M
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
- sentiment-classification
- sentiment-scoring
- sentiment-analysis
---

# Dataset Card for Brazilian Portuguese Sentiment Analysis Dataset

## Table of Contents
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

- **Homepage:** [Kaggle Dataset](https://www.kaggle.com/datasets/fredericods/ptbr-sentiment-analysis-datasets)
- **Paper:** [Sentiment Analysis on Brazilian Portuguese User Reviews](https://ieeexplore.ieee.org/abstract/document/9769838)
- **Point of Contact:** [Frederico Dias Souza](fredericods@poli.ufrj.br)

### Dataset Summary

**Disclaimer:** *The team releasing the dataset did not write a dataset card
for this dataset so this dataset card has been written by the contributors.*

The Brazilian Portuguese Sentiment Analysis Dataset (BPSAD) is composed
by the concatenation of 5 differents sources (Olist, B2W Digital, Buscapé,
UTLC-Apps and UTLC-Movies), each one is composed by evaluation sentences
classified according to the polarity (0: negative; 1: positive) and ratings
(1, 2, 3, 4 and 5 stars).

This dataset requires manual download:
1. Download the `concatenated` file from dataset homepage.
2. Extract the file inside `<path/to/manual/data>`.
3. Load the dataset using the command:
```python
datasets.load_dataset(
    path="lm4pt/bpsad",
    name='<polarity|rating>',
    data_dir='<path/to/manual/data>')
```

A detailed description about the dataset and the processing steps can be
found at the [dataset homepage](https://www.kaggle.com/datasets/fredericods/ptbr-sentiment-analysis-datasets).


### Supported Tasks and Leaderboards

The dataset contains two configurations that represents the possible tasks
related to sentiment analysis. The polarity classification is a binary
classification problem where the sentences must be classified as positive (1)
or negative (0) reviews. The rating prediction is a multiclass problem
with values ranging from 1 to 5 stars.


### Languages

The texts are in Brazilian Portuguese, as spoken by users of different e-commerces and Filmow social network.

## Dataset Structure

### Data Instances

#### polarity

```
{
    "review_text": "Bem macio e felpudo...recomendo.  Preço imbatível e entrega rápida. Compraria outro quando precisar",
    "polarity": 1
}
```

#### rating

```
{
    "review_text": "Bem macio e felpudo...recomendo.  Preço imbatível e entrega rápida. Compraria outro quando precisar",
    "rating": 4
}
```

### Data Fields

#### polarity
- `review_text`: a `string` feature with product or movie review.
- `polarity`: an `integer` value that represents positive (1) or negative (0) reviews.

#### rating

- `review_text`: a `string` feature with product or movie review.
- `rating`: an `integer` value that represents the number of stars given by the reviewer. Possible values are 1, 2, 3, 4 and 5.

### Data Splits

Data splits are created based on the original `kfold` column of each configuration, following the original authors recomendations:
- train: folds 1 to 8
- validation: fold 9
- test: fold 10

|          |  train  | validation |  test  |
|----------|--------:|-----------:|-------:|
| polarity | 1908937 |     238614 | 238613 |
|   rating | 2228877 |     278608 | 278607 |

More information about sentence size and label distribution can be found in the [dataset homepage](https://www.kaggle.com/datasets/fredericods/ptbr-sentiment-analysis-datasets).

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@inproceedings{souza2021sentiment,
    author={
        Souza, Frederico Dias and
        Baptista de Oliveira e Souza Filho, João},
    booktitle={
        2021 IEEE Latin American Conference on
        Computational Intelligence (LA-CCI)}, 
    title={
        Sentiment Analysis on Brazilian Portuguese User Reviews}, 
    year={2021},
    pages={1-6},
    doi={10.1109/LA-CCI48322.2021.9769838}
}
```

### Contributions

Thanks to [@guilhermelmello](https://huggingface.co/guilhermelmello) and [@DominguesPH](https://huggingface.co/DominguesPH) for adding this dataset.