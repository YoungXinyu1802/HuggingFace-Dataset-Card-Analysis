---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- part-of-speech
paperswithcode_id: twitter-pos-vcb
pretty_name: Twitter PoS VCB
---

# Dataset Card for "twitter-pos-vcb"

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
- **Paper:** [https://aclanthology.org/R13-1026.pdf](https://aclanthology.org/R13-1026.pdf)
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)
- **Size of downloaded dataset files:** 4.51 MiB
- **Size of the generated dataset:** 26.88 MB
- **Total amount of disk used:** 31.39 MB

### Dataset Summary

Part-of-speech information is basic NLP task. However, Twitter text
is difficult to part-of-speech tag: it is noisy, with linguistic errors and idiosyncratic style.
This data is the vote-constrained bootstrapped data generate to support state-of-the-art results.

The data is about 1.5 million English tweets annotated for part-of-speech using Ritter's extension of the PTB tagset.
The tweets are from 2012 and 2013, tokenized using the GATE tokenizer and tagged
jointly using the CMU ARK tagger and Ritter's T-POS tagger. Only when both these taggers' outputs
are completely compatible over a whole tweet, is that tweet added to the dataset.

This data is recommend for use a training data **only**, and not evaluation data.

For more details see https://gate.ac.uk/wiki/twitter-postagger.html and https://aclanthology.org/R13-1026.pdf

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

English, non-region-specific. `bcp47:en`

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.

```

```


### Data Fields

The data fields are the same among all splits.

#### twitter_pos_vcb
- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `pos_tags`: a `list` of classification labels (`int`). Full tagset with indices:

```python

```


### Data Splits

|  name   |tokens|sentences|
|---------|----:|---------:|
|twitter-pos-vcb|1 543 126| 159 492|

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

Creative Commons Attribution 4.0 (CC-BY)

### Citation Information

```
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