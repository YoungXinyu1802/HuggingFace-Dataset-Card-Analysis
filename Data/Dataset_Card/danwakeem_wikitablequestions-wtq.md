---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: WikiTableQuestions-wtq
size_categories:
- 10K<n<100K
source_datasets:
- wikitablequestions
task_categories:
- question-answering
task_ids: []
tags:
- table-question-answering
---

# Dataset Card for WikiTableQuestions-wtq

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

- **Homepage:** [WikiTableQuestions homepage](https://nlp.stanford.edu/software/sempre/wikitable)
- **Repository:** [WikiTableQuestions repository](https://github.com/ppasupat/WikiTableQuestions)
- **Paper:** [Compositional Semantic Parsing on Semi-Structured Tables](https://arxiv.org/abs/1508.00305)
- **Leaderboard:** [WikiTableQuestions leaderboard on PaperWithCode](https://paperswithcode.com/dataset/wikitablequestions)
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The WikiTableQuestions-wtq dataset is a small-scale dataset for the task of question answering on semi-structured tables.

This data includes the `aggregation_label` and `answer_coordinates` to make it easy to train this model on any [TAPAS](https://huggingface.co/docs/transformers/model_doc/tapas#usage-finetuning) based modles.

### Supported Tasks and Leaderboards

question-answering, table-question-answering

### Languages

en

## Dataset Structure

### Data Instances

#### default

- **Size of downloaded dataset files:** 27.91 MB
- **Size of the generated dataset:** 45.68 MB
- **Total amount of disk used:** 73.60 MB

An example of 'validation' looks as follows:
```
{
  "id": "nt-0",
  "question": "What is the total average attendance at all USL First Division matches?",
  "answers": [
    "36755"
  ],
  "table": {
    "header": [
      "Year",
      "Division",
      "League",
      "Regular Season",
      "Playoffs",
      "Open Cup",
      "Avg. Attendance"
    ],
    "rows": [
      [
        "2001",
        "2",
        "USL A-League",
        "4th, Western",
        "Quarterfinals",
        "Did not qualify",
        "7,169"
      ],
      ...
    ],
    "name": "csv/204-csv/590.tsv"
  },
  "aggregation_label": "SUM",
  "answer_coordinates": [
    [
      4,
      6
    ],
    ...
  ]
}
```

### Data Fields

The data fields are the same among all splits.

#### default
- `id`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a `list` of `string` feature.
- `answers_coordinates`: a `list` of `int,int` tuples.
- `aggregation_label`: a `string` feature.
- `table`: a dictionary feature containing:
  - `header`: a `list` of `string` features.
  - `rows`: a `list` of `list` of `string` features:
  - `name`: a `string` feature.

### Data Splits

TBA

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

Panupong Pasupat and Percy Liang

### Licensing Information

Creative Commons Attribution Share Alike 4.0 International

### Citation Information

```
@inproceedings{pasupat-liang-2015-compositional,
    title = "Compositional Semantic Parsing on Semi-Structured Tables",
    author = "Pasupat, Panupong and Liang, Percy",
    booktitle = "Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = jul,
    year = "2015",
    address = "Beijing, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P15-1142",
    doi = "10.3115/v1/P15-1142",
    pages = "1470--1480",
}
```

### Contributions

Thanks to [@SivilTaram](https://github.com/SivilTaram) for adding this dataset.