---
annotations_creators:
- Leonardo Zilio, Hadeel Saadany, Prashant Sharma, Diptesh Kanojia, Constantin Orasan
language_creators:
- found
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids: []
paperswithcode_id: plod-an-abbreviation-detection-dataset-for
pretty_name: 'PLOD: An Abbreviation Detection Dataset'
tags:
- abbreviation-detection
---

# PLOD: An Abbreviation Detection Dataset  

This is the repository for PLOD Dataset published at LREC 2022. The dataset can help build sequence labelling models for the task Abbreviation Detection.

### Dataset

We provide two variants of our dataset - Filtered and Unfiltered. They are described in our paper here.

1. The Filtered version can be accessed via [Huggingface Datasets here](https://huggingface.co/datasets/surrey-nlp/PLOD-filtered) and a [CONLL format is present here](https://github.com/surrey-nlp/PLOD-AbbreviationDetection).<br/>

2. The Unfiltered version can be accessed via [Huggingface Datasets here](https://huggingface.co/datasets/surrey-nlp/PLOD-unfiltered) and a [CONLL format is present here](https://github.com/surrey-nlp/PLOD-AbbreviationDetection).<br/>

3. The [SDU Shared Task](https://sites.google.com/view/sdu-aaai22/home) data we use for zero-shot testing is [available here](https://huggingface.co/datasets/surrey-nlp/SDU-test).

# Dataset Card for PLOD-unfiltered

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

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/surrey-nlp/PLOD-AbbreviationDetection
- **Paper:** https://arxiv.org/abs/2204.12061
- **Leaderboard:** https://paperswithcode.com/sota/abbreviationdetection-on-plod-an-abbreviation
- **Point of Contact:** [Diptesh Kanojia](mailto:d.kanojia@surrey.ac.uk)

### Dataset Summary

This PLOD Dataset is an English-language dataset of abbreviations and their long-forms tagged in text. The dataset has been collected for research from the PLOS journals indexing of abbreviations and long-forms in the text. This dataset was created to support the Natural Language Processing task of abbreviation detection and covers the scientific domain. 

### Supported Tasks and Leaderboards

This dataset primarily supports the Abbreviation Detection Task. It has also been tested on a train+dev split provided by the Acronym Detection Shared Task organized as a part of the Scientific Document Understanding (SDU) workshop at AAAI 2022.


### Languages

English

## Dataset Structure

### Data Instances

A typical data point comprises an ID, a set of `tokens` present in the text, a set of `pos_tags` for the corresponding tokens obtained via Spacy NER, and a set of `ner_tags` which are limited to `AC` for `Acronym` and `LF` for `long-forms`.

An example from the dataset:
{'id': '1',
 'tokens': ['Study', '-', 'specific', 'risk', 'ratios', '(', 'RRs', ')', 'and', 'mean', 'BW', 'differences', 'were', 'calculated', 'using', 'linear', 'and', 'log', '-', 'binomial', 'regression', 'models', 'controlling', 'for', 'confounding', 'using', 'inverse', 'probability', 'of', 'treatment', 'weights', '(', 'IPTW', ')', 'truncated', 'at', 'the', '1st', 'and', '99th', 'percentiles', '.'],
 'pos_tags': [8, 13, 0, 8, 8, 13, 12, 13, 5, 0, 12, 8, 3, 16, 16, 0, 5, 0, 13, 0, 8, 8, 16, 1, 8, 16, 0, 8, 1, 8, 8, 13, 12, 13, 16, 1, 6, 0, 5, 0, 8, 13],
 'ner_tags': [0, 0, 0, 3, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

### Data Fields

- id: the row identifier for the dataset point.
- tokens: The tokens contained in the text.
- pos_tags: the Part-of-Speech tags obtained for the corresponding token above from Spacy NER.
- ner_tags: The tags for abbreviations and long-forms.


### Data Splits

|            | Train   | Valid | Test |
| -----      | ------ | -----  | ---- |
| Filtered   | 112652 |  24140 | 24140|
| Unfiltered | 113860 |  24399 | 24399|


## Dataset Creation

### Source Data

#### Initial Data Collection and Normalization

Extracting the data from PLOS Journals online and then tokenization, normalization.

#### Who are the source language producers?

PLOS Journal

## Additional Information

### Dataset Curators

The dataset was initially created by Leonardo Zilio, Hadeel Saadany, Prashant Sharma,
Diptesh Kanojia, Constantin Orasan.

### Licensing Information

CC-BY-SA 4.0

### Citation Information

[Needs More Information]

### Installation

We use the custom NER pipeline in the [spaCy transformers](https://spacy.io/universe/project/spacy-transformers) library to train our models. This library supports training via any pre-trained language models available at the :rocket: [HuggingFace repository](https://huggingface.co/).<br/>
Please see the instructions at these websites to setup your own custom training with our dataset to reproduce the experiments using Spacy.

OR<br/>

However, you can also reproduce the experiments via the Python notebook we [provide here](https://github.com/surrey-nlp/PLOD-AbbreviationDetection/blob/main/nbs/fine_tuning_abbr_det.ipynb) which uses HuggingFace Trainer class to perform the same experiments. The exact hyperparameters can be obtained from the models readme cards linked below. Before starting, please perform the following steps:

```bash
git clone https://github.com/surrey-nlp/PLOD-AbbreviationDetection
cd PLOD-AbbreviationDetection
pip install -r requirements.txt
```

Now, you can use the notebook to reproduce the experiments.

### Model(s)

Our best performing models are hosted on the HuggingFace models repository:

| Models | [`PLOD - Unfiltered`](https://huggingface.co/datasets/surrey-nlp/PLOD-unfiltered) | [`PLOD - Filtered`](https://huggingface.co/datasets/surrey-nlp/PLOD-filtered) | Description |
| --- | :---: | :---: | --- |
| [RoBERTa<sub>large</sub>](https://huggingface.co/roberta-large) | [RoBERTa<sub>large</sub>-finetuned-abbr](https://huggingface.co/surrey-nlp/roberta-large-finetuned-abbr) | -soon- | Fine-tuning on the RoBERTa<sub>large</sub> language model |
| [RoBERTa<sub>base</sub>](https://huggingface.co/roberta-base) | -soon- | [RoBERTa<sub>base</sub>-finetuned-abbr](https://huggingface.co/surrey-nlp/roberta-large-finetuned-abbr) | Fine-tuning on the RoBERTa<sub>base</sub> language model |
| [AlBERT<sub>large-v2</sub>](https://huggingface.co/albert-large-v2) | [AlBERT<sub>large-v2</sub>-finetuned-abbDet](https://huggingface.co/surrey-nlp/albert-large-v2-finetuned-abbDet) | -soon- | Fine-tuning on the AlBERT<sub>large-v2</sub> language model |


On the link provided above, the model(s) can be used with the help of the Inference API via the web-browser itself. We have placed some examples with the API for testing.<br/>

### Usage

You can use the HuggingFace Model link above to find the instructions for using this model in Python locally using the notebook provided in the Git repo.

