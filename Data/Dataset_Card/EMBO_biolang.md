---
annotations_creators:
- machine-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- n>1M
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Dataset Card for BioLang

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
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

- **Homepage:** https://sourcedata.embo.org
- **Repository:** https://github.com/source-data/soda-roberta
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** thomas.lemberger@embo.org
- **Download Size:** 5_299_878_661

### Dataset Summary

BioLang is a dataset is based on abstracts from the open access section of EuropePubMed Central to train language models in the domain of biology. The dataset can be used for random masked language modeling or for language modeling using only specific part-of-speech maksing. More details on generation and use of the dataset at https://github.com/source-data/soda-roberta .

### Supported Tasks and Leaderboards

- `MLM`: masked language modeling
- `DET`: part-of-speach masked language model, with determinants (`DET`) tagged
- `SMALL`: part-of-speech masked language model, with "small" words (`DET`, `CCONJ`, `SCONJ`, `ADP`, `PRON`) tagged
- `VERB`: part-of-speach masked language model, with  verbs (`VERB`) tagged


### Languages

English

## Dataset Structure

### Data Instances

```json
{
    "input_ids":[
        0, 2444, 6997, 46162, 7744, 35, 20632, 20862, 3457, 36, 500, 23858, 29, 43, 32, 3919, 716, 15, 49, 4476, 4, 1398, 6, 52, 1118, 5, 20862, 819, 9, 430, 23305, 248, 23858, 29, 4, 256, 40086, 104, 35, 1927, 1069, 459, 1484, 58, 4776, 13, 23305, 634, 16706, 493, 2529, 8954, 14475, 73, 34263, 6, 4213, 718, 833, 12, 24291, 4473, 22500, 14475, 73, 510, 705, 73, 34263, 6, 5143, 4313, 2529, 8954, 14475, 73, 34263, 6, 8, 5143, 4313, 2529, 8954, 14475, 248, 23858, 29, 23, 4448, 225, 4722, 2392, 11, 9341, 261, 4, 49043, 35, 96, 746, 6, 5962, 9, 38415, 4776, 408, 36, 3897, 4, 398, 8871, 56, 23305, 4, 20, 15608, 21, 8061, 6164, 207, 13, 70, 248, 23858, 29, 6, 150, 5, 42561, 21, 8061, 5663, 207, 13, 80, 3457, 4, 509, 1296, 5129, 21567, 3457, 36, 398, 23528, 8748, 22065, 11654, 35, 7253, 15, 49, 4476, 6, 70, 3457, 4682, 65, 189, 28, 5131, 13, 23305, 9726, 4, 2
    ], 
    "label_ids": [
        "X", "NOUN", "NOUN", "NOUN", "NOUN", "PUNCT", "ADJ", "ADJ", "NOUN", "PUNCT", "PROPN", "PROPN", "PROPN", "PUNCT", "AUX", "VERB", "VERB", "ADP", "DET", "NOUN", "PUNCT", "ADV", "PUNCT", "PRON", "VERB", "DET", "ADJ", "NOUN", "ADP", "ADJ", "NOUN", "NOUN", "NOUN", "NOUN", "PUNCT", "ADJ", "ADJ", "ADJ", "PUNCT", "NOUN", "NOUN", "NOUN", "NOUN", "AUX", "VERB", "ADP", "NOUN", "VERB", "PROPN", "PROPN", "PROPN", "PROPN", "PROPN", "SYM", "PROPN", "PUNCT", "PROPN", "PROPN", "PROPN", "PUNCT", "PROPN", "PROPN", "PROPN", "PROPN", "SYM", "PROPN", "PROPN", "SYM", "PROPN", "PUNCT", "PROPN", "PROPN", "PROPN", "PROPN", "PROPN", "SYM", "PROPN", "PUNCT", "CCONJ", "ADJ", "PROPN", "PROPN", "PROPN", "PROPN", "NOUN", "NOUN", "NOUN", "ADP", "PROPN", "PROPN", "PROPN", "PROPN", "ADP", "PROPN", "PROPN", "PUNCT", "PROPN", "PUNCT", "ADP", "NOUN", "PUNCT", "NUM", "ADP", "NUM", "VERB", "NOUN", "PUNCT", "NUM", "NUM", "NUM", "NOUN", "AUX", "NOUN", "PUNCT", "DET", "NOUN", "AUX", "X", "NUM", "NOUN", "ADP", "DET", "NOUN", "NOUN", "NOUN", "PUNCT", "SCONJ", "DET", "NOUN", "AUX", "X", "NUM", "NOUN", "ADP", "NUM", "NOUN", "PUNCT", "NUM", "NOUN", "VERB", "ADJ", "NOUN", "PUNCT", "NUM", "NOUN", "NOUN", "NOUN", "NOUN", "PUNCT", "VERB", "ADP", "DET", "NOUN", "PUNCT", "DET", "NOUN", "SCONJ", "PRON", "VERB", "AUX", "VERB", "ADP", "NOUN", "NOUN", "PUNCT", "X"
    ], 
    "special_tokens_mask": [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
    ]
}
```


### Data Fields

`MLM`:
- `input_ids`: a `list` of `int32` features.
- `special_tokens_mask`: a `list` of `int8` features.

`DET`, `VERB`, `SMALL`:
- `input_ids`: a `list` of `int32` features.
- `tag_mask`: a `list` of `int8` features.


### Data Splits

- `train`:
  - features: ['input_ids', 'special_tokens_mask'],
  - num_rows: 12_005_390
- `test`:
  - features: ['input_ids', 'special_tokens_mask'],
  - num_rows: 37_112
- `validation`:
  - features: ['input_ids', 'special_tokens_mask'],
  - num_rows: 36_713

## Dataset Creation

### Curation Rationale

The dataset was assembled to train language models in the field of cell and molecular biology. To expand the size of the dataset and to include many examples with highly technical language, abstracts were complemented with figure legends (or figure 'captions'). 

### Source Data

#### Initial Data Collection and Normalization

The xml content of papers were downloaded in January 2021 from the open access section of [EuropePMC]("https://europepmc.org/downloads/openaccess"). Figure legends and abstracts were extracted from the JATS XML, tokenized with the `roberta-base` tokenizer and part-of-speech tagged with Spacy's `en_core_web_sm` model (https://spacy.io).

More details at https://github.com/source-data/soda-roberta

#### Who are the source language producers?

Experts scientists.

### Annotations

#### Annotation process

Part-of-speech was tagged automatically. 

#### Who are the annotators?

Spacy's `en_core_web_sm` model (https://spacy.io) was used for part-of-speech tagging.

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

Thomas Lemberger

### Licensing Information

CC-BY 4.0

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@tlemberger](https://github.com/tlemberger) for adding this dataset.
