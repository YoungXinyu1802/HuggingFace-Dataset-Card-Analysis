---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
- topic-classification
pretty_name: GuardianAuthorship
dataset_info:
- config_name: cross_topic_1
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 677054
    num_examples: 112
  - name: test
    num_bytes: 1283126
    num_examples: 207
  - name: validation
    num_bytes: 374390
    num_examples: 62
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_genre_1
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 406144
    num_examples: 63
  - name: test
    num_bytes: 1657512
    num_examples: 269
  - name: validation
    num_bytes: 677054
    num_examples: 112
  download_size: 3100749
  dataset_size: 2740710
- config_name: cross_topic_2
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 677054
    num_examples: 112
  - name: test
    num_bytes: 1104764
    num_examples: 179
  - name: validation
    num_bytes: 552752
    num_examples: 90
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_3
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 677054
    num_examples: 112
  - name: test
    num_bytes: 927138
    num_examples: 152
  - name: validation
    num_bytes: 730378
    num_examples: 117
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_4
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 374390
    num_examples: 62
  - name: test
    num_bytes: 1283126
    num_examples: 207
  - name: validation
    num_bytes: 677054
    num_examples: 112
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_5
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 374390
    num_examples: 62
  - name: test
    num_bytes: 1407428
    num_examples: 229
  - name: validation
    num_bytes: 552752
    num_examples: 90
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_6
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 374390
    num_examples: 62
  - name: test
    num_bytes: 1229802
    num_examples: 202
  - name: validation
    num_bytes: 730378
    num_examples: 117
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_7
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 552752
    num_examples: 90
  - name: test
    num_bytes: 1104764
    num_examples: 179
  - name: validation
    num_bytes: 677054
    num_examples: 112
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_8
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 552752
    num_examples: 90
  - name: test
    num_bytes: 1407428
    num_examples: 229
  - name: validation
    num_bytes: 374390
    num_examples: 62
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_9
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 552752
    num_examples: 90
  - name: test
    num_bytes: 1051440
    num_examples: 174
  - name: validation
    num_bytes: 730378
    num_examples: 117
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_10
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 730378
    num_examples: 117
  - name: test
    num_bytes: 927138
    num_examples: 152
  - name: validation
    num_bytes: 677054
    num_examples: 112
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_11
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 730378
    num_examples: 117
  - name: test
    num_bytes: 1229802
    num_examples: 202
  - name: validation
    num_bytes: 374390
    num_examples: 62
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_topic_12
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 730378
    num_examples: 117
  - name: test
    num_bytes: 1051440
    num_examples: 174
  - name: validation
    num_bytes: 552752
    num_examples: 90
  download_size: 3100749
  dataset_size: 2334570
- config_name: cross_genre_2
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 406144
    num_examples: 63
  - name: test
    num_bytes: 1960176
    num_examples: 319
  - name: validation
    num_bytes: 374390
    num_examples: 62
  download_size: 3100749
  dataset_size: 2740710
- config_name: cross_genre_3
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 406144
    num_examples: 63
  - name: test
    num_bytes: 1781814
    num_examples: 291
  - name: validation
    num_bytes: 552752
    num_examples: 90
  download_size: 3100749
  dataset_size: 2740710
- config_name: cross_genre_4
  features:
  - name: author
    dtype:
      class_label:
        names:
          '0': catherinebennett
          '1': georgemonbiot
          '2': hugoyoung
          '3': jonathanfreedland
          '4': martinkettle
          '5': maryriddell
          '6': nickcohen
          '7': peterpreston
          '8': pollytoynbee
          '9': royhattersley
          '10': simonhoggart
          '11': willhutton
          '12': zoewilliams
  - name: topic
    dtype:
      class_label:
        names:
          '0': Politics
          '1': Society
          '2': UK
          '3': World
          '4': Books
  - name: article
    dtype: string
  splits:
  - name: train
    num_bytes: 406144
    num_examples: 63
  - name: test
    num_bytes: 1604188
    num_examples: 264
  - name: validation
    num_bytes: 730378
    num_examples: 117
  download_size: 3100749
  dataset_size: 2740710
---

# Dataset Card for "guardian_authorship"

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

- **Homepage:** [http://www.icsd.aegean.gr/lecturers/stamatatos/papers/JLP2013.pdf](http://www.icsd.aegean.gr/lecturers/stamatatos/papers/JLP2013.pdf)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 47.31 MB
- **Size of the generated dataset:** 37.17 MB
- **Total amount of disk used:** 84.49 MB

### Dataset Summary

A dataset cross-topic authorship attribution. The dataset is provided by Stamatatos 2013.
1- The cross-topic scenarios are based on Table-4 in Stamatatos 2017 (Ex. cross_topic_1 => row 1:P S U&W ).
2- The cross-genre scenarios are based on Table-5 in the same paper. (Ex. cross_genre_1 => row 1:B P S&U&W).

3- The same-topic/genre scenario is created by grouping all the datasts as follows.
For ex., to use same_topic and split the data 60-40 use:
train_ds = load_dataset('guardian_authorship', name="cross_topic_<<#>>",
                        split='train[:60%]+validation[:60%]+test[:60%]')
tests_ds = load_dataset('guardian_authorship', name="cross_topic_<<#>>",
                        split='train[-40%:]+validation[-40%:]+test[-40%:]')

IMPORTANT: train+validation+test[:60%] will generate the wrong splits because the data is imbalanced

* See https://huggingface.co/docs/datasets/splits.html for detailed/more examples

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### cross_genre_1

- **Size of downloaded dataset files:** 2.96 MB
- **Size of the generated dataset:** 2.61 MB
- **Total amount of disk used:** 5.57 MB

An example of 'train' looks as follows.
```
{
    "article": "File 1a\n",
    "author": 0,
    "topic": 4
}
```

#### cross_genre_2

- **Size of downloaded dataset files:** 2.96 MB
- **Size of the generated dataset:** 2.61 MB
- **Total amount of disk used:** 5.57 MB

An example of 'validation' looks as follows.
```
{
    "article": "File 1a\n",
    "author": 0,
    "topic": 1
}
```

#### cross_genre_3

- **Size of downloaded dataset files:** 2.96 MB
- **Size of the generated dataset:** 2.61 MB
- **Total amount of disk used:** 5.57 MB

An example of 'validation' looks as follows.
```
{
    "article": "File 1a\n",
    "author": 0,
    "topic": 2
}
```

#### cross_genre_4

- **Size of downloaded dataset files:** 2.96 MB
- **Size of the generated dataset:** 2.61 MB
- **Total amount of disk used:** 5.57 MB

An example of 'validation' looks as follows.
```
{
    "article": "File 1a\n",
    "author": 0,
    "topic": 3
}
```

#### cross_topic_1

- **Size of downloaded dataset files:** 2.96 MB
- **Size of the generated dataset:** 2.23 MB
- **Total amount of disk used:** 5.18 MB

An example of 'validation' looks as follows.
```
{
    "article": "File 1a\n",
    "author": 0,
    "topic": 1
}
```

### Data Fields

The data fields are the same among all splits.

#### cross_genre_1
- `author`: a classification label, with possible values including `catherinebennett` (0), `georgemonbiot` (1), `hugoyoung` (2), `jonathanfreedland` (3), `martinkettle` (4).
- `topic`: a classification label, with possible values including `Politics` (0), `Society` (1), `UK` (2), `World` (3), `Books` (4).
- `article`: a `string` feature.

#### cross_genre_2
- `author`: a classification label, with possible values including `catherinebennett` (0), `georgemonbiot` (1), `hugoyoung` (2), `jonathanfreedland` (3), `martinkettle` (4).
- `topic`: a classification label, with possible values including `Politics` (0), `Society` (1), `UK` (2), `World` (3), `Books` (4).
- `article`: a `string` feature.

#### cross_genre_3
- `author`: a classification label, with possible values including `catherinebennett` (0), `georgemonbiot` (1), `hugoyoung` (2), `jonathanfreedland` (3), `martinkettle` (4).
- `topic`: a classification label, with possible values including `Politics` (0), `Society` (1), `UK` (2), `World` (3), `Books` (4).
- `article`: a `string` feature.

#### cross_genre_4
- `author`: a classification label, with possible values including `catherinebennett` (0), `georgemonbiot` (1), `hugoyoung` (2), `jonathanfreedland` (3), `martinkettle` (4).
- `topic`: a classification label, with possible values including `Politics` (0), `Society` (1), `UK` (2), `World` (3), `Books` (4).
- `article`: a `string` feature.

#### cross_topic_1
- `author`: a classification label, with possible values including `catherinebennett` (0), `georgemonbiot` (1), `hugoyoung` (2), `jonathanfreedland` (3), `martinkettle` (4).
- `topic`: a classification label, with possible values including `Politics` (0), `Society` (1), `UK` (2), `World` (3), `Books` (4).
- `article`: a `string` feature.

### Data Splits

|    name     |train|validation|test|
|-------------|----:|---------:|---:|
|cross_genre_1|   63|       112| 269|
|cross_genre_2|   63|        62| 319|
|cross_genre_3|   63|        90| 291|
|cross_genre_4|   63|       117| 264|
|cross_topic_1|  112|        62| 207|

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
@article{article,
    author = {Stamatatos, Efstathios},
    year = {2013},
    month = {01},
    pages = {421-439},
    title = {On the robustness of authorship attribution based on character n-gram features},
    volume = {21},
    journal = {Journal of Law and Policy}
}

@inproceedings{stamatatos2017authorship,
    title={Authorship attribution using text distortion},
    author={Stamatatos, Efstathios},
    booktitle={Proc. of the 15th Conf. of the European Chapter of the Association for Computational Linguistics},
    volume={1}
    pages={1138--1149},
    year={2017}
}

```


### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@eltoto1219](https://github.com/eltoto1219), [@malikaltakrori](https://github.com/malikaltakrori) for adding this dataset.