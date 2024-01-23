---
YAML tags:
annotations_creators: []
language_creators: []
language: []
license: []
multilinguality: []
pretty_name: ''
size_categories:
- unknown
source_datasets: []
task_categories: []
task_ids: []
---

# Dataset Card for UR50_2021_04 

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
  https://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/
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

- **Homepage:** https://www.uniprot.org/
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

The Uniref50 (UR50) dataset version 2021/04 is a biological dataset taken from the Uniprot database: https://www.uniprot.org/

### Supported Tasks and Leaderboards

The UR50 dataset contains 48 Million protein sequences. It is a useful dataset to train protein language models.

### Languages

Proteins

## Dataset Structure

### Data Instances


### Data Fields


### Data Splits

 Train, validation

## Dataset Creation

### Curation Rationale

Substituted FASTA headers by <endoftext> tag.
  The dataset was tokenized using BPE and further split into train and validation datasets (ratio 90/10) choosing random sequences for the latter.

### Source Data

#### Initial Data Collection and Normalization


#### Who are the source language producers?

UniProt

### Annotations

#### Annotation process

UniProt contains annotations but no labels/annotations were used for this dataset.

#### Who are the annotators?


### Personal and Sensitive Information



## Considerations for Using the Data

### Social Impact of Dataset



### Discussion of Biases



### Other Known Limitations



## Additional Information

### Dataset Curators



### Licensing Information


### Citation Information



### Contributions

Thanks to UniProt for curating this dataset. https://www.uniprot.org/
