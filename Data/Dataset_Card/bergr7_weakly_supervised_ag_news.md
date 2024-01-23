---
annotations_creators: []
language:
- en
language_creators:
- other
license: []
multilinguality:
- monolingual
pretty_name: Weakly supervised AG News Dataset
size_categories:
- 1K<n<10K
source_datasets:
- extended|ag_news
tags: []
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

# Dataset Card for Weakly supervised AG News Dataset
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

### Dataset Summary

AG is a collection of more than 1 million news articles. News articles have been gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. ComeToMyHead is an academic news search engine which has been running since July, 2004. The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc), information retrieval (ranking, search, etc), xml, data compression, data streaming, and any other non-commercial activity. For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The Weakly supervised AG News Dataset was created by Team 44 of FSDL 2022 course with the only purpose of experimenting with weak supervision techniques. It was assumed that only the labels of the original test set and 20% of the training set were available. The labels in the training set were obtained by creating weak labels with LFs and denoising them with Snorkel's label model.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

text: a string feature
label: a classification label, with possible values including World (0), Sports (1), Business (2), Sci/Tech (3).

### Data Splits

- Training set with probabilistic labels from weak supervision: 37340
- Unlabeled data: 58660
- Validation set: 24000
- Test set: 7600

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

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to  Xiang Zhang (xiang.zhang@nyu.edu) for adding this dataset to the HF Dataset Hub.