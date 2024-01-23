---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license:
- cc-by-2.0
multilinguality:
- monolingual
pretty_name: Quasimodo
size_categories:
- 100M<n<1B
source_datasets:
- original
tags:
- knowledge base
- commonsense
task_categories:
- question-answering
task_ids:
- closed-domain-qa
---


# Dataset Card for Quasimodo

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)


## Dataset Description

- **Homepage:** https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/commonsense/quasimodo
- **Repository:** https://github.com/Aunsiels/CSK
- **Paper:** Romero et al., Commonsense Properties from Query Logs and Question Answering Forums, CIKM, 2019

### Dataset Summary

A commonsense knowledge base constructed automatically from question-answering forums and query logs.

### Supported Tasks and Leaderboards

Can be useful for tasks requiring external knowledge such as question answering.

### Languages

English

## Dataset Structure

### Data Instances

```python
{
  "subject": "elephant",
  "predicate": "has_body_part"
  "object": "trunk",
  "modality": "TBC[so long trunks] x#x2 // TBC[long trunks] x#x9 // TBC[big trunks] x#x6 // TBC[long trunk] x#x1 // TBC[such big trunks] x#x1	0	0.9999667967035647	elephants have trunks x#x34 x#xGoogle Autocomplete, Bing Autocomplete, Yahoo Questions, Answers.com Questions, Reddit Questions // a elephants have trunks x#x2 x#xGoogle Autocomplete // a elephant have a trunk x#x2 x#xGoogle Autocomplete // elephants have so long trunks x#x2 x#xGoogle Autocomplete // elephants have long trunks x#x8 x#xGoogle Autocomplete, Yahoo Questions, Answers.com Questions // elephants have big trunks x#x6 x#xGoogle Autocomplete, Answers.com Questions, Reddit Questions // elephants have trunk x#x3 x#xGoogle Autocomplete, Yahoo Questions // elephant have long trunks x#x1 x#xGoogle Autocomplete // elephant has a trunk x#x1 x#xGoogle Autocomplete // elephants have a trunk x#x2 x#xAnswers.com Questions // an elephant has a long trunk x#x1 x#xAnswers.com Questions // elephant have trunks x#x1 x#xAnswers.com Questions // elephants have such big trunks x#x1 x#xReddit Questions",
  "score": 0.9999667967668732,
  "local_sigma": 1.0
}
```

### Data Fields

- subject: The subject of the triple
- predicate: The predicate of the triple
- object: The object of the triple
- modality: Modalities associated with the triples with their counts. TBC means the object can be further refined to the listed objects
- is_negative: 1 if the statement was negated
- score: salience score of the supervised scoring model
- local sigma: strict conditional probability of observing a (predicate, object) with a specific subject. I.e., a measure of how unique a statement is. E.g., local_sigma(lawyers, defend, serial_killers) = 1, local_sigma(lawyers, make, money) = 0.01, even though both statements have a similar score of 0.99.



## Dataset Creation

See original paper.

## Additional Information

### Licensing Information

CC-BY 2.0

### Citation Information

Romero et al., Commonsense Properties from Query Logs and Question Answering Forums, CIKM, 2019
