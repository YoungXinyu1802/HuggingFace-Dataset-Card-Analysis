---
YAML tags:

annotations_creators:
- expert-generated
language:
- es
language_creators:
- found
multilinguality:
- monolingual
pretty_name: CoNLL-NERC-es
size_categories: []
source_datasets: []
tags: []
task_categories:
- token-classification
task_ids:
- part-of-speech

---


# CoNLL-NERC-es

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
- **Website:** https://www.cs.upc.edu/~nlp/tools/nerc/nerc.html
- **Point of Contact:** [Xavier Carreras](carreras@lsi.upc.es) 


### Dataset Summary

CoNLL-NERC is the Spanish dataset of the CoNLL-2002 Shared Task [(Tjong Kim Sang, 2002)](https://aclanthology.org/W02-2024.pdf). The dataset is annotated with four types of named entities --persons, locations, organizations, and other miscellaneous entities-- formatted in the standard Beginning-Inside-Outside (BIO) format. The corpus consists of 8,324 train sentences with 19,400 named entities, 1,916 development sentences with 4,568 named entities, and 1,518 test sentences with 3,644 named entities.

We use this corpus as part of the EvalEs Spanish language benchmark. 

### Supported Tasks and Leaderboards

Named Entity Recognition and Classification

### Languages

The dataset is in Spanish (`es-ES`)

## Dataset Structure

### Data Instances

<pre>
El DA O
Abogado NC B-PER
General AQ I-PER
del SP I-PER
Estado NC I-PER
, Fc O
Daryl VMI B-PER
Williams NC I-PER
, Fc O
subrayó VMI O
hoy RG O
la DA O
necesidad NC O
de SP O
tomar VMN O
medidas NC O
para SP O
proteger VMN O
al SP O
sistema NC O
judicial AQ O
australiano AQ O
frente RG O
a SP O
una DI O
página NC O
de SP O
internet NC O
que PR O
imposibilita VMI O
el DA O
cumplimiento NC O
de SP O
los DA O
principios NC O
básicos AQ O
de SP O
la DA O
Ley NC B-MISC
. Fp O
</pre>

### Data Fields

Every file has two columns, with the word form or punctuation symbol in the first one and the corresponding IOB tag in the second one. The different files are separated by an empty line. 

### Data Splits

- esp.train: 273037 lines
- esp.testa: 54837 lines (used as dev)
- esp.testb: 53049 lines (used as test)

## Dataset Creation

### Curation Rationale
[N/A] 

### Source Data

The data is a collection of news wire articles made available by the Spanish EFE News Agency. The articles are from May 2000.

#### Initial Data Collection and Normalization

For more information visit the paper from the CoNLL-2002 Shared Task [(Tjong Kim Sang, 2002)](https://aclanthology.org/W02-2024.pdf).

#### Who are the source language producers?

For more information visit the paper from the CoNLL-2002 Shared Task [(Tjong Kim Sang, 2002)](https://aclanthology.org/W02-2024.pdf).

### Annotations

#### Annotation process

For more information visit the paper from the CoNLL-2002 Shared Task [(Tjong Kim Sang, 2002)](https://aclanthology.org/W02-2024.pdf).

#### Who are the annotators?

The annotation was carried out by the TALP Research Center2 of the Technical University of Catalonia (UPC) and the Center of Language and Computation (CLiC3 ) of the University of Barcelona (UB), and funded by the European Commission through the NAMIC pro ject (IST-1999-12392).

For more information visit the paper from the CoNLL-2002 Shared Task [(Tjong Kim Sang, 2002)](https://aclanthology.org/W02-2024.pdf).

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Spanish.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]


## Additional Information


### Dataset curators


### Licensing information


### Citation Information

The following paper must be cited when using this corpus:

Erik F. Tjong Kim Sang. 2002. Introduction to the CoNLL-2002 Shared Task: Language-Independent Named Entity Recognition. In COLING-02: The 6th Conference on Natural Language Learning 2002 (CoNLL-2002).


### Contributions

[N/A]


