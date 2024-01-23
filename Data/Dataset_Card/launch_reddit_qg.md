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
pretty_name: RedditQG
---


# Dataset Card for RedditQG

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

This dataset contains answer-question pairs from QA communities of Reddit.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

English

## Dataset Structure

### Data Instances

An example looks as follows.
```
{
    "id": "askscience/123",
    "qid": "2323",
    "answer": "A test answer.",
    "question": "A test question?",
    "score": 20
}
```

### Data Fields

- `id`: a `string` feature.
- `qid`: a `string` feature. There could be multiple answers to the same question.
- `answer`: a `string` feature.
- `question`: a `string` feature.
- `score`: an `int` feature which is the value of `upvotes - downvotes`.

### Data Splits

- train: 647763
- valid: 36023
- test: 36202

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

Reddit users.

### Personal and Sensitive Information

Samples with abusive words are discarded, but there could be samples containing personal information.

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
