---
annotations_creators:
- expert-generated
language:
- ar
language_creators:
- expert-generated
license:
- cc-by-nd-4.0
multilinguality:
- monolingual
pretty_name: Qur'anic Reading Comprehension Dataset
size_categories:
- n<1K
- 1K<n<10K
source_datasets:
- original
tags:
- quran
- qa
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for the Qur'anic Reading Comprehension Dataset (QRCD)

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

- **Homepage:** https://sites.google.com/view/quran-qa-2022/home
- **Repository:** https://gitlab.com/bigirqu/quranqa/-/tree/main/
- **Paper:** https://dl.acm.org/doi/10.1145/3400396
- **Leaderboard:** 
- **Point of Contact:** @piraka9011

### Dataset Summary

The QRCD (Qur'anic Reading Comprehension Dataset) is composed of 1,093 tuples of question-passage pairs that are 
  coupled with their extracted answers to constitute 1,337 question-passage-answer triplets.

### Supported Tasks and Leaderboards

This task is evaluated as a ranking task.
To give credit to a QA system that may retrieve an answer (not necessarily at the first rank) that does not fully 
  match one of the gold answers but partially matches it, we use partial Reciprocal Rank (pRR) measure.
It is a variant of the traditional Reciprocal Rank evaluation metric that considers partial matching.
pRR is the official evaluation measure of this shared task.
We will also report Exact Match (EM) and F1@1, which are evaluation metrics applied only on the top predicted answer.
The EM metric is a binary measure that rewards a system only if the top predicted answer exactly matches one of the 
  gold answers.
Whereas, the F1@1 metric measures the token overlap between the top predicted answer and the best matching gold answer.
To get an overall evaluation score, each of the above measures is averaged over all questions.

### Languages

Qur'anic Arabic

## Dataset Structure

### Data Instances

To simplify the structure of the dataset, each tuple contains one passage, one question and a list that may contain 
  one or more answers to that question, as shown below:

```json
{
  "pq_id": "38:41-44_105",
  "passage": "واذكر عبدنا أيوب إذ نادى ربه أني مسني الشيطان بنصب وعذاب. اركض برجلك هذا مغتسل بارد وشراب. ووهبنا له أهله ومثلهم معهم رحمة منا وذكرى لأولي الألباب. وخذ بيدك ضغثا فاضرب به ولا تحنث إنا وجدناه صابرا نعم العبد إنه أواب.",
  "surah": 38,
  "verses": "41-44",
  "question": "من هو النبي المعروف بالصبر؟",
  "answers": [
    {
      "text": "أيوب",
      "start_char": 12
    }
  ]
}
```

Each Qur’anic passage in QRCD may have more than one occurrence; and each passage occurrence is paired with a different 
  question.
Likewise, each question in QRCD may have more than one occurrence; and each question occurrence is paired with a 
  different Qur’anic passage.
The source of the Qur'anic text in QRCD is the Tanzil project download page, which provides verified versions of the 
  Holy Qur'an in several scripting styles.
We have chosen the simple-clean text style of Tanzil version 1.0.2.

### Data Fields

* `pq_id`: Sample ID
* `passage`: Context text
* `surah`: Surah number
* `verses`: Verse range
* `question`: Question text
* `answers`: List of answers and their start character

### Data Splits

| **Dataset** | **%** | **# Question-Passage  Pairs** | **# Question-Passage-Answer  Triplets** |
|-------------|:-----:|:-----------------------------:|:---------------------------------------:|
| Training    |  65%  |              710              |                   861                   |
| Development |  10%  |              109              |                   128                   |
| Test        |  25%  |              274              |                   348                   |
| All         | 100%  |             1,093             |                  1,337                  |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

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

The QRCD v1.1 dataset is distributed under the CC-BY-ND 4.0 License https://creativecommons.org/licenses/by-nd/4.0/legalcode
For a human-readable summary of (and not a substitute for) the above CC-BY-ND 4.0 License, please refer to https://creativecommons.org/licenses/by-nd/4.0/

### Citation Information

```
@article{malhas2020ayatec,
  author = {Malhas, Rana and Elsayed, Tamer},
  title = {AyaTEC: Building a Reusable Verse-Based Test Collection for Arabic Question Answering on the Holy Qur’an},
  year = {2020},
  issue_date = {November 2020},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  volume = {19},
  number = {6},
  issn = {2375-4699},
  url = {https://doi.org/10.1145/3400396},
  doi = {10.1145/3400396},
  journal = {ACM Trans. Asian Low-Resour. Lang. Inf. Process.},
  month = {oct},
  articleno = {78},
  numpages = {21},
  keywords = {evaluation, Classical Arabic}
}
```
### Contributions

Thanks to [@piraka9011](https://github.com/piraka9011) for adding this dataset.
