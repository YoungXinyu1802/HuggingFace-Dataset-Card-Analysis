---
annotations_creators:
- other
language:
- sv
language_creators:
- other
license: []
multilinguality:
- monolingual
pretty_name: 'A standardized suite for evaluation and analysis of Swedish natural
  language understanding systems.'
size_categories:
- unknown
source_datasets: []
tags: []
task_categories:
- multiple-choice
- text-classification
- question-answering
- sentence-similarity
- token-classification
task_ids:
- sentiment-analysis
- acceptability-classification
- closed-domain-qa
- word-sense-disambiguation
- coreference-resolution
---
# Dataset Card for [Dataset Name]

## Table of Contents
- [Table of Contents](#table-of-contents)
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

- **Homepage:** [The official homepage of Språkbanken](https://spraakbanken.gu.se/resurser/superlim/)
- **Repository:**
- **Paper:**[SwedishGLUE – Towards a Swedish Test Set for Evaluating Natural Language Understanding Models](https://gup.ub.gu.se/publication/299130?lang=sv)
- **Leaderboard:** [To be implemented]
- **Point of Contact:**[sb-info@svenska.gu.se](sb-info@svenska.gu.se)

### Dataset Summary

SuperLim 2.0 is a continuation of SuperLim 1.0, which aims for a standardized suite for evaluation and analysis of Swedish natural language understanding systems. The projects is inspired by the GLUE/SuperGLUE projects from which the name is derived: "lim" is the Swedish translation of "glue".   

### Supported Tasks and Leaderboards

[More Information Needed] 

### Languages

Swedish

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

Most datasets have a train, dev and test split. However, there are a few (`supersim`, `sweanalogy` and `swesat-synonyms`) who only have a train and test split. The diagnostic tasks `swediagnostics` and `swewinogender` only have a test split, but they could be evaluated on models trained on `swenli` since they are also NLI-based.

## Dataset Creation


### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

To cite as a whole, use the standard reference. If you use or reference individual resources, cite the references specific for these resources:
 
Standard reference:

Yvonne Adesam, Aleksandrs Berdicevskis, Felix Morger (2020): [SwedishGLUE – Towards a Swedish Test Set for Evaluating Natural Language Understanding Models] (https://gup.ub.gu.se/publication/299130?lang=sv)

Dataset references:

[More information needed]

Thanks to [Felix Morger](https://github.com/felixhultin) for adding this dataset.