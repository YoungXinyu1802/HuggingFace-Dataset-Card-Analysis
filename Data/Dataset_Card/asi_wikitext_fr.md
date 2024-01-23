---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- fr
language_bcp47:
- fr-FR
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Wikitext-fr
size_categories:
- unknown
source_datasets:
- original
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---

# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Repository:** [https://github.com/AntoineSimoulin/gpt-fr](https://github.com/AntoineSimoulin/gpt-fr)
- **Paper:** [https://aclanthology.org/2021.jeptalnrecital-taln.24.pdf](https://aclanthology.org/2021.jeptalnrecital-taln.24.pdf)

### Dataset Summary

Wikitext-fr language modeling dataset consists of over 70 million tokens extracted from the set of french Wikipedia articles that are classified as "quality articles" or "good articles". It is designed to mirror the english benchmark from Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. 2016.
[Pointer Sentinel Mixture Models](https://arxiv.org/abs/1609.07843) The dataset is available under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/)

### Supported Tasks and Leaderboards

- `language-modeling`: The dataset can be used to evaluate the generation abilites of a model. Success on this task is typically measured by achieving a *low* perplexity. The ([model name](https://huggingface.co/asi/gpt-fr-cased-base) currently achieves 12.9.

### Languages

The dataset is in French.

## Dataset Structure

### Data Instances

The dataset consists in the agregation of paragraphs from wikipedia articles.

```
{
  'paragraph': ...,
  ...
}
```


### Data Fields

- `paragraph`: This is a paragraph from the original wikipedia article.

### Data Splits

The dataset is splited into a train/valid/test split.

|                            | Tain (35)   | Train (72) | Valid | Test |
| -----                      | ------ | ----- | ---- | ---- |
| Number of Documents        |   2 126   | 5 902 |  60  |  60  |
| Number of tokens           |   351 66  |  72 961  | 896 | 897 |
| Vocabulary size           |   137 589  |  205 403  |  |  |
| Out of   Vocabulary   |   0.8%  |   1.2%  |  |  |


## Dataset Creation

### Curation Rationale

The dataset is created to evaluate French models with similart criteria than English.s

### Source Data

Wikitext-fr language modeling dataset consists of over 70 million tokens extracted from the set of french Wikipedia articles that are classified as "quality articles" or "good articles". 
We did not apply specific pre-treatments as transformers models might use a dedicated tokenization.s

#### Initial Data Collection and Normalization

We used the Wikipedia API to collect the articles since cleaning Wikipedia articles from dumps is not a trivial task.


### Personal and Sensitive Information

## Considerations for Using the Data

### Social Impact of Dataset

### Discussion of Biases

### Other Known Limitations

## Additional Information

### Dataset Curators

### Licensing Information

The dataset is available under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/)

### Citation Information

```
@inproceedings{simoulin:hal-03265900,
  TITLE = {{Un mod{\`e}le Transformer G{\'e}n{\'e}ratif Pr{\'e}-entrain{\'e} pour le \_\_\_\_\_\_ fran{\c c}ais}},
  AUTHOR = {Simoulin, Antoine and Crabb{\'e}, Benoit},
  URL = {https://hal.archives-ouvertes.fr/hal-03265900},
  BOOKTITLE = {{Traitement Automatique des Langues Naturelles}},
  ADDRESS = {Lille, France},
  EDITOR = {Denis, Pascal and Grabar, Natalia and Fraisse, Amel and Cardon, R{\'e}mi and Jacquemin, Bernard and Kergosien, Eric and Balvet, Antonio},
  PUBLISHER = {{ATALA}},
  PAGES = {246-255},
  YEAR = {2021},
  KEYWORDS = {fran{\c c}ais. ; GPT ; G{\'e}n{\'e}ratif ; Transformer ; Pr{\'e}-entra{\^i}n{\'e}},
  PDF = {https://hal.archives-ouvertes.fr/hal-03265900/file/7.pdf},
  HAL_ID = {hal-03265900},
  HAL_VERSION = {v1},
}
```


### Contributions

Thanks to [@AntoineSimoulin](https://github.com/AntoineSimoulin) for adding this dataset.