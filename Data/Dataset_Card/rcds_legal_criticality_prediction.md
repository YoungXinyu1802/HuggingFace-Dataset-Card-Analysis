---
annotations_creators:
- machine-generated
language:
- de
- fr
- it
language_creators:
- expert-generated
license: []
multilinguality:
- multilingual
pretty_name: Legal Criticality Prediction
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- text-classification
---
# Dataset Card for [legal criticality prediction]

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

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Legal Criticality Prediction (LCP) is a multilingual, diachronic dataset of 130K Swiss Federal Supreme Court (FSCS) cases annotated with two criticality labels. The bge_label i a binary label (critical, non-critical), while the citation label has 5 classes (critical-1, critical-2, critical-3, critical-4, non-critical). Critical classes of the citation_label are distinct subsets of the critical class of the bge_label. This dataset creates a challenging text classification task. We also provide additional metadata as the publication year, the law area and the canton of origin per case, to promote robustness and fairness studies on the critical area of legal NLP.

### Supported Tasks and Leaderboards

LCP can be used as text classification task

### Languages

Switzerland has four official languages with three languages German, French and Italian being represenated. The decisions are written by the judges and clerks in the language of the proceedings.
German (80k), French (40k), Italian (10k)

## Dataset Structure

```
{
  "decision_id": ,
  "language": de,
  "year": 2018,
  "chamber": ,
  "court": ,
  "canton": ,
  "region": ,
  "origin_chamber": ,
  "origin_court": ,
  "origin_canton": ,
  "law_area": ,
  "law_sub_area": ,
  "bge_label": ,
  "citation_label": ,
  "facts": ,
  "considerations": ,
  "rulings": ,
  "origin_facts": ,
  "origin_considerations": ,
}
```

### Data Fields

```
decision_id: (str) a unique identifier of the for the document
language: (str) one of (de, fr, it)
year: (int) the publication year
chamber: (str) the chamber of the case
court: (str) the court of the case
canton: (str) the canton
region: (str) the region of the case
origin_chamber: (str) the chamber of the origin case
origin_court: (str) the court of the origin case
origin_canton:  (str) the canton of the origin case
law_area: (str) the law area of the case
law_sub_area:(str) the law sub area of the case
bge_label: (str) critical or non-critical
citation_label: (str) critical-1, critical-2, critical-3, critical-4, non-critical
facts: (str) the facts of the case
considerations: (str) the considerations of the case
rulings: (str) the rulings of the case
origin_facts: (str) the facts of the origin case
origin_considerations: (str) the considerations of the origin case
```

### Data Instances
[More Information Needed]
### Data Fields
[More Information Needed]
### Data Splits

The dataset was split date-stratisfied
- Train: 2002-2015
- Validation: 2016-2017
- Test: 2018-2022

| Language   | Subset     | Number of Documents (Training/Validation/Test) | 
|------------|------------|--------------------------------------------|  
| German     | **de**     |  /  /                          |
| French     | **fr**     |  /  /                       |
| Italian    | **it**     |  /  /                           |

## Dataset Creation
### Curation Rationale

The dataset was curated by Stern et al. (2023).

### Source Data
#### Initial Data Collection and Normalization

The original data are published from the Swiss Federal Supreme Court (https://www.bger.ch) in unprocessed formats (HTML). The documents were downloaded from the Entscheidsuche portal (https://entscheidsuche.ch) in HTML. 

#### Who are the source language producers?

The decisions are written by the judges and clerks in the language of the proceedings.

### Annotations
#### Annotation process

bge_label:
1. all bger_references in the bge header were extracted
2. bger file_names are compared with the found references

citation_label:
1. count all citations for all bger cases and weight citations
2. divide cited cases in four different classes, depending on amount of citations

#### Who are the annotators?

Ronja Stern annotated the citations.
Metadata is published by the Swiss Federal Supreme Court (https://www.bger.ch).

### Personal and Sensitive Information

The dataset contains publicly available court decisions from the Swiss Federal Supreme Court. Personal or sensitive information has been anonymized by the court before publication according to the following guidelines: https://www.bger.ch/home/juridiction/anonymisierungsregeln.html.

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

We release the data under CC-BY-4.0 which complies with the court licensing (https://www.bger.ch/files/live/sites/bger/files/pdf/de/urteilsveroeffentlichung_d.pdf)
© Swiss Federal Supreme Court, 2002-2022

The copyright for the editorial content of this website and the consolidated texts, which is owned by the Swiss Federal Supreme Court, is licensed under the Creative Commons Attribution 4.0 International licence. This means that you can re-use the content provided you acknowledge the source and indicate any changes you have made.
Source: https://www.bger.ch/files/live/sites/bger/files/pdf/de/urteilsveroeffentlichung_d.pdf

### Citation Information

*Visu, Ronja, Joel*
*Title: Blabliblablu*
*Name of conference*
```
cit
```

### Contributions

Thanks to [@Stern5497](https://github.com/stern5497) for adding this dataset.