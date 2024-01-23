---
annotations_creators:
  - expert-generated
language_creators:
  - expert-generated
language:
  - en
license:
  - cc-by-4.0
multilinguality:
  - monolingual
pretty_name: BCOPA
size_categories:
  - unknown
source_datasets:
  - extended|copa
task_categories:
  - question-answering
task_ids:
  - multiple-choice-qa
---

# Dataset Card for "Balanced COPA"

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

- **Homepage:** [https://balanced-copa.github.io/](https://balanced-copa.github.io/)
- **Repository:** [Balanced COPA](https://github.com/Balanced-COPA/Balanced-COPA)
- **Paper:** [When Choosing Plausible Alternatives, Clever Hans can be Clever](https://aclanthology.org/D19-6004/)
- **Point of Contact:** [@pkavumba](https://github.com/pkavumba)

### Dataset Summary

Bala-COPA: An English language Dataset for Training Robust Commonsense Causal Reasoning Models

The Balanced Choice of Plausible Alternatives dataset is a benchmark for training machine learning models that are robust to superficial cues/spurious correlations. The dataset extends the COPA dataset(Roemmele et al. 2011) with mirrored instances that mitigate against token-level superficial cues in the original COPA answers. The superficial cues in the original COPA datasets result from an unbalanced token distribution between the correct and the incorrect answer choices, i.e., some tokens appear more in the correct choices than the incorrect ones. Balanced COPA equalizes the token distribution by adding mirrored instances with identical answer choices but different labels.
The details about the creation of Balanced COPA and the implementation of the baselines are available in the paper.

Balanced COPA language en

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

- English

## Dataset Structure

### Data Instances

An example of 'validation' looks as follows.

```
{
    "id": 1,
    "premise": "My body cast a shadow over the grass.",
    "choice1": "The sun was rising.",
    "choice2": "The grass was cut.",
    "question": "cause",
    "label": 1,
    "mirrored": false,
}

{
    "id": 1001,
    "premise": "The garden looked well-groomed.",
    "choice1": "The sun was rising.",
    "choice2": "The grass was cut.",
    "question": "cause",
    "label": 1,
    "mirrored": true,
}
```

### Data Fields

The data fields are the same among all splits.

#### en

- `premise`: a `string` feature.
- `choice1`: a `string` feature.
- `choice2`: a `string` feature.
- `question`: a `string` feature.
- `label`: a `int32` feature.
- `id`: a `int32` feature.
- `mirrored`: a `bool` feature.

### Data Splits

| validation | test |
| ---------: | ---: |
|      1,000 |  500 |

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

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

```
  @inproceedings{kavumba-etal-2019-choosing,
    title = "When Choosing Plausible Alternatives, Clever Hans can be Clever",
    author = "Kavumba, Pride  and
      Inoue, Naoya  and
      Heinzerling, Benjamin  and
      Singh, Keshav  and
      Reisert, Paul  and
      Inui, Kentaro",
    booktitle = "Proceedings of the First Workshop on Commonsense Inference in Natural Language Processing",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-6004",
    doi = "10.18653/v1/D19-6004",
    pages = "33--42",
    abstract = "Pretrained language models, such as BERT and RoBERTa, have shown large improvements in the commonsense reasoning benchmark COPA. However, recent work found that many improvements in benchmarks of natural language understanding are not due to models learning the task, but due to their increasing ability to exploit superficial cues, such as tokens that occur more often in the correct answer than the wrong one. Are BERT{'}s and RoBERTa{'}s good performance on COPA also caused by this? We find superficial cues in COPA, as well as evidence that BERT exploits these cues.To remedy this problem, we introduce Balanced COPA, an extension of COPA that does not suffer from easy-to-exploit single token cues. We analyze BERT{'}s and RoBERTa{'}s performance on original and Balanced COPA, finding that BERT relies on superficial cues when they are present, but still achieves comparable performance once they are made ineffective, suggesting that BERT learns the task to a certain degree when forced to. In contrast, RoBERTa does not appear to rely on superficial cues.",
}

@inproceedings{roemmele2011choice,
  title={Choice of plausible alternatives: An evaluation of commonsense causal reasoning},
  author={Roemmele, Melissa and Bejan, Cosmin Adrian and Gordon, Andrew S},
  booktitle={2011 AAAI Spring Symposium Series},
  year={2011},
  url={https://people.ict.usc.edu/~gordon/publications/AAAI-SPRING11A.PDF},
}

```

### Contributions

Thanks to [@pkavumba](https://github.com/pkavumba) for adding this dataset.
