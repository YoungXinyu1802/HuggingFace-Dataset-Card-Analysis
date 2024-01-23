---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- crowdsourced
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: SQuAD-shifts
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
paperswithcode_id: squad-shifts
dataset_info:
- config_name: new_wiki
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  splits:
  - name: test
    num_bytes: 7865203
    num_examples: 7938
  download_size: 16505623
  dataset_size: 7865203
- config_name: nyt
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  splits:
  - name: test
    num_bytes: 10792550
    num_examples: 10065
  download_size: 16505623
  dataset_size: 10792550
- config_name: reddit
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  splits:
  - name: test
    num_bytes: 9473946
    num_examples: 9803
  download_size: 16505623
  dataset_size: 9473946
- config_name: amazon
  features:
  - name: id
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: answers
    sequence:
    - name: text
      dtype: string
    - name: answer_start
      dtype: int32
  splits:
  - name: test
    num_bytes: 9445004
    num_examples: 9885
  download_size: 16505623
  dataset_size: 9445004
---

# Dataset Card for "squadshifts"

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

- **Homepage:** [https://modestyachts.github.io/squadshifts-website/index.html](https://modestyachts.github.io/squadshifts-website/index.html)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 62.96 MB
- **Size of the generated dataset:** 35.82 MB
- **Total amount of disk used:** 98.78 MB

### Dataset Summary

SquadShifts consists of four new test sets for the Stanford Question Answering Dataset (SQuAD) from four different domains: Wikipedia articles, New York \
Times articles, Reddit comments, and Amazon product reviews. Each dataset was generated using the same data generating pipeline, Amazon Mechanical Turk interface, and data cleaning code as the original SQuAD v1.1 dataset. The "new-wikipedia" dataset measures overfitting on the original SQuAD v1.1 dataset.  The "new-york-times", "reddit", and "amazon" datasets measure robustness to natural distribution shifts. We encourage SQuAD model developers to also evaluate their methods on these new datasets!

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### amazon

- **Size of downloaded dataset files:** 15.74 MB
- **Size of the generated dataset:** 9.00 MB
- **Total amount of disk used:** 24.74 MB

An example of 'test' looks as follows.
```
{
    "answers": {
        "answer_start": [25],
        "text": ["amazon"]
    },
    "context": "This is a paragraph from amazon.",
    "id": "090909",
    "question": "Where is this paragraph from?",
    "title": "amazon dummy data"
}
```

#### new_wiki

- **Size of downloaded dataset files:** 15.74 MB
- **Size of the generated dataset:** 7.50 MB
- **Total amount of disk used:** 23.24 MB

An example of 'test' looks as follows.
```
{
    "answers": {
        "answer_start": [25],
        "text": ["wikipedia"]
    },
    "context": "This is a paragraph from wikipedia.",
    "id": "090909",
    "question": "Where is this paragraph from?",
    "title": "new_wiki dummy data"
}
```

#### nyt

- **Size of downloaded dataset files:** 15.74 MB
- **Size of the generated dataset:** 10.29 MB
- **Total amount of disk used:** 26.03 MB

An example of 'test' looks as follows.
```
{
    "answers": {
        "answer_start": [25],
        "text": ["new york times"]
    },
    "context": "This is a paragraph from new york times.",
    "id": "090909",
    "question": "Where is this paragraph from?",
    "title": "nyt dummy data"
}
```

#### reddit

- **Size of downloaded dataset files:** 15.74 MB
- **Size of the generated dataset:** 9.03 MB
- **Total amount of disk used:** 24.77 MB

An example of 'test' looks as follows.
```
{
    "answers": {
        "answer_start": [25],
        "text": ["reddit"]
    },
    "context": "This is a paragraph from reddit.",
    "id": "090909",
    "question": "Where is this paragraph from?",
    "title": "reddit dummy data"
}
```

### Data Fields

The data fields are the same among all splits.

#### amazon
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

#### new_wiki
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

#### nyt
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

#### reddit
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.

### Data Splits

|  name  |test |
|--------|----:|
|amazon  | 9885|
|new_wiki| 7938|
|nyt     |10065|
|reddit  | 9803|

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

All the datasets are distributed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) license.

### Citation Information

```
@InProceedings{pmlr-v119-miller20a,
  title = {The Effect of Natural Distribution Shift on Question Answering Models},
  author = {Miller, John and Krauth, Karl and Recht, Benjamin and Schmidt, Ludwig},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning},
  pages = {6905--6916},
  year = {2020},
  editor = {III, Hal Daumé and Singh, Aarti},
  volume = {119},
  series = {Proceedings of Machine Learning Research},
  month = {13--18 Jul},
  publisher = {PMLR},
  pdf = {http://proceedings.mlr.press/v119/miller20a/miller20a.pdf},
  url = {https://proceedings.mlr.press/v119/miller20a.html},
}
```

### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@lewtun](https://github.com/lewtun), [@millerjohnp](https://github.com/millerjohnp), [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.