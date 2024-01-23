---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
license:
- cc0-1.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: Million Headlines
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories: []
task_ids: []
---
# Dataset Card for Million Headlines

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

- **Homepage:** [Kaggle dataset](https://www.kaggle.com/datasets/therohk/million-headlines)
- **Point of Contact:** Rohit Kulkarni)

### Dataset Summary

This contains data of news headlines published over a period of eighteen years.  Sourced from the reputable Australian news source ABC (Australian Broadcasting Corporation) 


## Dataset Structure

### Data Instances

For each instance, there is a integer for the data, a string for news headline.

### Data Fields

- `publish date`: a integer that represents the data
- `headline`: a string for the news headline

### Personal and Sensitive Information

The dataset does not contain any personal information about the authors or the crowdworkers, but may contain descriptions of the people that were in the headlines.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset represents one news service in Australia and should not be considered representative of all news or headlines.

### Discussion of Biases

News headlines may contain biases and should not be considered neutral.

### Licensing Information

[CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/).