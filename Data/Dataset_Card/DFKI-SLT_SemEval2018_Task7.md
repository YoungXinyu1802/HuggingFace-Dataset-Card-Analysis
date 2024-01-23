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
paperswithcode_id: acronym-identification
pretty_name: >-
  Semeval2018Task7 is a dataset that describes the Semantic Relation Extraction
  and Classification in Scientific Papers
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- Relation Classification
- Relation extraction
- Scientific papers
- Research papers
task_categories:
- text-classification
task_ids:
- entity-linking-classification
train-eval-index:
- col_mapping:
    labels: tags
    tokens: tokens
  config: default
  splits:
    eval_split: test
  task: text-classification
  task_id: entity_extraction
---
# Dataset Card for SemEval2018Task7

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

- **Homepage:** [https://lipn.univ-paris13.fr/~gabor/semeval2018task7/](https://lipn.univ-paris13.fr/~gabor/semeval2018task7/)
- **Repository:** [https://github.com/gkata/SemEval2018Task7/tree/testing](https://github.com/gkata/SemEval2018Task7/tree/testing)
- **Paper:** [SemEval-2018 Task 7: Semantic Relation Extraction and Classification in Scientific Papers](https://aclanthology.org/S18-1111/)
- **Leaderboard:** [https://competitions.codalab.org/competitions/17422#learn_the_details-overview](https://competitions.codalab.org/competitions/17422#learn_the_details-overview)
- **Size of downloaded dataset files:** 1.93 MB

### Dataset Summary

Semeval2018Task7 is a dataset that describes the Semantic Relation Extraction and Classification in Scientific Papers.
The challenge focuses on domain-specific semantic relations and includes three different subtasks. The subtasks were designed so as to compare and quantify the effect of different pre-processing steps on the relation classification results. We expect the task to be relevant for a broad range of researchers working on extracting specialized knowledge from domain corpora, for example but not limited to scientific or bio-medical information extraction. The task attracted a total of 32 participants, with 158 submissions across different scenarios.

The three subtasks are:

- Subtask 1.1: Relation classification on clean data
  - In the training data, semantic relations are manually annotated between entities. 
  - In the test data, only entity annotations and unlabeled relation instances are given.
  - Given a scientific publication, The task is to predict the semantic relation between the entities.
  
- Subtask 1.2: Relation classification on noisy data
  - Entity occurrences are automatically annotated in both the training and the test data.
  - The task is to predict the semantic
relation between the entities. 
  
- Subtask 2: Metrics for the extraction and classification scenario 
  - Evaluation of relation extraction
  - Evaluation of relation classification
  
The Relations types are USAGE, RESULT, MODEL, PART_WHOLE, TOPIC, COMPARISION.

The following example shows a text snippet with the information provided in the test data:
    Korean, a \<entity id=”H01-1041.10”>verb final language\</entity>with\<entity id=”H01-1041.11”>overt case markers\</entity>(...)
  - A relation instance is identified by the unique identifier of the entities in the pair, e.g.(H01-1041.10, H01-1041.11)
  - The information to be predicted is the relation class label: MODEL-FEATURE(H01-1041.10, H01-1041.11).
For details, see the paper https://aclanthology.org/S18-1111/. 

### Supported Tasks and Leaderboards

- **Tasks:** Relation extraction and classification in scientific papers
- **Leaderboards:** [https://competitions.codalab.org/competitions/17422#learn_the_details-overview](https://competitions.codalab.org/competitions/17422#learn_the_details-overview)

### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

#### subtask_1.1
- **Size of downloaded dataset files:** 714 KB
  
An example of 'train' looks as follows:
```json
{
  "id": "H01-1041", 
  "title": "'Interlingua-Based Broad-Coverage Korean-to-English Translation in CCLING'",
  "abstract": 'At MIT Lincoln Laboratory, we have been developing a Korean-to-English machine translation system CCLINC (Common Coalition Language System at Lincoln Laboratory) . The CCLINC Korean-to-English translation system consists of two core modules , language understanding and generation modules mediated by a language neutral meaning representation called a semantic frame . The key features of the system include: (i) Robust efficient parsing of Korean (a verb final language with overt case markers , relatively free word order , and frequent omissions of arguments ). (ii) High quality translation via word sense disambiguation and accurate word order generation of the target language . (iii) Rapid system development and porting to new domains via knowledge-based automated acquisition of grammars . Having been trained on Korean newspaper articles on missiles and chemical biological warfare, the system produces the translation output sufficient for content understanding of the original document.
  "entities": [{'id': 'H01-1041.1', 'char_start': 54, 'char_end': 97},
  {'id': 'H01-1041.2', 'char_start': 99, 'char_end': 161},
  {'id': 'H01-1041.3', 'char_start': 169, 'char_end': 211},
  {'id': 'H01-1041.4', 'char_start': 229, 'char_end': 240},
  {'id': 'H01-1041.5', 'char_start': 244, 'char_end': 288},
  {'id': 'H01-1041.6', 'char_start': 304, 'char_end': 342},
  {'id': 'H01-1041.7', 'char_start': 353, 'char_end': 366},
  {'id': 'H01-1041.8', 'char_start': 431, 'char_end': 437},
  {'id': 'H01-1041.9', 'char_start': 442, 'char_end': 447},
  {'id': 'H01-1041.10', 'char_start': 452, 'char_end': 470},
  {'id': 'H01-1041.11', 'char_start': 477, 'char_end': 494},
  {'id': 'H01-1041.12', 'char_start': 509, 'char_end': 523},
  {'id': 'H01-1041.13', 'char_start': 553, 'char_end': 561},
  {'id': 'H01-1041.14', 'char_start': 584, 'char_end': 594},
  {'id': 'H01-1041.15', 'char_start': 600, 'char_end': 624},
  {'id': 'H01-1041.16', 'char_start': 639, 'char_end': 659},
  {'id': 'H01-1041.17', 'char_start': 668, 'char_end': 682},
  {'id': 'H01-1041.18', 'char_start': 692, 'char_end': 715},
  {'id': 'H01-1041.19', 'char_start': 736, 'char_end': 742},
  {'id': 'H01-1041.20', 'char_start': 748, 'char_end': 796},
  {'id': 'H01-1041.21', 'char_start': 823, 'char_end': 847},
  {'id': 'H01-1041.22', 'char_start': 918, 'char_end': 935},
  {'id': 'H01-1041.23', 'char_start': 981, 'char_end': 997}],
}
  "relations": [{'label': 3, 'arg1': 'H01-1041.3', 'arg2': 'H01-1041.4', 'reverse': True},
  {'label': 0, 'arg1': 'H01-1041.8', 'arg2': 'H01-1041.9', 'reverse': False},
  {'label': 2, 'arg1': 'H01-1041.10', 'arg2': 'H01-1041.11', 'reverse': True},
  {'label': 0, 'arg1': 'H01-1041.14', 'arg2': 'H01-1041.15', 'reverse': True}]

```
#### Subtask_1.2
- **Size of downloaded dataset files:** 1.00 MB
  
An example of 'train' looks as follows:
```json
{'id': 'L08-1450',
 'title': '\nA LAF/GrAF based Encoding Scheme for underspecified Representations of syntactic Annotations.\n',
 'abstract': 'Data models and encoding formats for syntactically annotated text corpora need to deal with syntactic ambiguity; underspecified representations are particularly well suited for the representation of ambiguousdata because they allow for high informational efficiency. We discuss the issue of being informationally efficient, and the trade-off between efficient encoding of linguistic annotations and complete documentation of linguistic analyses. The main topic of this article is adata model and an encoding scheme based on LAF/GrAF ( Ide and  Romary, 2006 ; Ide and  Suderman, 2007 ) which provides a flexible framework for encoding underspecified representations. We show how a set of dependency structures and a set of TiGer graphs ( Brants et al., 2002 ) representing the readings of an ambiguous sentence can be encoded, and we discuss basic issues in querying corpora which are encoded using the framework presented here.\n',
 'entities': [{'id': 'L08-1450.4', 'char_start': 0, 'char_end': 3},
  {'id': 'L08-1450.5', 'char_start': 5, 'char_end': 10},
  {'id': 'L08-1450.6', 'char_start': 25, 'char_end': 31},
  {'id': 'L08-1450.7', 'char_start': 61, 'char_end': 64},
  {'id': 'L08-1450.8', 'char_start': 66, 'char_end': 72},
  {'id': 'L08-1450.9', 'char_start': 82, 'char_end': 85},
  {'id': 'L08-1450.10', 'char_start': 92, 'char_end': 100},
  {'id': 'L08-1450.11', 'char_start': 102, 'char_end': 110},
  {'id': 'L08-1450.12', 'char_start': 128, 'char_end': 142},
  {'id': 'L08-1450.13', 'char_start': 181, 'char_end': 194},
  {'id': 'L08-1450.14', 'char_start': 208, 'char_end': 211},
  {'id': 'L08-1450.15', 'char_start': 255, 'char_end': 264},
  {'id': 'L08-1450.16', 'char_start': 282, 'char_end': 286},
  {'id': 'L08-1450.17', 'char_start': 408, 'char_end': 420},
  {'id': 'L08-1450.18', 'char_start': 425, 'char_end': 443},
  {'id': 'L08-1450.19', 'char_start': 450, 'char_end': 453},
  {'id': 'L08-1450.20', 'char_start': 455, 'char_end': 459},
  {'id': 'L08-1450.21', 'char_start': 481, 'char_end': 484},
  {'id': 'L08-1450.22', 'char_start': 486, 'char_end': 490},
  {'id': 'L08-1450.23', 'char_start': 508, 'char_end': 513},
  {'id': 'L08-1450.24', 'char_start': 515, 'char_end': 519},
  {'id': 'L08-1450.25', 'char_start': 535, 'char_end': 537},
  {'id': 'L08-1450.26', 'char_start': 559, 'char_end': 561},
  {'id': 'L08-1450.27', 'char_start': 591, 'char_end': 598},
  {'id': 'L08-1450.28', 'char_start': 611, 'char_end': 619},
  {'id': 'L08-1450.29', 'char_start': 649, 'char_end': 663},
  {'id': 'L08-1450.30', 'char_start': 687, 'char_end': 707},
  {'id': 'L08-1450.31', 'char_start': 722, 'char_end': 726},
  {'id': 'L08-1450.32', 'char_start': 801, 'char_end': 808},
  {'id': 'L08-1450.33', 'char_start': 841, 'char_end': 845},
  {'id': 'L08-1450.34', 'char_start': 847, 'char_end': 852},
  {'id': 'L08-1450.35', 'char_start': 857, 'char_end': 864},
  {'id': 'L08-1450.36', 'char_start': 866, 'char_end': 872},
  {'id': 'L08-1450.37', 'char_start': 902, 'char_end': 910},
  {'id': 'L08-1450.1', 'char_start': 12, 'char_end': 16},
  {'id': 'L08-1450.2', 'char_start': 27, 'char_end': 32},
  {'id': 'L08-1450.3', 'char_start': 72, 'char_end': 80}],
 'relations': [{'label': 1,
   'arg1': 'L08-1450.12',
   'arg2': 'L08-1450.13',
   'reverse': False},
  {'label': 5, 'arg1': 'L08-1450.17', 'arg2': 'L08-1450.18', 'reverse': False},
  {'label': 1, 'arg1': 'L08-1450.28', 'arg2': 'L08-1450.29', 'reverse': False},
  {'label': 3, 'arg1': 'L08-1450.30', 'arg2': 'L08-1450.32', 'reverse': False},
  {'label': 3, 'arg1': 'L08-1450.34', 'arg2': 'L08-1450.35', 'reverse': False},
  {'label': 3, 'arg1': 'L08-1450.36', 'arg2': 'L08-1450.37', 'reverse': True}]}
[ ]

```


### Data Fields

#### subtask_1_1
- `id`: the instance id of this abstract, a `string` feature.
- `title`: the title of this abstract, a `string` feature
- `abstract`: the abstract from the scientific papers, a `string` feature
- `entities`: the entity id's for the key phrases, a `list` of entity id's.
    - `id`: the instance id of this sentence, a `string` feature.
    - `char_start`: the 0-based index of the entity starting, an `ìnt` feature.
    - `char_end`: the 0-based index of the entity ending, an `ìnt` feature.
- `relations`: the list of relations of this sentence marking the relation between the key phrases, a `list` of classification labels.
    - `label`: the list of relations between the key phrases, a `list` of classification labels.
    - `arg1`: the entity id of this key phrase, a `string` feature.
    - `arg2`: the entity id of the related key phrase, a `string` feature.
    - `reverse`: the reverse is `True` only if reverse is possible otherwise `False`, a `bool` feature.

```python
RELATIONS
{"":0,"USAGE": 1, "RESULT": 2, "MODEL-FEATURE": 3, "PART_WHOLE": 4, "TOPIC": 5, "COMPARE": 6}
```

#### subtask_1_2
- `id`: the instance id of this abstract, a `string` feature.
- `title`: the title of this abstract, a `string` feature
- `abstract`: the abstract from the scientific papers, a `string` feature
- `entities`: the entity id's for the key phrases, a `list` of entity id's.
    - `id`: the instance id of this sentence, a `string` feature.
    - `char_start`: the 0-based index of the entity starting, an `ìnt` feature.
    - `char_end`: the 0-based index of the entity ending, an `ìnt` feature.
- `relations`: the list of relations of this sentence marking the relation between the key phrases, a `list` of classification labels.
    - `label`: the list of relations between the key phrases, a `list` of classification labels.
    - `arg1`: the entity id of this key phrase, a `string` feature.
    - `arg2`: the entity id of the related key phrase, a `string` feature.
    - `reverse`: the reverse is `True` only if reverse is possible otherwise `False`, a `bool` feature.

```python
RELATIONS
{"":0,"USAGE": 1, "RESULT": 2, "MODEL-FEATURE": 3, "PART_WHOLE": 4, "TOPIC": 5, "COMPARE": 6}
```


### Data Splits

|             |           | Train| Test |
|-------------|-----------|------|------|
| subtask_1_1 | text      | 2807 | 3326 |
|             | relations | 1228 | 1248 |
| subtask_1_2 | text      | 1196 | 1193 |
|             | relations |  335 |  355 |

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
@inproceedings{gabor-etal-2018-semeval,
    title = "{S}em{E}val-2018 Task 7: Semantic Relation Extraction and Classification in Scientific Papers",
    author = {G{\'a}bor, Kata  and
      Buscaldi, Davide  and
      Schumann, Anne-Kathrin  and
      QasemiZadeh, Behrang  and
      Zargayouna, Ha{\"\i}fa  and
      Charnois, Thierry},
    booktitle = "Proceedings of the 12th International Workshop on Semantic Evaluation",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/S18-1111",
    doi = "10.18653/v1/S18-1111",
    pages = "679--688",
    abstract = "This paper describes the first task on semantic relation extraction and classification in scientific paper abstracts at SemEval 2018. The challenge focuses on domain-specific semantic relations and includes three different subtasks. The subtasks were designed so as to compare and quantify the effect of different pre-processing steps on the relation classification results. We expect the task to be relevant for a broad range of researchers working on extracting specialized knowledge from domain corpora, for example but not limited to scientific or bio-medical information extraction. The task attracted a total of 32 participants, with 158 submissions across different scenarios.",
}
```
### Contributions

Thanks to [@basvoju](https://github.com/basvoju) for adding this dataset.