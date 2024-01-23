---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- hi
license: "cc-by-sa-4.0"
multilinguality:
- monolingual
paperswithcode_id: hiner-collapsed-1
pretty_name: HiNER - Large Hindi Named Entity Recognition dataset
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

<p align="center"><img src="https://huggingface.co/datasets/cfilt/HiNER-collapsed/raw/main/cfilt-dark-vec.png" alt="Computation for Indian Language Technology Logo" width="150" height="150"/></p>

# Dataset Card for HiNER-original

[![Twitter Follow](https://img.shields.io/twitter/follow/cfiltnlp?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/cfiltnlp)
[![Twitter Follow](https://img.shields.io/twitter/follow/PeopleCentredAI?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/PeopleCentredAI)

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://github.com/cfiltnlp/HiNER
- **Repository:** https://github.com/cfiltnlp/HiNER
- **Paper:** https://arxiv.org/abs/2204.13743
- **Leaderboard:** https://paperswithcode.com/sota/named-entity-recognition-on-hiner-collapsed
- **Point of Contact:** Rudra Murthy V

### Dataset Summary

This dataset was created for the fundamental NLP task of Named Entity Recognition for the Hindi language at CFILT Lab, IIT Bombay. We gathered the dataset from various government information webpages and manually annotated these sentences as a part of our data collection strategy. 

**Note:** The dataset contains sentences from ILCI and other sources. ILCI dataset requires license from Indian Language Consortium due to which we do not distribute the ILCI portion of the data. Please send us a mail with proof of ILCI data acquisition to obtain the full dataset.

### Supported Tasks and Leaderboards

Named Entity Recognition

### Languages

Hindi

## Dataset Structure

### Data Instances

{'id': '0', 'tokens': ['प्राचीन', 'समय', 'में', 'उड़ीसा', 'को', 'कलिंग', 'के', 'नाम', 'से', 'जाना', 'जाता', 'था', '।'], 'ner_tags': [0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0]}

### Data Fields

- `id`: The ID value of the data point.
- `tokens`: Raw tokens in the dataset.
- `ner_tags`: the NER tags for this dataset. 

### Data Splits

|                  | Train  | Valid | Test |
| -----            | ------ | ----- | ---- |
| original         | 76025 |  10861 | 21722|
| collapsed        | 76025 |  10861 | 21722|

## About

This repository contains the Hindi Named Entity Recognition dataset (HiNER) published at the Langauge Resources and Evaluation conference (LREC) in 2022. A pre-print via arXiv is available [here](https://arxiv.org/abs/2204.13743).

### Recent Updates
* Version 0.0.5: HiNER initial release

## Usage

You should have the 'datasets' packages installed to be able to use the :rocket: HuggingFace datasets repository. Please use the following command and install via pip:

```code
    pip install datasets
```

To use the original dataset with all the tags, please use:<br/>

```python
    from datasets import load_dataset
    hiner = load_dataset('cfilt/HiNER-original')
```

To use the collapsed dataset with only PER, LOC, and ORG tags, please use:<br/>

```python
    from datasets import load_dataset
    hiner = load_dataset('cfilt/HiNER-collapsed')
```
However, the CoNLL format dataset files can also be found on this Git repository under the [data](data/) folder.

## Model(s)

Our best performing models are hosted on the HuggingFace models repository:
1. [HiNER-Collapsed-XLM-R](https://huggingface.co/cfilt/HiNER-Collapse-XLM-Roberta-Large)
2. [HiNER-Original-XLM-R](https://huggingface.co/cfilt/HiNER-Original-XLM-Roberta-Large)

## Dataset Creation

### Curation Rationale

HiNER was built on data extracted from various government websites handled by the Government of India which provide information in Hindi. This dataset was built for the task of Named Entity Recognition. The dataset was introduced to introduce new resources to the Hindi language that was under-served for Natural Language Processing.

### Source Data

#### Initial Data Collection and Normalization

HiNER was built on data extracted from various government websites handled by the Government of India which provide information in Hindi

#### Who are the source language producers?

Various Government of India webpages

### Annotations

#### Annotation process

This dataset was manually annotated by a single annotator of a long span of time. 

#### Who are the annotators?

Pallab Bhattacharjee

### Personal and Sensitive Information

We ensured that there was no sensitive information present in the dataset. All the data points are curated from publicly available information.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to provide a large Hindi Named Entity Recognition dataset. Since the information (data points) has been obtained from public resources, we do not think there is a negative social impact in releasing this data. 

### Discussion of Biases

Any biases contained in the data released by the Indian government are bound to be present in our data. 

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Pallab Bhattacharjee

### Licensing Information

CC-BY-SA 4.0

### Citation Information

```latex
@misc{https://doi.org/10.48550/arxiv.2204.13743,
  doi = {10.48550/ARXIV.2204.13743},
  url = {https://arxiv.org/abs/2204.13743},
  author = {Murthy, Rudra and Bhattacharjee, Pallab and Sharnagat, Rahul and Khatri, Jyotsana and Kanojia, Diptesh and Bhattacharyya, Pushpak},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {HiNER: A Large Hindi Named Entity Recognition Dataset},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```