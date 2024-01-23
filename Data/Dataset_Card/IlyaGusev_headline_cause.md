---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- ru
- en
license:
- cc0-1.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
pretty_name: HeadlineCause
tags:
- causal-reasoning
---

# Dataset Card for HeadlineCause

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

- **Homepage:** https://github.com/IlyaGusev/HeadlineCause
- **Paper:** [HeadlineCause: A Dataset of News Headlines for Detecting Causalities](https://arxiv.org/abs/2108.12626)
- **Point of Contact:** [Ilya Gusev](ilya.gusev@phystech.edu)

### Dataset Summary

A dataset for detecting implicit causal relations between pairs of news headlines. The dataset includes over 5000 headline pairs from English news and over 9000 headline pairs from Russian news labeled through crowdsourcing. The pairs vary from totally unrelated or belonging to the same general topic to the ones including causation and refutation relations.

### Usage
Loading Russian Simple task:
```python
from datasets import load_dataset
dataset = load_dataset("IlyaGusev/headline_cause", "ru_simple")
```

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

This dataset consists of two parts, Russian and English.

## Dataset Structure

### Data Instances
There is an URL, a title, and a timestamp for each of the two headlines in every data instance. A label is presented in three fields. 'Result' field is a textual label, 'label' field is a numeric label, and the 'agreement' field shows the majority vote agreement between annotators. Additional information includes instance ID and the presence of the link between two articles.

```
{
    'left_url': 'https://www.kommersant.ru/doc/4347456',
    'right_url': 'https://tass.ru/kosmos/8488527',
    'left_title': 'NASA: информация об отказе сотрудничать с Россией по освоению Луны некорректна',
    'right_title': 'NASA назвало некорректными сообщения о нежелании США включать РФ в соглашение по Луне',
    'left_timestamp': datetime.datetime(2020, 5, 15, 19, 46, 20),
    'right_timestamp': datetime.datetime(2020, 5, 15, 19, 21, 36),
    'label': 0,
    'result': 'not_cause',
    'agreement': 1.0,
    'id': 'ru_tg_101',
    'has_link': True
}
```

### Data Splits

| Dataset | Split | Number of Instances |
|:---------|:---------|:---------|
| ru_simple | train | 7,641 |
|  | validation | 955 |
|  | test | 957 |
| en_simple | train | 4,332 |
|  | validation | 542 |
|  | test | 542 |
| ru_full | train | 5,713 |
|  | validation | 715 |
|  | test | 715 |
| en_full | train | 2,009 |
|  | validation | 251 |
|  | test | 252 |

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

Every candidate pair was annotated with [Yandex Toloka](https://toloka.ai/), a crowdsourcing platform. The task was to determine a relationship between two headlines, A and B. There were seven possible options: titles are almost the same, A causes B, B causes A, A refutes B, B refutes A, A linked with B in another way, A is not linked to B. An annotation guideline was in Russian for Russian news and in English for English news.

Guidelines:
* Russian: [link](https://ilyagusev.github.io/HeadlineCause/toloka/ru/instruction.html)
* English: [link](https://ilyagusev.github.io/HeadlineCause/toloka/en/instruction.html)

Ten workers annotated every pair. The total annotation budget was 870$, with the estimated hourly wage paid to participants of 45 cents. Annotation management was semi-automatic. Scripts are available in the [Github repository](https://github.com/IlyaGusev/HeadlineCause).

#### Who are the annotators?

Yandex Toloka workers were the annotators, 457 workers for the Russian part, 180 workers for the English part.

### Personal and Sensitive Information

The dataset is not anonymized, so individuals' names can be found in the dataset. Information about the original author is not included in the dataset. No information about annotators is included except a platform worker ID.

## Considerations for Using the Data

### Social Impact of Dataset

We do not see any direct malicious applications of our work. The data probably do not contain offensive content, as news agencies usually do not produce it, and a keyword search returned nothing. However, there are news documents in the dataset on several sensitive topics.

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

The data was collected by Ilya Gusev.

### Licensing Information

[More Information Needed]

### Citation Information

```bibtex
@misc{gusev2021headlinecause,
      title={HeadlineCause: A Dataset of News Headlines for Detecting Causalities}, 
      author={Ilya Gusev and Alexey Tikhonov},
      year={2021},
      eprint={2108.12626},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

[N/A]