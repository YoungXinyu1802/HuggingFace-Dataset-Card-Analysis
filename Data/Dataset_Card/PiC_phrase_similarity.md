---
annotations_creators:
- expert-generated
language_creators:
- found
- expert-generated
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
paperswithcode_id: phrase-in-context
pretty_name: 'PiC: Phrase Similarity (PS)'
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- semantic-similarity-classification
---

# Dataset Card for "PiC: Phrase Similarity"

## Table of Contents
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

- **Homepage:** [https://phrase-in-context.github.io/](https://phrase-in-context.github.io/)
- **Repository:** [https://github.com/phrase-in-context](https://github.com/phrase-in-context)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [Thang Pham](<thangpham@auburn.edu>)
- **Size of downloaded dataset files:** 4.60 MB
- **Size of the generated dataset:** 2.96 MB
- **Total amount of disk used:** 7.56 MB

### Dataset Summary

PS is a binary classification task with the goal of predicting whether two multi-word noun phrases are semantically similar or not given *the same context* sentence.
This dataset contains ~10K pairs of two phrases along with their contexts used for disambiguation, since two phrases are not enough for semantic comparison.
Our ~10K examples were annotated by linguistic experts on <upwork.com> and verified in two rounds by 1000 Mturkers and 5 linguistic experts.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English.

## Dataset Structure

### Data Instances

**PS**
* Size of downloaded dataset files: 4.60 MB
* Size of the generated dataset: 2.96 MB
* Total amount of disk used: 7.56 MB

```
{
  "phrase1": "annual run",
  "phrase2": "yearlong performance",
  "sentence1": "since 2004, the club has been a sponsor of the annual run for rigby to raise money for off-campus housing safety awareness.",
  "sentence2": "since 2004, the club has been a sponsor of the yearlong performance for rigby to raise money for off-campus housing safety awareness.",
  "label": 0,
  "idx": 0,
}
```

### Data Fields

The data fields are the same among all splits.

* phrase1: a string feature.
* phrase2: a string feature.
* sentence1: a string feature.
* sentence2: a string feature.
* label: a classification label, with negative (0) and positive (1).
* idx: an int32 feature.

### Data Splits

|        name        |train |validation|test |
|--------------------|----:|--------:|----:|
|PS                  |7362|     1052|2102|

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The source passages + answers are from Wikipedia and the source of queries were produced by our hired linguistic experts from [Upwork.com](https://upwork.com).

#### Who are the source language producers?

We hired 13 linguistic experts from [Upwork.com](https://upwork.com) for annotation and more than 1000 human annotators on Mechanical Turk along with another set of 5 Upwork experts for 2-round verification.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

13 linguistic experts from [Upwork.com](https://upwork.com).

### Personal and Sensitive Information

No annotator identifying details are provided.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

This dataset is a joint work between Adobe Research and Auburn University.
Creators: [Thang M. Pham](https://scholar.google.com/citations?user=eNrX3mYAAAAJ), [David Seunghyun Yoon](https://david-yoon.github.io/), [Trung Bui](https://sites.google.com/site/trungbuistanford/), and [Anh Nguyen](https://anhnguyen.me).

[@PMThangXAI](https://twitter.com/pmthangxai) added this dataset to HuggingFace.

### Licensing Information

This dataset is distributed under [Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

### Citation Information

```
@article{pham2022PiC,
  title={PiC: A Phrase-in-Context Dataset for Phrase Understanding and Semantic Search},
  author={Pham, Thang M and Yoon, Seunghyun and Bui, Trung and Nguyen, Anh},
  journal={arXiv preprint arXiv:2207.09068},
  year={2022}
}
```