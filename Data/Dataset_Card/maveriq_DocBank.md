---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: DocBank
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- document-ai
task_categories: []
task_ids: []
---

# Dataset Card for DocBank

## Table of Contents
- [Dataset Card for DocBank](#dataset-card-for-docbank)
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

- **Homepage:** https://doc-analysis.github.io/docbank-page/index.html
- **Repository:** https://github.com/doc-analysis/DocBank
- **Paper:** https://arxiv.org/abs/2006.01038
- **Leaderboard:**
- **Point of Contact:** 

### Dataset Summary

DocBank is a new large-scale dataset that is constructed using a weak supervision approach. It enables models to integrate both the textual and layout information for downstream tasks. The current DocBank dataset totally includes 500K document pages, where 400K for training, 50K for validation and 50K for testing.

### Supported Tasks and Leaderboards

Document AI (text and layout)

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

dataset_info:
  features:
  - name: image
    dtype: image
  - name: token
    dtype: string
  - name: bounding_box
    sequence:
      sequence: uint16
  - name: color
    sequence:
      sequence: uint8
  - name: font
    dtype: string
  - name: label
    dtype: string

### Data Splits

dataset_info:
  splits:
  - name: train
    num_bytes: 80004043
    num_examples: 400000
  - name: validation
    num_bytes: 9995812
    num_examples: 50000
  - name: test
    num_bytes: 9995812
    num_examples: 50000
  download_size: 0
  dataset_size: 99995667

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

Apache 2.0 License

### Citation Information

    title={DocBank: A Benchmark Dataset for Document Layout Analysis},
    author={Minghao Li and Yiheng Xu and Lei Cui and Shaohan Huang and Furu Wei and Zhoujun Li and Ming Zhou},
    year={2020},
    eprint={2006.01038},
    archivePrefix={arXiv},
    primaryClass={cs.CL}

### Contributions

Thanks to [@doc-analysis](https://github.com/doc-analysis) for adding this dataset.