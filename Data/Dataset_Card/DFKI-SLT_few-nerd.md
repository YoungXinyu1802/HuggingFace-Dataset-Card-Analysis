---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended|wikipedia
task_categories:
- other
task_ids:
- named-entity-recognition
paperswithcode_id: few-nerd
pretty_name: Few-NERD
tags:
- structure-prediction
---

# Dataset Card for "Few-NERD"

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

- **Homepage:** [https://ningding97.github.io/fewnerd/](https://ningding97.github.io/fewnerd/)
- **Repository:** [https://github.com/thunlp/Few-NERD](https://github.com/thunlp/Few-NERD)
- **Paper:** [https://aclanthology.org/2021.acl-long.248/](https://aclanthology.org/2021.acl-long.248/)
- **Point of Contact:** See [https://ningding97.github.io/fewnerd/](https://ningding97.github.io/fewnerd/) 

### Dataset Summary

This script is for loading the Few-NERD dataset from https://ningding97.github.io/fewnerd/. 

Few-NERD is a large-scale, fine-grained manually annotated named entity recognition dataset, which contains 8 coarse-grained types, 66 fine-grained types, 188,200 sentences, 491,711 entities, and 4,601,223 tokens. Three benchmark tasks are built, one is supervised (Few-NERD (SUP)) and the other two are few-shot (Few-NERD (INTRA) and Few-NERD (INTER)).

NER tags use the `IO` tagging scheme. The original data uses a 2-column CoNLL-style format, with empty lines to separate sentences. DOCSTART information is not provided since the sentences are randomly ordered.

For more details see https://ningding97.github.io/fewnerd/ and https://aclanthology.org/2021.acl-long.248/.

### Supported Tasks and Leaderboards

- **Tasks:** Named Entity Recognition, Few-shot NER
- **Leaderboards:**
  - https://ningding97.github.io/fewnerd/
  - named-entity-recognition:https://paperswithcode.com/sota/named-entity-recognition-on-few-nerd-sup
  - other-few-shot-ner:https://paperswithcode.com/sota/few-shot-ner-on-few-nerd-intra
  - other-few-shot-ner:https://paperswithcode.com/sota/few-shot-ner-on-few-nerd-inter


### Languages

English

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 
  - `super`: 14.6 MB
  - `intra`: 11.4 MB
  - `inter`: 11.5 MB

- **Size of the generated dataset:**
  - `super`: 116.9 MB
  - `intra`: 106.2 MB
  - `inter`: 106.2 MB

- **Total amount of disk used:** 366.8 MB


An example of 'train' looks as follows.

```json
{
    'id': '1', 
    'tokens': ['It', 'starred', 'Hicks', "'s", 'wife', ',', 'Ellaline', 'Terriss', 'and', 'Edmund', 'Payne', '.'], 
    'ner_tags': [0, 0, 7, 0, 0, 0, 7, 7, 0, 7, 7, 0], 
    'fine_ner_tags': [0, 0, 51, 0, 0, 0, 50, 50, 0, 50, 50, 0]
}
```



### Data Fields

The data fields are the same among all splits.

- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels, with possible values including `O` (0), `art` (1), `building` (2), `event` (3), `location` (4), `organization` (5), `other`(6), `person` (7), `product` (8)
- `fine_ner_tags`: a `list` of fine-grained  classification labels, with possible values including `O` (0), `art-broadcastprogram` (1), `art-film` (2), ...

### Data Splits

| Task      | Train  |  Dev  | Test |
| -----     | ------ | ----- | ---- |
| SUP       | 131767 | 18824 | 37648 |
| INTRA     | 99519  | 19358 | 44059 |
| INTER     | 130112 | 18817 | 14007 |

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
@inproceedings{ding-etal-2021-nerd,
    title = "Few-{NERD}: A Few-shot Named Entity Recognition Dataset",
    author = "Ding, Ning  and
      Xu, Guangwei  and
      Chen, Yulin  and
      Wang, Xiaobin  and
      Han, Xu  and
      Xie, Pengjun  and
      Zheng, Haitao  and
      Liu, Zhiyuan",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.248",
    doi = "10.18653/v1/2021.acl-long.248",
    pages = "3198--3213",
}
```


### Contributions
