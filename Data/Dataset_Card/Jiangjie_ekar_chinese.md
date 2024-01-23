---
language:
- zh
license:
- afl-3.0
size_categories:
- 1K<n<2K
source_datasets:
- original
task_categories:
- question-answering
- text-generation
task_ids:
- analogical-qa
- explanation-generation
---

# Dataset Card for ekar_chinese

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

- **Homepage:** https://ekar-leaderboard.github.io
- **Paper:** [E-KAR: A Benchmark for Rationalizing Natural Language Analogical Reasoning](https://aclanthology.org/2022.findings-acl.311)
- **Leaderboard:** https://eval.ai/web/challenges/challenge-page/1671/overview
- **Point of Contact:** jjchen19@fudan.edu.cn

### Dataset Summary

***New!***(9/18/2022) E-KAR `v1.1` is officially released (at the `main` branch), **with a higher-quality English dataset!** In `v1.1`, we further improve the Chinese-to-English translation quality of the English E-KAR, with over 600 problems and over 1,000 explanations manually adjusted. You can still find previous version (as in the paper) in the `v1.0` branch in the repo. For more information please refer to https://ekar-leaderboard.github.io.

The ability to recognize analogies is fundamental to human cognition. Existing benchmarks to test word analogy do not reveal the underneath process of analogical reasoning of neural models. Holding the belief that models capable of reasoning should be right for the right reasons, we propose a first-of-its-kind Explainable Knowledge-intensive Analogical Reasoning benchmark (E-KAR). Our benchmark consists of 1,655 (in Chinese) and 1,251 (in English) problems sourced from the Civil Service Exams, which require intensive background knowledge to solve. More importantly, we design a free-text explanation scheme to explain whether an analogy should be drawn, and manually annotate them for each and every question and candidate answer. Empirical results suggest that this benchmark is very challenging for some state-of-the-art models for both explanation generation and analogical question answering tasks, which invites further research in this area.

### Supported Tasks and Leaderboards

- `analogical-qa`: The dataset can be used to train a model for analogical reasoning in the form of multiple-choice QA.
- `explanation-generation`: The dataset can be used to generate free-text explanations to rationalize analogical reasoning.

This dataset supports two task modes: EASY mode and HARD mode:
- `EASY mode`: where query explanation can be used as part of the input.
- `HARD mode`: no explanation is allowed as part of the input.

### Languages

This dataset is in Chinese, with its [English version](https://huggingface.co/datasets/Jiangjie/ekar_english).

## Dataset Structure

### Data Instances

```json
{
  "id": "982f17-en",
  "question": "plant:coal",
  "choices": {
    "label": [
      "A",
      "B",
      "C",
      "D"
    ],
    "text": [
      "white wine:aged vinegar",
      "starch:corn",
      "milk:yogurt",
      "pickled cabbage:cabbage"
    ]
  },
  "answerKey": "C",
  "explanation": [
    "\"plant\" is the raw material of \"coal\".",
    "both \"white wine\" and \"aged vinegar\" are brewed.",
    "\"starch\" is made of \"corn\", and the order of words is inconsistent with the query.",
    "\"yogurt\" is made from \"milk\".",
    "\"pickled cabbage\" is made of \"cabbage\", and the word order is inconsistent with the query."
  ],
  "relation": [
    [["plant", "coal", "R3.7"]],
    [["white wine", "aged vinegar", "R2.4"]],
    [["corn", "starch", "R3.7"]],
    [["milk", "yogurt", "R3.7"]],
    [["cabbage", "pickled cabbage", "R3.7"]]
  ]
}
```


### Data Fields

- id: a string identifier for each example.
- question: query terms.
- choices: candidate answer terms.
- answerKey: correct answer.
- explanation: explanations for query (1st) and candidate answers (2nd-5th).
- relation: annotated relations for terms in the query (1st) and candidate answers (2nd-5th).

### Data Splits

| name  |train|validation|test|
|:-----:|:---:|:--------:|:--:|
|default| 1155 | 165 | 335 |
|description|  |  | blinded |

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

The purpose of this dataset is to help develop analogical reasoning systems that are right for the right reasons.

### Discussion of Biases

This dataset is sourced and translated from the Civil Service Examinations of China. Therefore, it may contain information biased to Chinese culture.

### Other Known Limitations

1. The explanation annotation process in E-KAR (not the EG task) is mostly post-hoc and reflects only the result of reasoning. Humans solve the analogy problems in a trial-and-error manner, i.e., adjusting the abduced source structure and trying to find the most suited one for all candidate answers. Therefore, such explanations cannot offer supervision for intermediate reasoning.

2. E-KAR only presents one feasible explanation for each problem, whereas there may be several.


## Additional Information

### Dataset Curators

The dataset was initially created and curated by Jiangjie Chen (Fudan University, ByteDance), Rui Xu (Fudan University), Ziquan Fu (Brain Technologies, Inc.), Wei Shi (South China University of Technology), Xinbo Zhang (ByteDance), Changzhi Sun (ByteDance) and other colleagues at ByteDance and Fudan University.

### Licensing Information

[Needs More Information]

### Citation Information

```latex
@inproceedings{chen-etal-2022-e,
    title = "{E}-{KAR}: A Benchmark for Rationalizing Natural Language Analogical Reasoning",
    author = "Chen, Jiangjie  and
      Xu, Rui  and
      Fu, Ziquan  and
      Shi, Wei  and
      Li, Zhongqiao  and
      Zhang, Xinbo  and
      Sun, Changzhi  and
      Li, Lei  and
      Xiao, Yanghua  and
      Zhou, Hao",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-acl.311",
    pages = "3941--3955",
}
```

