---
annotations_creators:
- expert-generated
language:
- es
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: InferES
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- nli
- spanish
- negation
- coreference
task_categories:
- text-classification
task_ids:
- natural-language-inference
---

# Dataset Card for InferES

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
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/venelink/inferes
- **Repository:** https://github.com/venelink/inferes
- **Paper:** https://arxiv.org/abs/2210.03068
- **Point of Contact:** venelin [at] utexas [dot] edu

### Dataset Summary

Natural Language Inference dataset for European Spanish

Paper accepted and (to be) presented at COLING 2022

### Supported Tasks and Leaderboards

Natural Language Inference

### Languages

Spanish

## Dataset Structure

The dataset contains two texts inputs (Premise and Hypothesis), Label for three-way classification, and annotation data.

### Data Instances

train size = 6444 

test size = 1612

### Data Fields

ID : the unique ID of the instance

Premise 

Hypothesis

Label: cnt, ent, neutral

Topic: 1 (Picasso), 2 (Columbus), 3 (Videogames), 4 (Olympic games), 5 (EU), 6 (USSR)

Anno: ID of the annotators (in cases of undergrads or crowd - the ID of the group)

Anno Type: Generate, Rewrite, Crowd, and Automated

### Data Splits

train size = 6444 

test size = 1612

The train/test split is stratified by a key that combines Label + Anno + Anno type

### Source Data

Wikipedia + text generated from "sentence generators" hired as part of the process

#### Who are the annotators?

Native speakers of European Spanish

### Personal and Sensitive Information

No personal or Sensitive information is included.

Annotators are anonymized and only kept as "ID" for research purposes.

### Dataset Curators

Venelin Kovatchev

### Licensing Information

cc-by-4.0

### Citation Information

To be added after proceedings from COLING 2022 appear

### Contributions

Thanks to [@venelink](https://github.com/venelink) for adding this dataset.
