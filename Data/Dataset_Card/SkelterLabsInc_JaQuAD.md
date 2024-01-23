---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
- found
language:
- ja
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: "JaQuAD: Japanese Question Answering Dataset"
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for JaQuAD

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splitting](#data-splitting)
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
  - [Acknowledgements](#acknowledgements)

## Dataset Description

- **Repository:** https://github.com/SkelterLabsInc/JaQuAD
- **Paper:** [JaQuAD: Japanese Question Answering Dataset for Machine Reading Comprehension]()
- **Point of Contact:** [jaquad@skelterlabs.com](jaquad@skelterlabs.com)
- **Size of dataset files:** 24.6 MB
- **Size of the generated dataset:** 48.6 MB
- **Total amount of disk used:** 73.2 MB

### Dataset Summary

Japanese Question Answering Dataset (JaQuAD), released in 2022, is a
human-annotated dataset created for Japanese Machine Reading Comprehension.
JaQuAD is developed to provide a SQuAD-like QA dataset in Japanese.
JaQuAD contains 39,696 question-answer pairs.
Questions and answers are manually curated by human annotators.
Contexts are collected from Japanese Wikipedia articles.
Fine-tuning [BERT-Japanese](https://huggingface.co/cl-tohoku/bert-base-japanese)
on JaQuAD achieves 78.92% for an F1 score and 63.38% for an exact match.

### Supported Tasks

- `extractive-qa`: This dataset is intended to be used for `extractive-qa`.

### Languages

Japanese (`ja`)

## Dataset Structure

### Data Instances

- **Size of dataset files:** 24.6 MB
- **Size of the generated dataset:** 48.6 MB
- **Total amount of disk used:** 73.2 MB

An example of 'validation':
```python
{
    "id": "de-001-00-000",
    "title": "イタセンパラ",
    "context": "イタセンパラ(板鮮腹、Acheilognathuslongipinnis)は、コイ科のタナゴ亜科タナゴ属に分類される淡水>魚の一種。\n別名はビワタナゴ(琵琶鱮、琵琶鰱)。",
    "question": "ビワタナゴの正式名称は何?",
    "question_type": "Multiple sentence reasoning",
    "answers": {
        "text": "イタセンパラ",
        "answer_start": 0,
        "answer_type": "Object",
    },
},
```

### Data Fields

- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `question_type`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.
  - `answer_type`: a `string` feature.

### Data Splitting

JaQuAD consists of three sets, `train`, `validation`, and `test`. They were
created from disjoint sets of Wikipedia articles. The `test` set is not publicly
released yet. The following table shows statistics for each set.

Set | Number of Articles | Number of Contexts | Number of Questions
--------------|--------------------|--------------------|--------------------
Train | 691 | 9713 | 31748
Validation | 101 | 1431 | 3939
Test | 109 | 1479 | 4009


## Dataset Creation

### Curation Rationale

The JaQuAD dataset was created by [Skelter Labs](https://skelterlabs.com/) to
provide a SQuAD-like QA dataset in Japanese. Questions are original and based
on Japanese Wikipedia articles.

### Source Data

The articles used for the contexts are from [Japanese Wikipedia](https://ja.wikipedia.org/).
88.7% of articles are from the curated list of Japanese high-quality Wikipedia
articles, e.g., [featured articles](https://ja.wikipedia.org/wiki/Wikipedia:%E8%89%AF%E8%B3%AA%E3%81%AA%E8%A8%98%E4%BA%8B)
and [good articles](https://ja.wikipedia.org/wiki/Wikipedia:%E7%A7%80%E9%80%B8%E3%81%AA%E8%A8%98%E4%BA%8B).

### Annotations

Wikipedia articles were scrapped and divided into one more multiple paragraphs
as contexts. Annotations (questions and answer spans) are written by fluent
Japanese speakers, including natives and non-natives. Annotators were given a
context and asked to generate non-trivial questions about information in the
context.

### Personal and Sensitive Information

No personal or sensitive information is included in this dataset. Dataset
annotators has been manually verified it.

## Considerations for Using the Data

Users should consider that the articles are sampled from Wikipedia articles but
not representative of all Wikipedia articles.

### Social Impact of Dataset

The social biases of this dataset have not yet been investigated.

### Discussion of Biases

The social biases of this dataset have not yet been investigated. Articles and
questions have been selected for quality and diversity.

### Other Known Limitations

The JaQuAD dataset has limitations as follows:
- Most of them are short answers.
- Assume that a question is answerable using the corresponding context.

This dataset is incomplete yet. If you find any errors in JaQuAD, please contact
us.

## Additional Information

### Dataset Curators

Skelter Labs: [https://skelterlabs.com/](https://skelterlabs.com/)

### Licensing Information

The JaQuAD dataset is licensed under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

### Citation Information

```bibtex
@misc{so2022jaquad,
      title={{JaQuAD: Japanese Question Answering Dataset for Machine Reading Comprehension}},
      author={ByungHoon So and Kyuhong Byun and Kyungwon Kang and Seongjin Cho},
      year={2022},
      eprint={2202.01764},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Acknowledgements

This work was supported by [TPU Research Cloud (TRC) program](https://sites.research.google/trc/).
For training models, we used cloud TPUs provided by TRC. We also thank
annotators who generated JaQuAD.

