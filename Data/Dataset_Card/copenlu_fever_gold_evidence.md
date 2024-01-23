---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- machine-generated
- crowdsourced
language:
- en
license:
- cc-by-sa-3.0
- gpl-3.0
multilinguality:
- monolingual
paperswithcode_id: fever
pretty_name: ''
size_categories:
- 100K<n<1M
source_datasets:
- extended|fever
task_categories:
- text-classification
task_ids:
- fact-checking
---
# Dataset Card for fever_gold_evidence

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

- **Homepage:** https://github.com/copenlu/fever-adversarial-attacks
- **Repository:** https://github.com/copenlu/fever-adversarial-attacks
- **Paper:** https://aclanthology.org/2020.emnlp-main.256/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Dataset for training classification-only fact checking with claims from the FEVER dataset.
This dataset is used in the paper "Generating Label Cohesive and Well-Formed Adversarial Claims", EMNLP 2020

The evidence is the gold evidence from the FEVER dataset for *REFUTE* and *SUPPORT* claims.
For *NEI* claims, we extract evidence sentences with the system in "Christopher Malon. 2018. Team Papelo: Transformer Networks at FEVER. In Proceedings of the
First Workshop on Fact Extraction and VERification (FEVER), pages 109113."
More details can be found in https://github.com/copenlu/fever-adversarial-attacks


### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

[Needs More Information]

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information
```
@inproceedings{atanasova-etal-2020-generating,
    title = "Generating Label Cohesive and Well-Formed Adversarial Claims",
    author = "Atanasova, Pepa  and
      Wright, Dustin  and
      Augenstein, Isabelle",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.256",
    doi = "10.18653/v1/2020.emnlp-main.256",
    pages = "3168--3177",
    abstract = "Adversarial attacks reveal important vulnerabilities and flaws of trained models. One potent type of attack are universal adversarial triggers, which are individual n-grams that, when appended to instances of a class under attack, can trick a model into predicting a target class. However, for inference tasks such as fact checking, these triggers often inadvertently invert the meaning of instances they are inserted in. In addition, such attacks produce semantically nonsensical inputs, as they simply concatenate triggers to existing samples. Here, we investigate how to generate adversarial attacks against fact checking systems that preserve the ground truth meaning and are semantically valid. We extend the HotFlip attack algorithm used for universal trigger generation by jointly minimizing the target class loss of a fact checking model and the entailment class loss of an auxiliary natural language inference model. We then train a conditional language model to generate semantically valid statements, which include the found universal triggers. We find that the generated attacks maintain the directionality and semantic validity of the claim better than previous work.",
}
```