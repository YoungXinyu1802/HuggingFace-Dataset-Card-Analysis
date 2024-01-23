---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- de
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- other
task_ids:
- named-entity-recognition
paperswithcode_id: mobie
pretty_name: MobIE
tags:
- structure-prediction
---

# Dataset Card for "MobIE"

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

- **Homepage:** [https://github.com/dfki-nlp/mobie](https://github.com/dfki-nlp/mobie)
- **Repository:** [https://github.com/dfki-nlp/mobie](https://github.com/dfki-nlp/mobie)
- **Paper:** [https://aclanthology.org/2021.konvens-1.22/](https://aclanthology.org/2021.konvens-1.22/)
- **Point of Contact:** See [https://github.com/dfki-nlp/mobie](https://github.com/dfki-nlp/mobie) 
- **Size of downloaded dataset files:** 7.8 MB
- **Size of the generated dataset:** 1.9 MB
- **Total amount of disk used:** 9.7 MB

### Dataset Summary

This script is for loading the MobIE dataset from https://github.com/dfki-nlp/mobie. 

MobIE is a German-language dataset which is human-annotated with 20 coarse- and fine-grained entity types and entity linking information for geographically linkable entities. The dataset consists of 3,232 social media texts and traffic reports with 91K tokens, and contains 20.5K annotated entities, 13.1K of which are linked to a knowledge base. A subset of the dataset is human-annotated with seven mobility-related, n-ary relation types, while the remaining documents are annotated using a weakly-supervised labeling approach implemented with the Snorkel framework. The dataset combines annotations for NER, EL and RE, and thus can be used for joint and multi-task learning of these fundamental information extraction tasks.

This version of the dataset loader provides NER tags only. NER tags use the `BIO` tagging scheme. 

For more details see https://github.com/dfki-nlp/mobie and https://aclanthology.org/2021.konvens-1.22/.

### Supported Tasks and Leaderboards

- **Tasks:** Named Entity Recognition
- **Leaderboards:**

### Languages

German

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 7.8 MB
- **Size of the generated dataset:** 1.9 MB
- **Total amount of disk used:** 9.7 MB

An example of 'train' looks as follows.

```json
{ 
  'id': 'http://www.ndr.de/nachrichten/verkehr/index.html#2@2016-05-04T21:02:14.000+02:00',
  'tokens': ['Vorsicht', 'bitte', 'auf', 'der', 'A28', 'Leer', 'Richtung', 'Oldenburg', 'zwischen', 'Zwischenahner', 'Meer', 'und', 'Neuenkruge', 'liegen', 'Gegenstände', '!'], 
  'ner_tags': [0, 0, 0, 0, 19, 13, 0, 13, 0, 11, 12, 0, 11, 0, 0, 0]
}
```


### Data Fields

The data fields are the same among all splits.

- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels, with possible values including `O` (0), `B-date` (1), `I-date` (2), `B-disaster-type` (3), `I-disaster-type` (4), ...

### Data Splits

|           | Train  |  Dev  | Test |
| -----     | ------ | ----- | ---- |
| MobIE     | 4785 | 1082 | 1210 |

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

[CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/)

### Citation Information

```
@inproceedings{hennig-etal-2021-mobie,
    title = "{M}ob{IE}: A {G}erman Dataset for Named Entity Recognition, Entity Linking and Relation Extraction in the Mobility Domain",
    author = "Hennig, Leonhard  and
      Truong, Phuc Tran  and
      Gabryszak, Aleksandra",
    booktitle = "Proceedings of the 17th Conference on Natural Language Processing (KONVENS 2021)",
    month = "6--9 " # sep,
    year = "2021",
    address = {D{\"u}sseldorf, Germany},
    publisher = "KONVENS 2021 Organizers",
    url = "https://aclanthology.org/2021.konvens-1.22",
    pages = "223--227",
}
```


### Contributions
