---
annotations_creators:
- no-annotation
language_creators:
- machine-generated
language: []
license: []
multilinguality: []
pretty_name: Goud-sum
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- summarization
task_ids:
- news-articles-headline-generation
---

# Dataset Card for Goud summarization dataset

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

- **Homepage:**[Needs More Information]
- **Repository:**[Needs More Information]
- **Paper:**[Goud.ma: a News Article Dataset for Summarization in Moroccan Darija](https://openreview.net/forum?id=BMVq5MELb9)
- **Leaderboard:**[Needs More Information]
- **Point of Contact:**[Needs More Information]

### Dataset Summary

Goud-sum contains 158k articles and their headlines extracted from [Goud.ma](https://www.goud.ma/) news website. The articles are written in the Arabic script. All headlines are in Moroccan Darija, while articles may be in Moroccan Darija, in Modern Standard Arabic, or a mix of both (code-switched Moroccan Darija).

### Supported Tasks and Leaderboards

Text Summarization

### Languages

* Moroccan Arabic (Darija)
* Modern Standard Arabic 

## Dataset Structure

### Data Instances

The dataset consists of article-headline pairs in string format.

### Data Fields

* article: a string containing the body of the news article
* headline: a string containing the article's headline
* categories: a list of string of article categories

### Data Splits

Goud-sum dataset has 3 splits: _train_, _validation_, and _test_. Below are the number of instances in each split.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 139,288                                     |
| Validation    | 9,497                                       |
| Test          | 9,497                                       |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

The text was written by journalists at [Goud](https://www.goud.ma/).

### Annotations
The dataset does not contain any additional annotations.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

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

[More Information Needed]

### Citation Information

```
@inproceedings{issam2022goudma,
title={Goud.ma: a News Article Dataset for Summarization in Moroccan Darija},
author={Abderrahmane Issam and Khalil Mrini},
booktitle={3rd Workshop on African Natural Language Processing},
year={2022},
url={https://openreview.net/forum?id=BMVq5MELb9}
}
```

### Contributions

Thanks to [@issam9](https://github.com/issam9) and [@KhalilMrini](https://github.com/KhalilMrini) for adding this dataset.
