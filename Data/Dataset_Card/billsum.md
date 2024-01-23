---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- cc0-1.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids: []
paperswithcode_id: billsum
pretty_name: BillSum
train-eval-index:
- config: default
  task: summarization
  task_id: summarization
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    text: text
    summary: target
  metrics:
  - type: rouge
    name: Rouge
tags:
- bills-summarization
dataset_info:
  features:
  - name: text
    dtype: string
  - name: summary
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: train
    num_bytes: 219596090
    num_examples: 18949
  - name: test
    num_bytes: 37866257
    num_examples: 3269
  - name: ca_test
    num_bytes: 14945291
    num_examples: 1237
  download_size: 67260676
  dataset_size: 272407638
---

# Dataset Card for "billsum"

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

- **Homepage:** [https://github.com/FiscalNote/BillSum](https://github.com/FiscalNote/BillSum)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 64.14 MB
- **Size of the generated dataset:** 259.80 MB
- **Total amount of disk used:** 323.94 MB

### Dataset Summary

BillSum, summarization of US Congressional and California state bills.

There are several features:
  - text: bill text.
  - summary: summary of the bills.
  - title: title of the bills.
features for us bills. ca bills does not have.
  - text_len: number of chars in text.
  - sum_len: number of chars in summary.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### default

- **Size of downloaded dataset files:** 64.14 MB
- **Size of the generated dataset:** 259.80 MB
- **Total amount of disk used:** 323.94 MB

An example of 'train' looks as follows.
```
{
    "summary": "some summary",
    "text": "some text.",
    "title": "An act to amend Section xxx."
}
```

### Data Fields

The data fields are the same among all splits.

#### default
- `text`: a `string` feature.
- `summary`: a `string` feature.
- `title`: a `string` feature.

### Data Splits

| name  |train|ca_test|test|
|-------|----:|------:|---:|
|default|18949|   1237|3269|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

The data consists of three parts: US training bills, US test bills and California test bills. The US bills were collected from the [Govinfo](https://github.com/unitedstates/congress) service provided by the United States Government Publishing Office (GPO) under CC0-1.0 license. The California, bills from the 2015-2016 session are available from the legislature’s [website](https://leginfo.legislature.ca.gov/).

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

@misc{kornilova2019billsum,
    title={BillSum: A Corpus for Automatic Summarization of US Legislation},
    author={Anastassia Kornilova and Vlad Eidelman},
    year={2019},
    eprint={1910.00523},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

```


### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@jplu](https://github.com/jplu), [@lewtun](https://github.com/lewtun) for adding this dataset.