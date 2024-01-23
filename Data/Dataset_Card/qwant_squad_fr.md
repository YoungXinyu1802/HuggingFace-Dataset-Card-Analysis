---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- fr-FR
license:
- cc-by-4.0
multilinguality:
- monolingual
- translation
paperswithcode_id: squad
pretty_name: SQuAD-fr
size_categories:
- 10K<n<100K
source_datasets:
- extended|squad
task_categories:
- question-answering
task_ids:
- extractive-qa
- closed-domain-qa
---


# Dataset Card for "squad_fr"
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
## Dataset Description
- **Paper:**  [On the Usability of Transformers-based models for a French Question-Answering task](https://hal.archives-ouvertes.fr/hal-03336060)
- **Size of downloaded dataset files:** 10 MB
- **Size of the generated dataset:** 73 MB
- **Total amount of disk used:** 83 MB
### Dataset Summary
SQuAD-fr:
- a translated version of the Stanford Question Answering Dataset (SQuAD) into French
  - obtained through automatic translation of the English dataset
- a reading comprehension dataset, consisting of approximately 90K factoid questions on Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage
- serves as a means of data augmentation on FQuAD and PIAF benchmarks
### Supported Tasks and Leaderboards
- `closed-domain-qa`, `text-retrieval`: This dataset is intended to be used for `closed-domain-qa`, but can also be used for information retrieval tasks.
### Languages
This dataset is exclusively in French.
## Dataset Structure
### Data Instances
#### default
- **Size of downloaded dataset files:** 10 MB
- **Size of the generated dataset:** 73 MB
- **Total amount of disk used:** 83 MB
An example of 'train' looks as follows.
```
{
    "answers": {
        "answer_start": [1],
        "text": ["This is a test text"]
    },
    "context": "This is a test context.",
    "id": "1",
    "question": "Is this a test?",
    "title": "train test"
}
```
### Data Fields
The data fields are the same among all splits.
#### plain_text
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

### Data Splits
|   name   |train|validation|
|----------|----:|---------:|
|1.1.0|87514|     17492|
## Dataset Creation
### Curation Rationale
Usability of Transformer-based models, instability relating to data scarcity, investigation of data augmentation, hyperparameters optimization and cross-lingual transfer on the performance of a question-answering task in French.
### Source Data
#### Initial Data Collection and Normalization
validation: manually collected gold standards, chrf scores and bleu evaluation
#### Who are the source language producers?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Annotations
#### Annotation process
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the annotators?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Personal and Sensitive Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Discussion of Biases
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Other Known Limitations
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Additional Information
### Dataset Curators
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Licensing Information
Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
### Citation Information
```
@inproceedings{cattan:hal-03336060,
  TITLE = {{On the Usability of Transformers-based models for a French Question-Answering task}},
  AUTHOR = {Cattan, Oralie and Servan, Christophe and Rosset, Sophie},
  URL = {https://hal.archives-ouvertes.fr/hal-03336060},
  BOOKTITLE = {{Recent Advances in Natural Language Processing (RANLP)}},
  ADDRESS = {Varna, Bulgaria},
  YEAR = {2021},
  MONTH = Sep,
  PDF = {https://hal.archives-ouvertes.fr/hal-03336060/file/RANLP_2021_transformers_usability.pdf},
  HAL_ID = {hal-03336060},
  HAL_VERSION = {v1},
}
```