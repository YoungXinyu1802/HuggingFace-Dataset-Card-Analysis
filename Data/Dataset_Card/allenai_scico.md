---
annotations_creators:
- domain experts
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
task_categories:
- token-classification
task_ids:
- coreference-resolution
paperswithcode_id: scico
tags:
- cross-document-coreference-resolution
- structure-prediction
---

# Dataset Card for SciCo

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

- **Homepage:** [SciCo homepage](https://scico.apps.allenai.org/)
- **Repository:** [SciCo repository](https://github.com/ariecattan/scico)
- **Paper:** [SciCo: Hierarchical Cross-document Coreference for Scientific Concepts](https://openreview.net/forum?id=OFLbgUP04nC)
- **Point of Contact:** [Arie Cattan](arie.cattan@gmail.com)

### Dataset Summary


SciCo consists of clusters of mentions in context and a hierarchy over them.
The corpus is drawn from computer science papers, and the concept mentions are methods and tasks from across CS. 
Scientific concepts pose significant challenges: they often take diverse forms (e.g., class-conditional image
synthesis and categorical image generation) or are ambiguous (e.g., network architecture in AI vs.
systems research). 
To build SciCo, we develop a new candidate generation
approach built on three resources: a low-coverage KB ([https://paperswithcode.com/](https://paperswithcode.com/)), a noisy hypernym extractor, and curated
candidates. 



### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The text in the dataset is in English. 

## Dataset Structure

### Data Instances

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


### Data Fields

* `flatten_tokens`: a single list of all tokens in the topic
* `flatten_mentions`: array of mentions, each mention is represented by [start, end, cluster_id]
* `tokens`: array of paragraphs 
* `doc_ids`: doc_id of each paragraph in `tokens`
* `metadata`: metadata of each doc_id 
* `sentences`: sentences boundaries for each paragraph in `tokens` [start, end]
* `mentions`: array of mentions, each mention is represented by [paragraph_id, start, end, cluster_id]
* `relations`: array of binary relations between cluster_ids [parent, child]
* `id`: id of the topic 
* `hard_10` and `hard_20` (only in the test set): flag for 10% or 20% hardest topics based on Levenshtein similarity.
* `source`: source of this topic PapersWithCode (pwc), hypernym or curated. 



### Data Splits

|                    |Train |Validation|Test |
|--------------------|-----:|---------:|----:|
|Topic               |   221|       100|  200|
|Documents           |  9013|      4120| 8237|
|Mentions            | 10925|      4874|10424|
|Clusters            |  4080|      1867| 3711|
|Relations           |  2514|      1747| 2379|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations



## Additional Information

### Dataset Curators

This dataset was initially created by Arie Cattan, Sophie Johnson, Daniel Weld, Ido Dagan, Iz Beltagy, Doug Downey and Tom Hope, while Arie was intern at Allen Institute of Artificial Intelligence.

### Licensing Information

This dataset is distributed under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

### Citation Information

```
@inproceedings{
    cattan2021scico,
    title={SciCo: Hierarchical Cross-Document Coreference for Scientific Concepts},
    author={Arie Cattan and Sophie Johnson and Daniel S. Weld and Ido Dagan and Iz Beltagy and Doug Downey and Tom Hope},
    booktitle={3rd Conference on Automated Knowledge Base Construction},
    year={2021},
    url={https://openreview.net/forum?id=OFLbgUP04nC}
}
```
### Contributions

Thanks to [@ariecattan](https://github.com/ariecattan) for adding this dataset.
