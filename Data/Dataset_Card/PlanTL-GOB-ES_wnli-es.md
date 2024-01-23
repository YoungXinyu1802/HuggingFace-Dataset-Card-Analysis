---
YAML tags:

annotations_creators:
- expert-generated
language_creators:
- found
language:
- es
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: wnli-es
size_categories:
- unknown
source_datasets: 
- extended|glue
task_categories:
- text-classification
task_ids:
- natural-language-inference

---


# WNLI-es

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
- **Website:** https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html
- **Point of Contact:** [Carlos Rodríguez-Penagos](carlos.rodriguez1@bsc.es) and [Carme Armentano-Oller](carme.armentano@bsc.es)


### Dataset Summary

"A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its resolution. The schema takes its name from Terry Winograd." Source: [The Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

The [Winograd NLI dataset](https://dl.fbaipublicfiles.com/glue/data/WNLI.zip) presents 855 sentence pairs, in which the first sentence contains an ambiguity and the second one a possible interpretation of it. The label indicates if the interpretation is correct (1) or not (0).

This dataset is a professional translation into Spanish of [Winograd NLI dataset](https://dl.fbaipublicfiles.com/glue/data/WNLI.zip) as published in [GLUE Benchmark](https://gluebenchmark.com/tasks).

Both the original dataset and this translation are licenced under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

### Supported Tasks and Leaderboards

Textual entailment, Text classification, Language Model.

### Languages

* Spanish (es)

## Dataset Structure

### Data Instances

Three tsv files.

### Data Fields

- index
- sentence 1: first sentence of the pair
- sentence 2: second sentence of the pair
- label: relation between the two sentences:
    * 0: the second sentence does not entail a correct interpretation of the first one (neutral)
    * 1: the second sentence entails a correct interpretation of the first one (entailment)
  
### Data Splits

- wnli-train-es.csv: 636 sentence pairs
- wnli-dev-es.csv: 72 sentence pairs
- wnli-test-shuffled-es.csv: 147 sentence pairs

## Dataset Creation

### Curation Rationale

We translated this dataset to contribute to the development of language models in Spanish. 

### Source Data

- [GLUE Benchmark site](https://gluebenchmark.com)

#### Initial Data Collection and Normalization

This is a professional translation of [WNLI dataset](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) into Spanish, commissioned by [BSC TeMU](https://temu.bsc.es/) within the the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

For more information on how the Winograd NLI dataset was created, visit the webpage [The Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

#### Who are the source language producers?

For more information on how the Winograd NLI dataset was created, visit the webpage [The Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

### Annotations

#### Annotation process

We comissioned a professional translation of [WNLI dataset](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) into Spanish.

#### Who are the annotators?

Translation was commisioned to a professional translation agency.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Spanish.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators 
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es). 

For further information, send an email to (plantl-gob-es@bsc.es).

This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://avancedigital.mineco.gob.es/en-us/Paginas/index.aspx) within the framework of the [Plan-TL](https://plantl.mineco.gob.es/Paginas/index.aspx).

### Licensing information
This work is licensed under [CC Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) License.

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Contributions
[N/A]

