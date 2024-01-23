---
annotations_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
task_categories:
- text-classification
task_ids: []
pretty_name: OpenQuestionType
---


# Dataset Card for OpenQuestionType

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

- **Homepage:** [https://shuyangcao.github.io/projects/ontology_open_ended_question/](https://shuyangcao.github.io/projects/ontology_open_ended_question/)
- **Repository:** [https://github.com/ShuyangCao/open-ended_question_ontology](https://github.com/ShuyangCao/open-ended_question_ontology)
- **Paper:** [https://aclanthology.org/2021.acl-long.502/](https://aclanthology.org/2021.acl-long.502/)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Question types annotated on open-ended questions.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

### Data Instances

An example looks as follows.
```
{
    "id": "123",
    "question": "A test question?",
    "annotator1": ["verification", None],
    "annotator2": ["concept", None],
    "resolve_type": "verification"
}
```

### Data Fields

- `id`: a `string` feature.
- `question`: a `string` feature.
- `annotator1`: a sequence feature containing two elements. The first one is the most confident label by the first annotator and the second one is the second-most confident label by the first annotator.
- `annotator2`: a sequence feature containing two elements. The first one is the most confident label by the second annotator and the second one is the second-most confident label by the second annotator.
- `resolve_type`: a `string` feature which is the final label after resolving disagreement.

### Data Splits

- train: 3716
- valid: 580
- test: 660

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

Yahoo Answer and Reddit users.

### Personal and Sensitive Information

None.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

CC BY 4.0

### Citation Information

```
@inproceedings{cao-wang-2021-controllable,
    title = "Controllable Open-ended Question Generation with A New Question Type Ontology",
    author = "Cao, Shuyang  and
      Wang, Lu",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.502",
    doi = "10.18653/v1/2021.acl-long.502",
    pages = "6424--6439",
    abstract = "We investigate the less-explored task of generating open-ended questions that are typically answered by multiple sentences. We first define a new question type ontology which differentiates the nuanced nature of questions better than widely used question words. A new dataset with 4,959 questions is labeled based on the new ontology. We then propose a novel question type-aware question generation framework, augmented by a semantic graph representation, to jointly predict question focuses and produce the question. Based on this framework, we further use both exemplars and automatically generated templates to improve controllability and diversity. Experiments on two newly collected large-scale datasets show that our model improves question quality over competitive comparisons based on automatic metrics. Human judges also rate our model outputs highly in answerability, coverage of scope, and overall quality. Finally, our model variants with templates can produce questions with enhanced controllability and diversity.",
}
```
