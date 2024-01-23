---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-retrieval
- text-generation
task_ids: []
pretty_name: rebel-dataset
tags:
- relation-extraction
- conditional-text-generation
---

# Dataset Card for REBEL dataset

## Table of Contents
- [Dataset Card for REBEL dataset](#dataset-card-for-rebel)
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

- **Repository:** [https://github.com/Babelscape/rebel](https://github.com/Babelscape/rebel)
- **Paper:** [https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf)
- **Point of Contact:** [huguetcabot@babelscape.com](huguetcabot@babelscape.com)

### Dataset Summary

Dataset created for [REBEL](https://huggingface.co/Babelscape/rebel-large) dataset from interlinking Wikidata and Wikipedia for Relation Extraction, filtered using NLI.

### Supported Tasks and Leaderboards

- `text-retrieval-other-relation-extraction`: The dataset can be used to train a model for Relation Extraction, which consists in extracting triplets from raw text, made of subject, object and relation type. Success on this task is typically measured by achieving a *high* [F1](https://huggingface.co/metrics/F1). The [BART](https://huggingface.co/transformers/model_doc/bart.html)) model currently achieves the following score: 74 Micro F1 and 51 Macro F1 for the 220 most frequent relation types.

### Languages

The dataset is in English, from the English Wikipedia.

## Dataset Structure

### Data Instances

 REBEL

- `Size of downloaded dataset files`: 1490.02 MB
- `Size of the generated dataset`: 1199.27 MB
- `Total amount of disk used`: 2689.29 MB


```
{
  'id': 'Q82442-1',
  'title': 'Arsène Lupin, Gentleman Burglar',
  'context': 'Arsène Lupin , Gentleman Burglar is the first collection of stories by Maurice Leblanc recounting the adventures of Arsène Lupin , released on 10 June 1907 .',
  'triplets': '<triplet> Arsène Lupin, Gentleman Burglar <subj> Maurice Leblanc <obj> author <triplet> Arsène Lupin <subj> Maurice Leblanc <obj> creator'
}
```

The original data is in jsonl format and contains much more information. It is divided by Wikipedia articles instead of by sentence, and contains metadata about Wikidata entities, their boundaries in the text, how it was annotated, etc. For more information check the [paper repository](https://huggingface.co/Babelscape/rebel-large) and how it was generated using the Relation Extraction dataset pipeline, [cRocoDiLe](https://github.com/Babelscape/crocodile).

### Data Fields

List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.

- `id`: ID of the instance. It contains a unique id matching to a Wikipedia page and a number separated by a hyphen indicating which sentence of the Wikipedia article it is.
- `title`: Title of the Wikipedia page the sentence comes from.
- `context`: Text from Wikipedia articles that serves as context for the Relation Extraction task.
- `triplets`: Linearized version of the triplets present in the text, split by the use of special tokens. For more info on this linearization check the [paper](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf).

### Data Splits

Test and Validation splits are each 5% of the original data. 

Provide the sizes of each split. As appropriate, provide any descriptive statistics for the features, such as average length.  For example:

|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |  3,120,296  | 172,860 | 173,601 |
| Input Sentences  (top 220 relation types as used in original paper)          |  784,202  | 43,341 | 43,506 |
| Number of Triplets  (top 220 relation types as used in original paper)          |  878,555  | 48,514 | 48,852 |

## Dataset Creation

### Curation Rationale

This dataset was created to enable the training of a BART based model as pre-training phase for Relation Extraction as seen in the paper [REBEL: Relation Extraction By End-to-end Language generation](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf).

### Source Data

Data comes from Wikipedia text before the table of contents, as well as Wikidata for the triplets annotation.

#### Initial Data Collection and Normalization

For the data collection, the dataset extraction pipeline [cRocoDiLe: Automati**c** **R**elati**o**n Extra**c**ti**o**n **D**ataset w**i**th N**L**I filt**e**ring](https://github.com/Babelscape/crocodile) insipired by [T-REx Pipeline](https://github.com/hadyelsahar/RE-NLG-Dataset) more details found at: [T-REx Website](https://hadyelsahar.github.io/t-rex/). The starting point is a Wikipedia dump as well as a Wikidata one.

After the triplets are extracted, an NLI system was used to filter out those not entailed by the text.

#### Who are the source language producers?

Any Wikipedia and Wikidata contributor.

### Annotations



#### Annotation process

The dataset extraction pipeline [cRocoDiLe: Automati**c** **R**elati**o**n Extra**c**ti**o**n **D**ataset w**i**th N**L**I filt**e**ring](https://github.com/Babelscape/crocodile).

#### Who are the annotators?

Automatic annottations

### Personal and Sensitive Information

All text is from Wikipedia, any Personal or Sensitive Information there may be present in this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

The dataset serves as a pre-training step for Relation Extraction models. It is distantly annotated, hence it should only be used as such. A model trained solely on this dataset may produce allucinations coming from the silver nature of the dataset. 

### Discussion of Biases

Since the dataset was automatically created from Wikipedia and Wikidata, it may reflect the biases withing those sources. 

For Wikipedia text, see for example [Dinan et al 2020 on biases in Wikipedia (esp. Table 1)](https://arxiv.org/abs/2005.00614), or [Blodgett et al 2020](https://www.aclweb.org/anthology/2020.acl-main.485/) for a more general discussion of the topic.

For Wikidata, there are class imbalances, also resulting from Wikipedia.

### Other Known Limitations

Not for now

## Additional Information

### Dataset Curators

Pere-Lluis Huguet Cabot - Babelscape and Sapienza University of Rome, Italy
Roberto Navigli - Sapienza University of Rome, Italy

### Licensing Information

Contents of this repository are restricted to only non-commercial research purposes under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright of the dataset contents belongs to the original copyright holders.

### Citation Information

Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example:
```
@inproceedings{huguet-cabot-navigli-2021-rebel,
title = "REBEL: Relation Extraction By End-to-end Language generation",
author = "Huguet Cabot, Pere-Llu{\'\i}s  and
    Navigli, Roberto",
booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
month = nov,
year = "2021",
address = "Online and in the Barceló Bávaro Convention Centre, Punta Cana, Dominican Republic",
publisher = "Association for Computational Linguistics",
url = "https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf",
}
```

### Contributions

Thanks to [@littlepea13](https://github.com/LittlePea13) for adding this dataset.
