---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- es
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- cc-news
task_categories:
- summarization
- text-generation
task_ids: []
tags:
- conditional-text-generation
---

# Dataset Card for CC-NEWS-ES-titles

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

- **Homepage:** 
- **Repository:** [CC-NEWS-ES-titles dataset repository](https://huggingface.co/datasets/LeoCordoba/CC-NEWS-ES-titles)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [Leonardo Ignacio Córdoba](https://www.linkedin.com/in/leonardo-ignacio-c%C3%B3rdoba/)

### Dataset Summary

CC-NEWS-ES-titles is a Spanish-language dataset for news titles generation. The text and titles comes from 2019 and 2020 CC-NEWS data (which is part of Common Crawl).

It contains 402.310 pairs of news title and body, splitted in :

- Train: 370.125

- Eval: 16.092

- Test: 16.092

### Supported Tasks and Leaderboards

- `text-classification`, `sentiment-classification`: The dataset can be used to train a model for news title generation which can be considered a subset of abstractive summarization.


### Languages

The text is in Spanish. The BCP-47 code for Spanish is es.

## Dataset Structure

### Data Instances

Each data instance contains the following features: _text_ and _output_text_. 

- _text_ is the body of the news.
- _output_text_ is the title of the news.


An example from the CC-NEWS-ES-titles train set looks like the following:
```
{'text': 'Hoy en el Boletín Oficial también se publicó la disposición para universidades, institutos universitarios y de educación superior de todas las jurisdicciones, a las que recomienda que "adecúen las condiciones en que se desarrolla la actividad académica presencial en el marco de la emergencia conforme con las recomendaciones del Ministerio de Salud", según lo publicado por la agencia	',
 'output_text': 'Coronavirus: "Seguimos educando", la plataforma online para que los chicos estudien en cuarentena'}

```

### Data Fields

- 'text': a string containing the body of the news.
- 'output_text': a string containing the title of the news.

### Data Splits

The CC-NEWS-ES-titles dataset has 3 splits: _train_, _validation_, and _test_. The splits contain disjoint sets of news.

| Dataset Split | Number of Instances in Split |
| ------------- | ---------------------------- |
| Train         | 370.125                      |
| Eval          | 16.092                       |
| Test          | 16.092                       |

## Dataset Creation

### Curation Rationale

[N/A]

### Source Data

#### Initial Data Collection and Normalization

TODO

#### Who are the source language producers?

Common Crawl: https://commoncrawl.org/

### Annotations

The dataset does not contain any additional annotations. 

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

Abstractive summarization is a complex task and Spanish is a underrepresented language in the NLP domain. As a consequence, adding a Spanish resource may help others to improve their research and educational activities.

### Discussion of Biases

[N/A]

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

This dataset is maintained by [Leonardo Ignacio Córdoba](https://www.linkedin.com/in/leonardo-ignacio-c%C3%B3rdoba/) and was built with the help of [María Gaska](https://www.linkedin.com/in/mfgaska/).

### Licensing Information

[N/A]

### Citation Information

TODO
### Contributions

[N/A]