---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- other
multilinguality:
- monolingual
pretty_name: FabNER is a manufacturing text dataset for Named Entity Recognition.
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- manufacturing
- 2000-2020
task_categories:
- token-classification
task_ids:
- named-entity-recognition
dataset_info:
- config_name: fabner
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-MATE
          '2': I-MATE
          '3': O-MATE
          '4': E-MATE
          '5': S-MATE
          '6': B-MANP
          '7': I-MANP
          '8': O-MANP
          '9': E-MANP
          '10': S-MANP
          '11': B-MACEQ
          '12': I-MACEQ
          '13': O-MACEQ
          '14': E-MACEQ
          '15': S-MACEQ
          '16': B-APPL
          '17': I-APPL
          '18': O-APPL
          '19': E-APPL
          '20': S-APPL
          '21': B-FEAT
          '22': I-FEAT
          '23': O-FEAT
          '24': E-FEAT
          '25': S-FEAT
          '26': B-PRO
          '27': I-PRO
          '28': O-PRO
          '29': E-PRO
          '30': S-PRO
          '31': B-CHAR
          '32': I-CHAR
          '33': O-CHAR
          '34': E-CHAR
          '35': S-CHAR
          '36': B-PARA
          '37': I-PARA
          '38': O-PARA
          '39': E-PARA
          '40': S-PARA
          '41': B-ENAT
          '42': I-ENAT
          '43': O-ENAT
          '44': E-ENAT
          '45': S-ENAT
          '46': B-CONPRI
          '47': I-CONPRI
          '48': O-CONPRI
          '49': E-CONPRI
          '50': S-CONPRI
          '51': B-MANS
          '52': I-MANS
          '53': O-MANS
          '54': E-MANS
          '55': S-MANS
          '56': B-BIOP
          '57': I-BIOP
          '58': O-BIOP
          '59': E-BIOP
          '60': S-BIOP
  splits:
  - name: train
    num_bytes: 4394010
    num_examples: 9435
  - name: validation
    num_bytes: 934347
    num_examples: 2183
  - name: test
    num_bytes: 940136
    num_examples: 2064
  download_size: 3793613
  dataset_size: 6268493
- config_name: fabner_bio
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-MATE
          '2': I-MATE
          '3': B-MANP
          '4': I-MANP
          '5': B-MACEQ
          '6': I-MACEQ
          '7': B-APPL
          '8': I-APPL
          '9': B-FEAT
          '10': I-FEAT
          '11': B-PRO
          '12': I-PRO
          '13': B-CHAR
          '14': I-CHAR
          '15': B-PARA
          '16': I-PARA
          '17': B-ENAT
          '18': I-ENAT
          '19': B-CONPRI
          '20': I-CONPRI
          '21': B-MANS
          '22': I-MANS
          '23': B-BIOP
          '24': I-BIOP
  splits:
  - name: train
    num_bytes: 4394010
    num_examples: 9435
  - name: validation
    num_bytes: 934347
    num_examples: 2183
  - name: test
    num_bytes: 940136
    num_examples: 2064
  download_size: 3793613
  dataset_size: 6268493
- config_name: fabner_simple
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': MATE
          '2': MANP
          '3': MACEQ
          '4': APPL
          '5': FEAT
          '6': PRO
          '7': CHAR
          '8': PARA
          '9': ENAT
          '10': CONPRI
          '11': MANS
          '12': BIOP
  splits:
  - name: train
    num_bytes: 4394010
    num_examples: 9435
  - name: validation
    num_bytes: 934347
    num_examples: 2183
  - name: test
    num_bytes: 940136
    num_examples: 2064
  download_size: 3793613
  dataset_size: 6268493
- config_name: text2tech
  features:
  - name: id
    dtype: string
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': Technological System
          '2': Method
          '3': Material
          '4': Technical Field
  splits:
  - name: train
    num_bytes: 4394010
    num_examples: 9435
  - name: validation
    num_bytes: 934347
    num_examples: 2183
  - name: test
    num_bytes: 940136
    num_examples: 2064
  download_size: 3793613
  dataset_size: 6268493
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

- **Homepage:** [https://figshare.com/articles/dataset/Dataset_NER_Manufacturing_-_FabNER_Information_Extraction_from_Manufacturing_Process_Science_Domain_Literature_Using_Named_Entity_Recognition/14782407](https://figshare.com/articles/dataset/Dataset_NER_Manufacturing_-_FabNER_Information_Extraction_from_Manufacturing_Process_Science_Domain_Literature_Using_Named_Entity_Recognition/14782407)
- **Paper:** ["FabNER": information extraction from manufacturing process science domain literature using named entity recognition](https://par.nsf.gov/servlets/purl/10290810)
- **Size of downloaded dataset files:** 3.79 MB
- **Size of the generated dataset:** 6.27 MB

### Dataset Summary

FabNER is a manufacturing text corpus of 350,000+ words for Named Entity Recognition.
It is a collection of abstracts obtained from Web of Science through known journals available in manufacturing process 
science research.
For every word, there were categories/entity labels defined namely Material (MATE), Manufacturing Process (MANP), 
Machine/Equipment (MACEQ), Application (APPL), Features (FEAT), Mechanical Properties (PRO), Characterization (CHAR), 
Parameters (PARA), Enabling Technology (ENAT), Concept/Principles (CONPRI), Manufacturing Standards (MANS) and 
BioMedical (BIOP). Annotation was performed in all categories along with the output tag in 'BIOES' format: 
B=Beginning, I-Intermediate, O=Outside, E=End, S=Single.

For details about the dataset, please refer to the paper: ["FabNER": information extraction from manufacturing process science domain literature using named entity recognition](https://par.nsf.gov/servlets/purl/10290810)

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 3.79 MB
- **Size of the generated dataset:** 6.27 MB
  
An example of 'train' looks as follows:
```json
{
  "id": "0", 
  "tokens": ["Revealed", "the", "location-specific", "flow", "patterns", "and", "quantified", "the", "speeds", "of", "various", "types", "of", "flow", "."], 
  "ner_tags": [0, 0, 0, 46, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

### Data Fields

#### fabner
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, a `list` of `string` features.
- `ner_tags`: the list of entity tags, a `list` of classification labels.

```json
{"O": 0, "B-MATE": 1, "I-MATE": 2, "O-MATE": 3, "E-MATE": 4, "S-MATE": 5, "B-MANP": 6, "I-MANP": 7, "O-MANP": 8, "E-MANP": 9, "S-MANP": 10, "B-MACEQ": 11, "I-MACEQ": 12, "O-MACEQ": 13, "E-MACEQ": 14, "S-MACEQ": 15, "B-APPL": 16, "I-APPL": 17, "O-APPL": 18, "E-APPL": 19, "S-APPL": 20, "B-FEAT": 21, "I-FEAT": 22, "O-FEAT": 23, "E-FEAT": 24, "S-FEAT": 25, "B-PRO": 26, "I-PRO": 27, "O-PRO": 28, "E-PRO": 29, "S-PRO": 30, "B-CHAR": 31, "I-CHAR": 32, "O-CHAR": 33, "E-CHAR": 34, "S-CHAR": 35, "B-PARA": 36, "I-PARA": 37, "O-PARA": 38, "E-PARA": 39, "S-PARA": 40, "B-ENAT": 41, "I-ENAT": 42, "O-ENAT": 43, "E-ENAT": 44, "S-ENAT": 45, "B-CONPRI": 46, "I-CONPRI": 47, "O-CONPRI": 48, "E-CONPRI": 49, "S-CONPRI": 50, "B-MANS": 51, "I-MANS": 52, "O-MANS": 53, "E-MANS": 54, "S-MANS": 55, "B-BIOP": 56, "I-BIOP": 57, "O-BIOP": 58, "E-BIOP": 59, "S-BIOP": 60}
```

#### fabner_bio
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, a `list` of `string` features.
- `ner_tags`: the list of entity tags, a `list` of classification labels.

```json
{"O": 0, "B-MATE": 1, "I-MATE": 2, "B-MANP": 3, "I-MANP": 4, "B-MACEQ": 5, "I-MACEQ": 6, "B-APPL": 7, "I-APPL": 8, "B-FEAT": 9, "I-FEAT": 10, "B-PRO": 11, "I-PRO": 12, "B-CHAR": 13, "I-CHAR": 14, "B-PARA": 15, "I-PARA": 16, "B-ENAT": 17, "I-ENAT": 18, "B-CONPRI": 19, "I-CONPRI": 20, "B-MANS": 21, "I-MANS": 22, "B-BIOP": 23, "I-BIOP": 24}
```

#### fabner_simple
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, a `list` of `string` features.
- `ner_tags`: the list of entity tags, a `list` of classification labels.

```json
{"O": 0, "MATE": 1, "MANP": 2, "MACEQ": 3, "APPL": 4, "FEAT": 5, "PRO": 6, "CHAR": 7, "PARA": 8, "ENAT": 9, "CONPRI": 10, "MANS": 11, "BIOP": 12}
```

#### text2tech
- `id`: the instance id of this sentence, a `string` feature.
- `tokens`: the list of tokens of this sentence, a `list` of `string` features.
- `ner_tags`: the list of entity tags, a `list` of classification labels.

```json
{"O": 0, "Technological System": 1, "Method": 2, "Material": 3, "Technical Field": 4}
```

### Data Splits

|        | Train | Dev  | Test |
|--------|-------|------|------|
| fabner | 9435  | 2183 | 2064 |

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

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

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Citation Information

```
@article{DBLP:journals/jim/KumarS22,
  author    = {Aman Kumar and
               Binil Starly},
  title     = {"FabNER": information extraction from manufacturing process science
               domain literature using named entity recognition},
  journal   = {J. Intell. Manuf.},
  volume    = {33},
  number    = {8},
  pages     = {2393--2407},
  year      = {2022},
  url       = {https://doi.org/10.1007/s10845-021-01807-x},
  doi       = {10.1007/s10845-021-01807-x},
  timestamp = {Sun, 13 Nov 2022 17:52:57 +0100},
  biburl    = {https://dblp.org/rec/journals/jim/KumarS22.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Contributions

Thanks to [@phucdev](https://github.com/phucdev) for adding this dataset.