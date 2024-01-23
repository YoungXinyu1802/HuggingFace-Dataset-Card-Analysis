---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- text-classification
task_ids:
- natural-language-inference
pretty_name: OSDG Community Dataset (OSDG-CD)
---
# Dataset Card for OSDG-CD

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

- **Homepage:** [OSDG-CD homepage](https://doi.org/10.5281/zenodo.6393942)

### Dataset Summary

The OSDG Community Dataset (OSDG-CD) is a public dataset of thousands of text excerpts, which were validated by approximately 1,000 OSDG Community Platform (OSDG-CP) citizen scientists from over 110 countries, with respect to the Sustainable Development Goals (SDGs).

> **_NOTE:_**  There are currently no examples for SDGs 16 and 17. See [this GitHub issue](https://github.com/osdg-ai/osdg-data/issues/3).

### Supported Tasks and Leaderboards

TBD

### Languages

The language of the dataset is English.

## Dataset Structure

### Data Instances

For each instance, there is a string for the text, a string for the SDG, and an integer for the label.

```
{'text': 'Each section states the economic principle, reviews international good practice and discusses the situation in Brazil.',
 'label': 5}
```

The average token count for the premises and hypotheses are given below:

| Feature    | Mean Token Count |
| ---------- | ---------------- |
| Premise    | 14.1             |
| Hypothesis | 8.3              |

### Data Fields

- `doi`: Digital Object Identifier of the original document
- `text_id`: unique text identifier
- `text`: text excerpt from the document
- `sdg`: the SDG the text is validated against
- `label`: an integer from `0` to `17` which corresponds to the `sdg` field
- `labels_negative`: the number of volunteers who rejected the suggested SDG label
- `labels_positive`: the number of volunteers who accepted the suggested SDG label
- `agreement`: agreement score based on the formula


### Data Splits

The OSDG-CD dataset has 1 splits: _train_.

| Dataset Split | Number of Instances in Split |
| ------------- |----------------------------- |
| Train         | 32,327                       |

## Dataset Creation

### Curation Rationale

The [The OSDG Community Dataset (OSDG-CD)](https://doi.org/10.5281/zenodo.6393942) was developed as a benchmark for ...
with the goal of producing a dataset large enough to train models using neural methodologies.

### Source Data

#### Initial Data Collection and Normalization

TBD

#### Who are the source language producers?

TBD

### Annotations

#### Annotation process

TBD

#### Who are the annotators?

TBD

### Personal and Sensitive Information

The dataset does not contain any personal information about the authors or the crowdworkers.

## Considerations for Using the Data

### Social Impact of Dataset

TBD

## Additional Information

TBD

### Dataset Curators

TBD

### Licensing Information

The OSDG Community Dataset (OSDG-CD) is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

### Citation Information

```
@dataset{osdg_2022_6393942,
  author       = {OSDG and
                  UNDP IICPSD SDG AI Lab and
                  PPMI},
  title        = {OSDG Community Dataset (OSDG-CD)},
  month        = apr,
  year         = 2022,
  note         = {{This CSV file uses UTF-8 character encoding. For 
                   easy access on MS Excel, open the file using Data
                   → From Text/CSV.  Please split CSV data into
                   different columns by using a TAB delimiter.}},
  publisher    = {Zenodo},
  version      = {2022.04},
  doi          = {10.5281/zenodo.6393942},
  url          = {https://doi.org/10.5281/zenodo.6393942}
}
```

### Contributions

TBD
