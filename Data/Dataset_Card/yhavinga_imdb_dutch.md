---
pretty_name: IMDB
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- nl
- en
license:
- other
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
paperswithcode_id: imdb-movie-reviews
train-eval-index:
- config: plain_text
  task: text-classification
  task_id: binary_classification
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    text: text
    label: target
  metrics:
  - type: accuracy
  - name: Accuracy
  - type: f1
    name: F1 macro
    args:
      average: macro
  - type: f1
    name: F1 micro
    args:
      average: micro
  - type: f1
    name: F1 weighted
    args:
      average: weighted
  - type: precision
    name: Precision macro
    args:
      average: macro
  - type: precision
    name: Precision micro
    args:
      average: micro
  - type: precision
    name: Precision weighted
    args:
      average: weighted
  - type: recall
    name: Recall macro
    args:
      average: macro
  - type: recall
    name: Recall micro
    args:
      average: micro
  - type: recall
    name: Recall weighted
    args:
      average: weighted
dataset_info:
  features:
  - name: text
    dtype: string
  - name: text_en
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          0: neg
          1: pos
  config_name: plain_text
  splits:
  - name: train
    num_bytes: 69589646
    num_examples: 24992
  - name: test
    num_bytes: 67958995
    num_examples: 24992
  - name: unsupervised
    num_bytes: 139649169
    num_examples: 49984
  download_size: 108170940
  dataset_size: 277197810
---

# Dataset Card for "imdb_dutch"

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

- **Homepage:** [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

Large Movie Review Dataset translated to Dutch.

This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets.
We provide a set of 24,992 highly polar movie reviews for training, and 24,992 for testing. There is additional unlabeled data for use as well.

### Translation to Dutch

The dataset was translated with [yhavinga/ul2-large-en-nl](https://huggingface.co/yhavinga/ul2-large-en-nl).
The translation code is available in the src directory.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

This dataset contains Dutch and English data.

## Dataset Structure

### Data Instances

#### plain_text

- **Size of downloaded dataset files:** 108 MiB
- **Size of the generated dataset:** 277 MiB

An example of 'train' looks as follows.
```
{
    "label": 0,
    "text": "Holy shit. Dit was de slechtste film die ik in lange tijd heb gezien."
    "text_en": "Holy crap. This was the worst film I have seen in a long time."
}
```

### Data Fields

The data fields are the same among all splits.

#### plain_text
- `text`: a `string` feature.
- `text_en`: a `string` feature.
- `label`: a classification label, with possible values including `neg` (0), `pos` (1).

### Data Splits

|   name   |train|unsupervised|test |
|----------|----:|-----------:|----:|
|plain_text|24992|       49984|24992|

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
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}

```


### Contributions

Thanks to [@ghazi-f](https://github.com/ghazi-f), [@patrickvonplaten](https://github.com/patrickvonplaten), [@lhoestq](https://github.com/lhoestq), [@thomwolf](https://github.com/thomwolf) for adding
the English `imdb` dataset.
This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

Created by [Yeb Havinga](https://www.linkedin.com/in/yeb-havinga-86530825/)
