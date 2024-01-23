---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
  trex:
  - 1M<n<10M
task_categories:
- text-retrieval
- text-classification
task_ids:
- fact-checking-retrieval
- text-scoring
paperswithcode_id: lama
pretty_name: 'LAMA: LAnguage Model Analysis - BigScience version'
tags:
- probing
---

# Dataset Card for LAMA: LAnguage Model Analysis - a dataset for probing and analyzing the factual and commonsense knowledge contained in pretrained language models.

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

## Dataset Description

- **Homepage:**
https://github.com/facebookresearch/LAMA
- **Repository:**
https://github.com/facebookresearch/LAMA
- **Paper:**
@inproceedings{petroni2019language,
  title={Language Models as Knowledge Bases?},
  author={F. Petroni, T. Rockt{\"{a}}schel, A. H. Miller, P. Lewis, A. Bakhtin, Y. Wu and S. Riedel},
  booktitle={In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2019},
  year={2019}
}

@inproceedings{petroni2020how,
  title={How Context Affects Language Models' Factual Predictions},
  author={Fabio Petroni and Patrick Lewis and Aleksandra Piktus and Tim Rockt{\"a}schel and Yuxiang Wu and Alexander H. Miller and Sebastian Riedel},
  booktitle={Automated Knowledge Base Construction},
  year={2020},
  url={https://openreview.net/forum?id=025X0zPfn}
}

### Dataset Summary

This dataset provides the data for LAMA. This dataset only contains TRex
(subset of wikidata triples).

The dataset includes some cleanup, and addition of a masked sentence
and associated answers for the [MASK] token. The accuracy in
predicting the [MASK] token shows how well the language model knows
facts and common sense information. The [MASK] tokens are only for the
"object" slots.

This version also contains questions instead of templates that can be used to probe also non-masking models.


See the paper for more details.  For more information, also see:
https://github.com/facebookresearch/LAMA

### Languages
en

## Dataset Structure

### Data Instances


The trex config has the following fields:


``
{'uuid': 'a37257ae-4cbb-4309-a78a-623036c96797', 'sub_label': 'Pianos Become the Teeth', 'predicate_id': 'P740', 'obj_label': 'Baltimore', 'template': '[X] was founded in [Y] .', 'type': 'N-1', 'question': 'Where was [X] founded?'}
34039
``




### Data Splits

There are no data splits.

## Dataset Creation

### Curation Rationale

This dataset was gathered and created to probe what language models understand.

### Source Data

#### Initial Data Collection and Normalization

See the reaserch paper and website for more detail. The dataset was
created gathered from various other datasets with cleanups for probing.


#### Who are the source language producers?

The LAMA authors and the original authors of the various configs.

### Annotations

#### Annotation process

Human annotations under the original datasets (conceptnet), and various machine annotations.

#### Who are the annotators?

Human annotations and machine annotations.

### Personal and Sensitive Information

Unkown, but likely names of famous people.

## Considerations for Using the Data

### Social Impact of Dataset

The goal for the work is to probe the understanding of language models.

### Discussion of Biases

Since the data is from human annotators, there is likely to be baises. 

[More Information Needed]

### Other Known Limitations

The original documentation for the datafields are limited.

## Additional Information

### Dataset Curators

The authors of LAMA at Facebook and the authors of the original datasets.

### Licensing Information

The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE

### Citation Information

@inproceedings{petroni2019language,
  title={Language Models as Knowledge Bases?},
  author={F. Petroni, T. Rockt{\"{a}}schel, A. H. Miller, P. Lewis, A. Bakhtin, Y. Wu and S. Riedel},
  booktitle={In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2019},
  year={2019}
}

@inproceedings{petroni2020how,
  title={How Context Affects Language Models' Factual Predictions},
  author={Fabio Petroni and Patrick Lewis and Aleksandra Piktus and Tim Rockt{\"a}schel and Yuxiang Wu and Alexander H. Miller and Sebastian Riedel},
  booktitle={Automated Knowledge Base Construction},
  year={2020},
  url={https://openreview.net/forum?id=025X0zPfn}
}

