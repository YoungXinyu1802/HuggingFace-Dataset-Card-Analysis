---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
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
task_ids:
- sentiment-classification
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
- **Paper:** [A Fine-grained Sentiment Dataset for Norwegian](https://www.aclweb.org/anthology/2020.lrec-1.618/)
- **Leaderboard:** N/A
- **Point of Contact:** -

### Dataset Summary

Aggregated NoRec_fine: A Fine-grained Sentiment Dataset for Norwegian.
This dataset was created by the Nordic Language Processing Laboratory by aggregating the fine-grained annotations in NoReC_fine and removing sentences with conflicting or no sentiment.

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
- `text`: Text of a sentence
- `label`: The sentiment label. Here
  - 0 = negative
  - 1 = positive

### Data Splits

The dataset is split into a `train`, `validation`, and `test` split with the following sizes:

|                            | Tain   | Valid | Test  |
| -----                      | ------ | ----- | ----- |
| Number of examples         | 2675   | 516   | 417   |



## Dataset Creation

This dataset is based largely on the original data described in the paper _A Fine-Grained Sentiment Dataset for Norwegian_ by L. Øvrelid, P. Mæhlum, J. Barnes, and E. Velldal, accepted at LREC 2020, [paper available](https://www.aclweb.org/anthology/2020.lrec-1.618). However, we have since added annotations for another 3476 sentences, increasing the overall size and scope of the dataset.

## Additional Information

### Licensing Information

This work is licensed under a Creative Commons Attribution 4.0 International License

### Citation Information

```latex
@misc{sheng2020investigating,
      title={Investigating Societal Biases in a Poetry Composition System},
      author={Emily Sheng and David Uthus},
      year={2020},
      eprint={2011.02686},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
