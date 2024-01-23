---
annotations_creators:
- expert-generated
language:
- jam
language_creators:
- expert-generated
- found
license:
- other
multilinguality:
- monolingual
- other-english-based-creole
pretty_name: JamPatoisNLI
size_categories:
- n<1K
source_datasets:
- original
tags:
- creole
- low-resource-language
task_categories:
- text-classification
task_ids:
- natural-language-inference
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

- **Homepage:**
- jampatoisnli.github.io
- **Repository:**
- https://github.com/ruth-ann/jampatoisnli
- **Paper:**
- https://arxiv.org/abs/2212.03419
- **Point of Contact:**
- Ruth-Ann Armsrong: armstrongruthanna@gmail.com

### Dataset Summary

JamPatoisNLI provides the first dataset for natural language inference in a creole language, Jamaican Patois. 
Many of the most-spoken low-resource languages are creoles. These languages commonly have a lexicon derived from 
a major world language and a distinctive grammar reflecting the languages of the original speakers and the process
of language birth by creolization. This gives them a distinctive place in exploring the effectiveness of transfer
from large monolingual or multilingual pretrained models. 

### Supported Tasks and Leaderboards

Natural language inference

### Languages

Jamaican Patois

### Data Fields

premise, hypothesis, label

### Data Splits

Train: 250
Val: 200
Test: 200


### Data set creation + Annotations

Premise collection: 
97% of examples from Twitter; remaining pulled from literature and online cultural website

Hypothesis construction: 
For each premise, hypothesis written by native speaker (our first author) so that pair’s classification would be  E, N  or C

Label validation: 
Random sample of 100 sentence pairs double annotated by fluent speakers


### Social Impact of Dataset

JamPatoisNLI is a low-resource language dataset in an English-based Creole spoken in the Caribbean,
Jamaican Patois. The creation of the dataset contributes to expanding the scope of NLP research
to under-explored languages across the world.


### Dataset Curators

[@ruth-ann](https://github.com/ruth-ann)


### Citation Information

@misc{https://doi.org/10.48550/arxiv.2212.03419,
  doi = {10.48550/ARXIV.2212.03419},
  
  url = {https://arxiv.org/abs/2212.03419},
  
  author = {Armstrong, Ruth-Ann and Hewitt, John and Manning, Christopher},
  
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.7},
  
  title = {JamPatoisNLI: A Jamaican Patois Natural Language Inference Dataset},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}

### Contributions

Thanks to Prof. Christopher Manning and John Hewitt for their contributions, guidance, facilitation and support related to the creation of this dataset.
