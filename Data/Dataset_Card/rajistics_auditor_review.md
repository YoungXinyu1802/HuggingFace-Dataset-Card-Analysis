---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- cc-by-nc-sa-3.0
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
pretty_name: Auditor_Review
---
# Dataset Card for financial_phrasebank
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
Auditor review data collected by News Department
- **Point of Contact:**
Talked to COE for Auditing

### Dataset Summary
Auditor sentiment dataset of sentences from financial news. The dataset consists of *** sentences from English language financial news categorized by sentiment. The dataset is divided by agreement rate of 5-8 annotators.
### Supported Tasks and Leaderboards
Sentiment Classification
### Languages
English
## Dataset Structure
### Data Instances
```
{ "sentence": "Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing .",
  "label": "negative"
}
```
### Data Fields
- sentence: a tokenized line from the dataset
- label: a label corresponding to the class as a string: 'positive', 'negative' or 'neutral'
### Data Splits
A test train split was created randomly with a 75/25 split

## Dataset Creation

### Curation Rationale

The key arguments for the low utilization of statistical techniques in
financial sentiment analysis have been the difficulty of implementation for
practical applications and the lack of high quality training data for building
such models. ***


### Source Data

#### Initial Data Collection and Normalization

The corpus used in this paper is made out of English news on all listed
companies in ****

#### Who are the source language producers?

The source data was written by various auditors

### Annotations

#### Annotation process

This release of the financial phrase bank covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets.

Given the large number of overlapping annotations (5 to 8 annotations per
sentence), there are several ways to define a majority vote based gold
standard. To provide an objective comparison, we have formed 4 alternative
reference datasets based on the strength of majority agreement: 


### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

All annotators were from the same institution and so interannotator agreement
should be understood with this taken into account.

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

License: Creative Commons Attribution 4.0 International License (CC-BY)

### Contributions
