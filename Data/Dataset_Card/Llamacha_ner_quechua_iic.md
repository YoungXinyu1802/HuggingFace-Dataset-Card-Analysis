
---
annotations_creators:
- crowdsourced

language:
- qu

license:
- apache-2.0

size_categories:
- n<1K
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition

---
# Dataset Card for WikiANN
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
- **Paper:** The original datasets come from Introducing QuBERT: A Large Monolingual Corpus and BERT Model for
Southern Quechua [paper](https://aclanthology.org/2022.deeplo-1.1.pdf) by Rodolfo Zevallos et al. (2022).
- **Point of Contact:** [Rodolfo Zevallos](mailto:rodolfojoel.zevallos@upf.edu)
### Dataset Summary
NER_Quechua_IIC is a named entity recognition dataset consisting of dictionary texts provided by the Peruvian Ministry of Education, annotated with LOC (location), PER (person) and ORG (organization) tags in the IOB2 format.
### Supported Tasks and Leaderboards
- `named-entity-recognition`: The dataset can be used to train a model for named entity recognition in Quechua languages.
