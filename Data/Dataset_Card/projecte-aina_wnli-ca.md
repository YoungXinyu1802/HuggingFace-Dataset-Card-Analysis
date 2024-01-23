---
YAML tags:

annotations_creators:
- expert-generated
language_creators:
- found
language:
- ca
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: wnli-ca
size_categories:
- unknown
source_datasets: 
- extended|glue
task_categories:
- text-classification
task_ids:
- natural-language-inference

---


# WNLI-ca

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

This dataset is a professional translation into Catalan of [Winograd NLI dataset](https://dl.fbaipublicfiles.com/glue/data/WNLI.zip) as published in [GLUE Benchmark](https://gluebenchmark.com/tasks).

Both the original dataset and this translation are licenced under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

### Supported Tasks and Leaderboards

Textual entailment, Text classification, Language Model.

### Languages

The dataset is in Catalan (`ca-CA`)

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
### Example

|  index  |   sentence 1  |  sentence 2  |  label  | 
| ------- |----------- | --------- | ----- | 
| 0 | Vaig clavar una agulla en una pastanaga. Quan la vaig treure, tenia un forat. | La pastanaga tenia un forat. | 1 |
| 1 | En Joan no podia veure l’escenari amb en Guillem davant seu perquè és molt baix. | En Joan és molt baix. | 1 |
| 2 | Els policies van arrestar tots els membres de la banda. Volien aturar el tràfic de drogues del barri. | Els policies volien aturar el tràfic de drogues del barri. | 1 |
| 3 | L’Esteve segueix els passos d’en Frederic en tot. L’influencia moltíssim. | L’Esteve l’influencia moltíssim. | 0 |
  
### Data Splits

- wnli-train-ca.csv: 636
- wnli-dev-ca.csv: 72
- wnli-test-shuffled-ca.csv: 147 

## Dataset Creation

### Curation Rationale

We translated this dataset to contribute to the development of language models in Catalan, a low-resource language, and to allow inter-lingual comparisons. 

### Source Data

- [GLUE Benchmark site](https://gluebenchmark.com)

#### Initial Data Collection and Normalization

This is a professional translation of [WNLI dataset](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) into Catalan, commissioned by BSC TeMU within the [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/).

For more information on how the Winograd NLI dataset was created, visit the webpage [The Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

#### Who are the source language producers?

For more information on how the Winograd NLI dataset was created, visit the webpage [The Winograd Schema Challenge](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html).

### Annotations

#### Annotation process

We comissioned a professional translation of [WNLI dataset](https://cs.nyu.edu/~davise/papers/WinogradSchemas/WS.html) into Catalan.

#### Who are the annotators?

Translation was commisioned to a professional translator.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset contributes to the development of language models in Catalan, a low-resource language.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es).

This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


### Licensing Information

This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">CC Attribution 4.0 International License</a>.


### Contributions

[N/A]
