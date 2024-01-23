---
language:
- fa
license:
- mit
multilinguality:
- monolingual
task_categories:
- fill-mask
- text-generation
task_ids:
- language-modeling
- masked-language-modeling
pretty_name: naab-raw (raw version of the naab corpus)
---

# naab-raw (raw version of the naab corpus)
_[If you want to join our community to keep up with news, models and datasets from naab, click on [this](https://docs.google.com/forms/d/e/1FAIpQLSe8kevFl_ODCx-zapAuOIAQYr8IvkVVaVHOuhRL9Ha0RVJ6kg/viewform) link.]_

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Changelog](#changelog)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Contribution Guideline](#contribution-guideline)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Sharif Speech and Language Processing Lab](https://huggingface.co/SLPL)
- **Paper:** [naab: A ready-to-use plug-and-play corpus for Farsi](https://arxiv.org/abs/2208.13486)
- **Point of Contact:** [Sadra Sabouri](mailto:sabouri.sadra@gmail.com)

### Dataset Summary

This is the raw (uncleaned) version of the [naab](https://huggingface.co/datasets/SLPL/naab) corpus. You can use also customize our [preprocess script](https://github.com/Sharif-SLPL/t5-fa/tree/main/preprocess) and make your own cleaned corpus. This repository is a hub for all Farsi corpora. Feel free to add your corpus following the [contribution guidelines](#contribution-guideline).

You can download the dataset by the command below:
```python
from datasets import load_dataset

dataset = load_dataset("SLPL/naab-raw")
```

If you wanted to download a specific part of the corpus you can set the config name to the specific corpus name:
```python
from datasets import load_dataset

dataset = load_dataset("SLPL/naab-raw", "CC-fa")
```

### Supported Tasks and Leaderboards

This corpus can be used for training all language models trained by Masked Language Modeling (MLM) or any other self-supervised objective.

- `language-modeling`
- `masked-language-modeling`

### Changelog

It's crucial to log changes on the projects which face changes periodically. Please refer to the [CHANGELOG.md](https://huggingface.co/datasets/SLPL/naab-raw/blob/main/CHANGELOG.md) for more details.

## Dataset Structure

Each row of the dataset will look like something like the below:
```json
{
  'text': "این یک تست برای نمایش یک پاراگراف در پیکره متنی ناب است.",
}
```
+ `text` : the textual paragraph.


### Data Splits

This corpus contains only a split (the `train` split).

## Dataset Creation

### Curation Rationale

Here are some details about each part of this corpus.

#### CC-fa

The Common Crawl corpus contains petabytes of data collected since 2008. It contains raw web page data, extracted metadata, and text extractions. We use the Farsi part of it here.

#### W2C

The W2C stands for Web to Corpus and it contains several corpera. We contain the Farsi part of it in this corpus.

### Contribution Guideline

In order to add your dataset, you should follow the below steps and make a pull request in order to be merged with the _naab-raw_:

1. Add your dataset to `_CORPUS_URLS` in `naab-raw.py` like:
```python
...
    "DATASET_NAME": "LINK_TO_A_PUBLIC_DOWNLOADABLE_FILE.txt"
...
```
2. Add a log of your changes to the [CHANGELOG.md](https://huggingface.co/datasets/SLPL/naab-raw/blob/main/CHANGELOG.md).
3. Add some minor descriptions to the [Curation Rationale](#curation-rationale) under a subsection with your dataset name.


### Personal and Sensitive Information

Since this corpus is briefly a compilation of some former corpora we take no responsibility for personal information included in this corpus. If you detect any of these violations please let us know, we try our best to remove them from the corpus ASAP.

We tried our best to provide anonymity while keeping the crucial information. We shuffled some parts of the corpus so the information passing through possible conversations wouldn't be harmful. 

## Additional Information

### Dataset Curators

+ Sadra Sabouri (Sharif University of Technology)
+ Elnaz Rahmati (Sharif University of Technology)

### Licensing Information

mit

### Citation Information

```
@article{sabouri2022naab,
  title={naab: A ready-to-use plug-and-play corpus for Farsi},
  author={Sabouri, Sadra and Rahmati, Elnaz and Gooran, Soroush and Sameti, Hossein},
  journal={arXiv preprint arXiv:2208.13486},
  year={2022}
}
```

DOI:[https://doi.org/10.48550/arXiv.2208.13486](https://doi.org/10.48550/arXiv.2208.13486).

### Contributions

Thanks to [@sadrasabouri](https://github.com/sadrasabouri) and [@elnazrahmati](https://github.com/elnazrahmati) for adding this dataset.

### Keywords
+ Farsi
+ Persian
+ raw text
+ پیکره فارسی
+ پیکره متنی
+ آموزش مدل زبانی
