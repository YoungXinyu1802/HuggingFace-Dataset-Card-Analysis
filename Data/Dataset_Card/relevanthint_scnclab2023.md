---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- machine-generated
license: []
multilinguality:
- monolingual
paperswithcode_id: scnclab2023
pretty_name: Synthetical Clinical Notes - Clab 2023
dataset_info:
  features:
    - name: tokens
      sequence: string
    - name: ner_tags
      sequence:
        class_label:
          names:
            '0' : O
            '1' : B-allergies
            '2' : I-allergies
            '3' : B-biomarkers
            '4' : I-biomarkers
            '5' : B-cancer_symptoms
            '6' : I-cancer_symptoms
            '7' : B-cancer_type
            '8' : I-cancer_type
            '9' : B-date
            '10' : I-date
            '11' : B-diagnosis
            '12' : I-diagnosis
            '13' : B-gender
            '14' : I-gender
            '15' : B-imaging_options
            '16' : I-imaging_options
            '17' : B-test_result
            '18' : I-test_result
            '19' : B-treatment
            '20' : I-treatment
size_categories:
- n<1K
source_datasets:
- original
tags:
- bio
- clinic
- cancer
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for [scnclab2023]

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
- **Point of Contact:** relevanthint@gmail.com

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

The Dataset has been created using the GPT-3 API by providing a prompt with some manually created clinical notes.


#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

The annotation has been done using [Argilla](https://github.com/argilla-io)

#### Who are the annotators?

The sinthetical clinical notes have been annotated by a group of three biomedical experts

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

Note that this is not a real dataset.

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

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.