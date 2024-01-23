annotations_creators:
- expert-generated
language_creators:
- expert-generated
languages: []
licenses:
- cc0-1.0
multilinguality: []
pretty_name: Monkey-Species-Collection
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-image-classification

# Dataset Card for Monkey-Species-Collection

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

- **Homepage:** https://www.kaggle.com/datasets/slothkong/10-monkey-species
- **Repository:** https://github.com/slothkong/CNN_classification_10_monkey_species
- **Paper:** @misc{kaggle-10-monkey-species,
  title={Kaggle: 10 Monkey Species},
  howpublished={\\url{https://www.kaggle.com/datasets/slothkong/10-monkey-species}},
  note = {Accessed: 2022-05-30},
}
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset is intended as a test case for fine-grain classification tasks (10 different kinds of monkey species). The dataset consists of almost 1400 JPEG images grouped into two splits - training and validation. Each split contains 10 categories labeled as n0~n9, each corresponding a species from [Wikipedia's monkey cladogram](https://en.wikipedia.org/wiki/Monkey). Images were downloaded with help of the [googliser](https://github.com/teracow/googliser) open source code.


| Label | Latin Name            | Common Name               | Train Images | Validation Images |
| ----- | --------------------- | ------------------------- | ------------ | ----------------- |
| n0    | alouatta_palliata     | mantled_howler            | 131          | 26                |
| n1    | erythrocebus_patas    | patas_monkey              | 139          | 28                |
| n2    | cacajao_calvus        | bald_uakari               | 137          | 27                |
| n3    | macaca_fuscata        | japanese_macaque          | 152          | 30                |
| n4    | cebuella_pygmea       | pygmy_marmoset            | 131          | 26                |
| n5    | cebus_capucinus       | white_headed_capuchin     | 141          | 28                |
| n6    | mico_argentatus       | silvery_marmoset          | 132          | 26                |
| n7    | saimiri_sciureus      | common_squirrel_monkey    | 142          | 28                |
| n8    | aotus_nigriceps       | black_headed_night_monkey | 133          | 27                |
| n9    | trachypithecus_johnii | nilgiri_langur            | 132          | 26                |


This collection includes the following GTZAN variants:
* original (images are 400x300 px or larger; ~550 MB)
* downsized (images are downsized to 224x224 px; ~40 MB)

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

[Needs More Information]

## Dataset Structure

### Data Instances

[Needs More Information]

### Data Fields

[Needs More Information]

### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]