---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
- machine-generated
language:
- ar
- de
- en
- es
- fr
- hi
- it
- ja
- nl
- pl
- pt
- ru
- sw
- ur
- vi
- zh
license:
- mit
multilinguality:
- multilingual
pretty_name: X-CSR
size_categories:
- 1K<n<10K
source_datasets:
- extended|codah
- extended|commonsense_qa
task_categories:
- question-answering
task_ids:
- multiple-choice-qa
dataset_info:
- config_name: X-CSQA-en
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 215919
    num_examples: 1074
  - name: validation
    num_bytes: 205361
    num_examples: 1000
  download_size: 7519903
  dataset_size: 421280
- config_name: X-CSQA-zh
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 197746
    num_examples: 1074
  - name: validation
    num_bytes: 188555
    num_examples: 1000
  download_size: 7519903
  dataset_size: 386301
- config_name: X-CSQA-de
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 234472
    num_examples: 1074
  - name: validation
    num_bytes: 223122
    num_examples: 1000
  download_size: 7519903
  dataset_size: 457594
- config_name: X-CSQA-es
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 237119
    num_examples: 1074
  - name: validation
    num_bytes: 224779
    num_examples: 1000
  download_size: 7519903
  dataset_size: 461898
- config_name: X-CSQA-fr
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 244254
    num_examples: 1074
  - name: validation
    num_bytes: 231678
    num_examples: 1000
  download_size: 7519903
  dataset_size: 475932
- config_name: X-CSQA-it
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 232906
    num_examples: 1074
  - name: validation
    num_bytes: 221184
    num_examples: 1000
  download_size: 7519903
  dataset_size: 454090
- config_name: X-CSQA-jap
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 251148
    num_examples: 1074
  - name: validation
    num_bytes: 240686
    num_examples: 1000
  download_size: 7519903
  dataset_size: 491834
- config_name: X-CSQA-nl
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 227251
    num_examples: 1074
  - name: validation
    num_bytes: 216476
    num_examples: 1000
  download_size: 7519903
  dataset_size: 443727
- config_name: X-CSQA-pl
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 231781
    num_examples: 1074
  - name: validation
    num_bytes: 220096
    num_examples: 1000
  download_size: 7519903
  dataset_size: 451877
- config_name: X-CSQA-pt
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 235771
    num_examples: 1074
  - name: validation
    num_bytes: 223067
    num_examples: 1000
  download_size: 7519903
  dataset_size: 458838
- config_name: X-CSQA-ru
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 342051
    num_examples: 1074
  - name: validation
    num_bytes: 324006
    num_examples: 1000
  download_size: 7519903
  dataset_size: 666057
- config_name: X-CSQA-ar
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 288947
    num_examples: 1074
  - name: validation
    num_bytes: 273862
    num_examples: 1000
  download_size: 7519903
  dataset_size: 562809
- config_name: X-CSQA-vi
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 265512
    num_examples: 1074
  - name: validation
    num_bytes: 253784
    num_examples: 1000
  download_size: 7519903
  dataset_size: 519296
- config_name: X-CSQA-hi
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 415313
    num_examples: 1074
  - name: validation
    num_bytes: 396600
    num_examples: 1000
  download_size: 7519903
  dataset_size: 811913
- config_name: X-CSQA-sw
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 222517
    num_examples: 1074
  - name: validation
    num_bytes: 211708
    num_examples: 1000
  download_size: 7519903
  dataset_size: 434225
- config_name: X-CSQA-ur
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 306431
    num_examples: 1074
  - name: validation
    num_bytes: 292283
    num_examples: 1000
  download_size: 7519903
  dataset_size: 598714
- config_name: X-CODAH-en
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 417286
    num_examples: 1000
  - name: validation
    num_bytes: 121923
    num_examples: 300
  download_size: 7519903
  dataset_size: 539209
- config_name: X-CODAH-zh
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 394946
    num_examples: 1000
  - name: validation
    num_bytes: 115137
    num_examples: 300
  download_size: 7519903
  dataset_size: 510083
- config_name: X-CODAH-de
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 476373
    num_examples: 1000
  - name: validation
    num_bytes: 138876
    num_examples: 300
  download_size: 7519903
  dataset_size: 615249
- config_name: X-CODAH-es
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 451240
    num_examples: 1000
  - name: validation
    num_bytes: 130790
    num_examples: 300
  download_size: 7519903
  dataset_size: 582030
- config_name: X-CODAH-fr
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 477811
    num_examples: 1000
  - name: validation
    num_bytes: 138001
    num_examples: 300
  download_size: 7519903
  dataset_size: 615812
- config_name: X-CODAH-it
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 457341
    num_examples: 1000
  - name: validation
    num_bytes: 133616
    num_examples: 300
  download_size: 7519903
  dataset_size: 590957
- config_name: X-CODAH-jap
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 538701
    num_examples: 1000
  - name: validation
    num_bytes: 157504
    num_examples: 300
  download_size: 7519903
  dataset_size: 696205
- config_name: X-CODAH-nl
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 449014
    num_examples: 1000
  - name: validation
    num_bytes: 130130
    num_examples: 300
  download_size: 7519903
  dataset_size: 579144
- config_name: X-CODAH-pl
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 438824
    num_examples: 1000
  - name: validation
    num_bytes: 127862
    num_examples: 300
  download_size: 7519903
  dataset_size: 566686
- config_name: X-CODAH-pt
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 455869
    num_examples: 1000
  - name: validation
    num_bytes: 132045
    num_examples: 300
  download_size: 7519903
  dataset_size: 587914
- config_name: X-CODAH-ru
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 674853
    num_examples: 1000
  - name: validation
    num_bytes: 193825
    num_examples: 300
  download_size: 7519903
  dataset_size: 868678
- config_name: X-CODAH-ar
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 568312
    num_examples: 1000
  - name: validation
    num_bytes: 165134
    num_examples: 300
  download_size: 7519903
  dataset_size: 733446
- config_name: X-CODAH-vi
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 543375
    num_examples: 1000
  - name: validation
    num_bytes: 157000
    num_examples: 300
  download_size: 7519903
  dataset_size: 700375
- config_name: X-CODAH-hi
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 974019
    num_examples: 1000
  - name: validation
    num_bytes: 283116
    num_examples: 300
  download_size: 7519903
  dataset_size: 1257135
- config_name: X-CODAH-sw
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 423707
    num_examples: 1000
  - name: validation
    num_bytes: 124882
    num_examples: 300
  download_size: 7519903
  dataset_size: 548589
- config_name: X-CODAH-ur
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: question_tag
    dtype: string
  - name: question
    struct:
    - name: stem
      dtype: string
    - name: choices
      sequence:
      - name: label
        dtype: string
      - name: text
        dtype: string
  - name: answerKey
    dtype: string
  splits:
  - name: test
    num_bytes: 687409
    num_examples: 1000
  - name: validation
    num_bytes: 199849
    num_examples: 300
  download_size: 7519903
  dataset_size: 887258
---

# Dataset Card for X-CSR

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

- **Homepage:** https://inklab.usc.edu//XCSR/
- **Repository:** https://github.com/INK-USC/XCSR
- **Paper:** https://arxiv.org/abs/2106.06937
- **Leaderboard:** https://inklab.usc.edu//XCSR/leaderboard
- **Point of Contact:** https://yuchenlin.xyz/

### Dataset Summary

To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. Specifically, we automatically translate the original CSQA and CODAH datasets, which only have English versions, to 15 other languages, forming development and test sets for studying X-CSR. As our goal is to evaluate different ML-LMs in a unified evaluation protocol for X-CSR, we argue that such translated examples, although might contain noise, can serve as a starting benchmark for us to obtain meaningful analysis, before more human-translated datasets will be available in the future.


### Supported Tasks and Leaderboards

https://inklab.usc.edu//XCSR/leaderboard

### Languages

The total 16 languages for X-CSR: {en, zh, de, es, fr, it, jap, nl, pl, pt, ru, ar, vi, hi, sw, ur}.


## Dataset Structure

### Data Instances

An example of the X-CSQA dataset:
```
{
  "id": "be1920f7ba5454ad",  # an id shared by all languages
  "lang": "en", # one of the 16 language codes.
  "question": { 
    "stem": "What will happen to your knowledge with more learning?",   # question text
    "choices": [
      {"label": "A",  "text": "headaches" },
      {"label": "B",  "text": "bigger brain" },
      {"label": "C",  "text": "education" },
      {"label": "D",  "text": "growth" },
      {"label": "E",  "text": "knowing more" }
    ] },
  "answerKey": "D"    # hidden for test data.
}
```

An example of the X-CODAH dataset:
```
{
  "id": "b8eeef4a823fcd4b",   # an id shared by all languages
  "lang": "en", # one of the 16 language codes.
  "question_tag": "o",  # one of 6 question types
  "question": {
    "stem": " ", # always a blank as a dummy question
    "choices": [
      {"label": "A",
        "text": "Jennifer loves her school very much, she plans to drop every courses."},
      {"label": "B",
        "text": "Jennifer loves her school very much, she is never absent even when she's sick."},
      {"label": "C",
        "text": "Jennifer loves her school very much, she wants to get a part-time job."},
      {"label": "D",
        "text": "Jennifer loves her school very much, she quits school happily."}
    ]
  },
  "answerKey": "B"  # hidden for test data.
}
```

### Data Fields

  - id: an id shared by all languages
  - lang: one of the 16 language codes.
  - question_tag: one of 6 question types
  - stem: always a blank as a dummy question
  - choices: a list of answers, each answer has: 
    - label: a string answer identifier for each answer
    - text: the answer text

### Data Splits

- X-CSQA: There are 8,888 examples for training in English, 1,000 for development in each language, and 1,074 examples for testing in each language.
- X-CODAH: There are 8,476 examples for training in English, 300 for development in each language, and 1,000 examples for testing in each language. 

## Dataset Creation

### Curation Rationale

To evaluate multi-lingual language models (ML-LMs) for commonsense reasoning in a cross-lingual zero-shot transfer setting (X-CSR), i.e., training in English and test in other languages, we create two benchmark datasets, namely X-CSQA and X-CODAH. 

The details of the dataset construction, especially the translation procedures, can be found in section A of the appendix of the [paper](https://inklab.usc.edu//XCSR/XCSR_paper.pdf).

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

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

```
# X-CSR
@inproceedings{lin-etal-2021-common,
    title = "Common Sense Beyond {E}nglish: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning",
    author = "Lin, Bill Yuchen  and
      Lee, Seyeon  and
      Qiao, Xiaoyang  and
      Ren, Xiang",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.102",
    doi = "10.18653/v1/2021.acl-long.102",
    pages = "1274--1287",
    abstract = "Commonsense reasoning research has so far been limited to English. We aim to evaluate and improve popular multilingual language models (ML-LMs) to help advance commonsense reasoning (CSR) beyond English. We collect the Mickey corpus, consisting of 561k sentences in 11 different languages, which can be used for analyzing and improving ML-LMs. We propose Mickey Probe, a language-general probing task for fairly evaluating the common sense of popular ML-LMs across different languages. In addition, we also create two new datasets, X-CSQA and X-CODAH, by translating their English versions to 14 other languages, so that we can evaluate popular ML-LMs for cross-lingual commonsense reasoning. To improve the performance beyond English, we propose a simple yet effective method {---} multilingual contrastive pretraining (MCP). It significantly enhances sentence representations, yielding a large performance gain on both benchmarks (e.g., +2.7{\%} accuracy for X-CSQA over XLM-R{\_}L).",
}

# CSQA
@inproceedings{Talmor2019commonsenseqaaq,
    address = {Minneapolis, Minnesota},
    author = {Talmor, Alon  and Herzig, Jonathan  and Lourie, Nicholas and Berant, Jonathan},
    booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)},
    doi = {10.18653/v1/N19-1421},
    pages = {4149--4158},
    publisher = {Association for Computational Linguistics},
    title = {CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge},
    url = {https://www.aclweb.org/anthology/N19-1421},
    year = {2019}
}

# CODAH
@inproceedings{Chen2019CODAHAA,
    address = {Minneapolis, USA},
    author = {Chen, Michael  and D{'}Arcy, Mike  and Liu, Alisa  and Fernandez, Jared  and Downey, Doug},
    booktitle = {Proceedings of the 3rd Workshop on Evaluating Vector Space Representations for {NLP}},
    doi = {10.18653/v1/W19-2008},
    pages = {63--69},
    publisher = {Association for Computational Linguistics},
    title = {CODAH: An Adversarially-Authored Question Answering Dataset for Common Sense},
    url = {https://www.aclweb.org/anthology/W19-2008},
    year = {2019}
}
```

### Contributions

Thanks to [Bill Yuchen Lin](https://yuchenlin.xyz/), [Seyeon Lee](https://seyeon-lee.github.io/), [Xiaoyang Qiao](https://www.linkedin.com/in/xiaoyang-qiao/), [Xiang Ren](http://www-bcf.usc.edu/~xiangren/) for adding this dataset.