---
language_creators:
- found
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: eoir_privacy
source_datasets: []
task_categories:
- text-classification
viewer: false
---
# Dataset Card for eoir_privacy

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
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset mimics privacy standards for EOIR decisions. It is meant to help learn contextual data sanitization rules to anonymize potentially sensitive contexts in crawled language data.

### Languages

English

## Dataset Structure

### Data Instances

{
  "text" : masked paragraph, 
  "label" : whether to use a pseudonym in filling masks
}

### Data Splits

train 75%, validation 25%

## Dataset Creation

### Curation Rationale

This dataset mimics privacy standards for EOIR decisions. It is meant to help learn contextual data sanitization rules to anonymize potentially sensitive contexts in crawled language data.

### Source Data

#### Initial Data Collection and Normalization

We scrape EOIR. We then filter at the paragraph level and replace any references to respondent, applicant, or names with [MASK] tokens. We then determine if the case used a pseudonym or not.

#### Who are the source language producers?

U.S. Executive Office for Immigration Review

### Annotations

#### Annotation process

Annotations (i.e., pseudonymity decisions) were made by the EOIR court. We use regex to identify if a pseudonym was used to refer to the applicant/respondent. 

#### Who are the annotators?

EOIR judges.

### Personal and Sensitive Information

There may be sensitive contexts involved, the courts already make a determination as to data filtering of sensitive data, but nonetheless there may be sensitive topics discussed. 

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is meant to learn contextual privacy rules to help filter private/sensitive data, but itself encodes biases of the courts from which the data came. We suggest that people look beyond this data for learning more contextual privacy rules.

### Discussion of Biases

Data may be biased due to its origin in U.S. immigration courts. 

### Licensing Information

CC-BY-NC

### Citation Information
```
@misc{hendersonkrass2022pileoflaw,
  url = {https://arxiv.org/abs/2207.00220},
  author = {Henderson, Peter and Krass, Mark S. and Zheng, Lucia and Guha, Neel and Manning, Christopher D. and Jurafsky, Dan and Ho, Daniel E.},
  title = {Pile of Law: Learning Responsible Data Filtering from the Law and a 256GB Open-Source Legal Dataset},
  publisher = {arXiv},
  year = {2022}
}

```