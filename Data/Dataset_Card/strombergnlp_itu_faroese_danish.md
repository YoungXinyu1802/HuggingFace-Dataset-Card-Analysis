---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- da
- fo
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: ITU Faroese Danish parallel text
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- translation
task_ids: []
---


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

- **Homepage:** 
- **Repository:** 
- **Paper:** [https://arxiv.org/abs/2206.08727](https://arxiv.org/abs/2206.08727)
- **Leaderboard:** 
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)

### Dataset Summary

This is a native-speaker-generated parallel corpus of Faroese and Danish

### Supported Tasks and Leaderboards

* 

### Languages

* Danish
* Faroese

## Dataset Structure

### Data Instances
3995 parallel sentences

### Data Fields

* `id`: the sentence pair ID, `string`
* `origin`: the original sentence identifier text, `string`
* `fo`: the Faroese text, `string`
* `da`: the Danish text, `string`

### Data Splits

Monolithic

## Dataset Creation

### Curation Rationale

To gather a broad range of topics about the Faroes and the rest of the world, to enable a general-purpose Faroese:Danish translation system

### Source Data

#### Initial Data Collection and Normalization

* EUROparl Danish
* Dimmaletting, Faroese newspaper
* Tatoeba Danish / Faroese

#### Who are the source language producers?



### Annotations

#### Annotation process

No annotations

#### Who are the annotators?

Two Faroese native speakers, one male one female, in their 20s, masters degrees, living in Denmark

### Personal and Sensitive Information

None due to the sources used

## Considerations for Using the Data

### Social Impact of Dataset



### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

This collection of Faroese is curated by Leon Derczynski

### Licensing Information

Creative Commons Attribution 4.0

### Citation Information

```

```