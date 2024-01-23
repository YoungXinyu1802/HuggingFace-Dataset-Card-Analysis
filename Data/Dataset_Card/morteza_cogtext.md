---
pretty_name: CogText PubMed Abstracts
license:
- cc-by-4.0
language:
- en
multilinguality:
- monolingual
task_categories:
- text-classification
task_ids:
- topic-classification
- semantic-similarity-classification
size_categories:
- 100K<n<1M
paperswithcode_id: linking-theories-and-methods-in-cognitive
inference: false
model-index:
- name: cogtext-pubmed
  results: []
source_datasets:
- original
language_creators:
- found
- expert-generated
configs:
- pubmed
- pubmed20pct
- lexicon
- pubmed_gp3ada
tags:
- Cognitive Control
- PubMed
---

# Dataset Card for CogText PubMed Abstracts

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

**CogText** dataset contains a collection of PubMed abstracts, along with their GPT-3 embeddings and topic embeddings. See [CogText on GitHub](https://github.com/morteza/cogtext) for the details and codes.

- **Homepage:** https://github.com/morteza/cogtext
- **Repository:** https://github.com/morteza/cogtext
- **Point of Contact:** [Morteza Ansarinia](mailto:ansarinia@me.com)
- **Paper:** https://arxiv.org/abs/2203.11016

### Dataset Summary

The dataset consists of 385,705 unique scientific articles that were retrieved from PubMed in December 2021. Each item includes title, abstract, some metadata,
and embeddings generated by both GPT-3 and Top2Vec. These texts were selected based on their relevance to the cognitive control constructs or related tasks.


### Supported Tasks and Leaderboards

Topic Modeling, Text Embedding

### Languages

English

## Dataset Structure

### Data Instances

522,972 scientific articles, of which 385,705 are unique.

### Data Fields

The CSV files contain the following fields:

| Field | Description |
| ----- | ----------- |
| `index` | (int) Index of the article in the current dataset |
| `pmid` | (int) PubMed ID |
| `doi` | (str) Digital Object Identifier |
| `year` | (int) Year of publication (yyyy format)|
| `journal_title` | (str) Title of the journal |
| `journal_iso_abbreviation` | (str) ISO abbreviation of the journal |
| `title` | (str) Title of the article |
| `abstract` | (str) Abstract of the article |
| `category` | (enum) Category of the article, either "CognitiveTask" or "CognitiveConstruct" |
| `label` | (enum) Label of the article, which refers to the class labels in the `ontologies/efo.owl` ontology |
| `original_index` | (int) Index of the article in the full dataset (see `pubmed/abstracts.csv.gz`) |


### Data Splits

| Dataset | Description |
| ------- | ----------- |
| `pubmed/abstracts.csv.gz` | Full dataset |
| `pubmed/abstracts20pct.csv.gz` | 20% of the dataset (stratified random sample by `label`) |
| `gpt3/abstracts_gp3ada.nc` | GPT-3 embeddings of the entire dataset in XArray/CDF4 format, indexed by `pmid` |

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

### Annotations

#### Annotation process

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

### Acknowledgments

This research was supported by the Luxembourg National Research Fund (ATTRACT/2016/ID/11242114/DIGILEARN and INTER Mobility/2017-2/ID/11765868/ULALA).


### Citation Information

To cite the paper use the following entry:

```
@misc{cogtext2022,
  author = {Morteza Ansarinia and
            Paul Schrater and
            Pedro Cardoso-Leite},
  title = {Linking Theories and Methods in Cognitive Sciences via Joint Embedding of the Scientific Literature: The Example of Cognitive Control},
  year = {2022},
  url = {https://arxiv.org/abs/2203.11016}
}
```