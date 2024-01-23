---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
- sentiment-classification
paperswithcode_id: null
pretty_name: Auditor_Sentiment
---
# Dataset Card for Auditor Sentiment

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

## Dataset Description
Auditor review sentiment collected by News Department

- **Point of Contact:**
Talked to COE for Auditing, currently sue@demo.org
### Dataset Summary

Auditor sentiment dataset of sentences from financial news. The dataset consists of several thousand sentences from English language financial news categorized by sentiment. 

### Supported Tasks and Leaderboards

Sentiment Classification

### Languages

English

## Dataset Structure

### Data Instances

```
"sentence": "Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing .",
"label": "negative"
```

### Data Fields

- sentence: a tokenized line from the dataset
- label: a label corresponding to the class as a string: 'positive' - (2), 'neutral' - (1), or 'negative' - (0)  

### Data Splits

A train/test split was created randomly with a 75/25 split

## Dataset Creation

### Curation Rationale

To gather our auditor evaluations into one dataset. Previous attempts using off-the-shelf sentiment had only 70% F1, this dataset was an attempt to improve upon that performance.

### Source Data

#### Initial Data Collection and Normalization

The corpus used in this paper is made out of English news reports.

#### Who are the source language producers?

The source data was written by various auditors.

### Annotations

#### Annotation process

This release of the auditor reviews covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets.  The subset here is where inter-annotation agreement was greater than 75%.

#### Who are the annotators?

They were pulled from the SME list, names are held by sue@demo.org

### Personal and Sensitive Information

There is no personal or sensitive information in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

All annotators were from the same institution and so interannotator agreement
should be understood with this taken into account.

### Licensing Information

License: Demo.Org Proprietary - DO NOT SHARE

This dataset is based on the [financial phrasebank](https://huggingface.co/datasets/financial_phrasebank) dataset.