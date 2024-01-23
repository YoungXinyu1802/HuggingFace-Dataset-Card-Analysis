---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- no
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
---

# Dataset Card Creation Guide

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

- **Homepage:** N/A
- **Repository:** [GitHub](https://github.com/ltgoslo/NorBERT/)
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** -

### Dataset Summary

The Norwegian Parliament Speeches is a collection of text passages from 1998 to 2016 and pronounced at the Norwegian Parliament (Storting) by members of the two major parties: Fremskrittspartiet and Sosialistisk Venstreparti. The dataset is annotated with the party the speaker was associated with at the time (dates of speeches are also included).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The text in the dataset is in Norwegian.

## Dataset Structure

### Data Instances

Example of one instance in the dataset.

```{'label': 0, 'text': 'Verre er det med slagsmålene .'}```

### Data Fields

- `id`: index of the example
- `text`: Text of a speech
- `date`: Date (`YYYY-MM-DD`) the speech was produced
- `label`: Political party the speaker was associated with at the time
  - 0 = Fremskrittspartiet
  - 1 = Sosialistisk Venstreparti

### Data Splits

The dataset is split into a `train`, `validation`, and `test` split with the following sizes:

|                            | Tain   | Valid | Test  |
| -----                      | ------ | ----- | ----- |
| Number of examples         | 3600   | 1200  | 1200  |

The dataset is balanced on political party.

## Dataset Creation

This dataset is based on the publicly available information by Norwegian Parliament (Storting) and created by the National Library of Norway AI-Lab to benchmark their language models.

## Additional Information

### Licensing Information

This work is licensed under a Creative Commons Attribution 4.0 International License

### Citation Information

```latex
@misc{--,
      title={--},
      author={--},
      year={2021},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
