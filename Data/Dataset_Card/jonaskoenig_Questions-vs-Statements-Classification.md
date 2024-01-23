[Needs More Information]

# Dataset Card for Questions-vs-Statements-Classification

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

## Dataset Description

- **Homepage:** [Kaggle](https://www.kaggle.com/datasets/shahrukhkhan/questions-vs-statementsclassificationdataset)
- **Point of Contact:** [Shahrukh Khan](https://www.kaggle.com/shahrukhkhan)

### Dataset Summary

A dataset containing statements and questions with their corresponding labels.

### Supported Tasks and Leaderboards

multi-class-classification

### Languages

en

## Dataset Structure


### Data Splits

Train Test Valid


## Dataset Creation

### Curation Rationale


The goal of this project is to classify sentences, based on type:
Statement (Declarative Sentence)
Question (Interrogative Sentence)

### Source Data
[Kaggle](https://www.kaggle.com/datasets/shahrukhkhan/questions-vs-statementsclassificationdataset)

#### Initial Data Collection and Normalization

The dataset is created by parsing out the SQuAD dataset and combining it with the SPAADIA dataset.


### Other Known Limitations

Questions in this case ar are only one sentence, statements are a single sentence or more. They are classified correctly but don't include sentences prior to questions.

## Additional Information

### Dataset Curators

[SHAHRUKH KHAN](https://www.kaggle.com/shahrukhkhan)

### Licensing Information

[CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

