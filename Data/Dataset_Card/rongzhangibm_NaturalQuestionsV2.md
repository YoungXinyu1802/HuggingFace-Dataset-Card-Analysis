---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: Natural Questions
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- open-domain-qa
paperswithcode_id: natural-questions
---

# Dataset Card for Natural Questions

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

- **Homepage:** [https://ai.google.com/research/NaturalQuestions/dataset](https://ai.google.com/research/NaturalQuestions/dataset)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 42981 MB
- **Size of the generated dataset:** 139706 MB
- **Total amount of disk used:** 182687 MB

### Dataset Summary

The NQ corpus contains questions from real users, and it requires QA systems to
read and comprehend an entire Wikipedia article that may or may not contain the
answer to the question. The inclusion of real user questions, and the
requirement that solutions should read an entire page to find the answer, cause
NQ to be a more realistic and challenging task than prior QA datasets.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### default

- **Size of downloaded dataset files:** 42981 MB
- **Size of the generated dataset:** 139706 MB
- **Total amount of disk used:** 182687 MB

An example of 'train' looks as follows.
```

```

### Data Fields

The data fields are the same among all splits.

#### default

```
"id": datasets.Value("string"),
"document": {
    "title": datasets.Value("string"),
    "url": datasets.Value("string"),
    "html": datasets.Value("string"),
    "tokens": datasets.features.Sequence(
        {
    	    "token": datasets.Value("string"),
	    "is_html": datasets.Value("bool"),  
            "start_byte": datasets.Value("int64"),
	    "end_byte": datasets.Value("int64"),
	}
    ),
},
"question": {
    "text": datasets.Value("string"),
    "tokens": datasets.features.Sequence(datasets.Value("string")),
},
"long_answer_candidates": datasets.features.Sequence(
    {
        "start_token": datasets.Value("int64"),
        "end_token": datasets.Value("int64"),
        "start_byte": datasets.Value("int64"),
        "end_byte": datasets.Value("int64"),
        "top_level": datasets.Value("bool"),
    }
),
"annotations": datasets.features.Sequence(
    {
        "id": datasets.Value("string"),
        "long_answer": {
            "start_token": datasets.Value("int64"),
            "end_token": datasets.Value("int64"),
            "start_byte": datasets.Value("int64"),
            "end_byte": datasets.Value("int64"),
            "candidate_index": datasets.Value("int64")
        },
        "short_answers": datasets.features.Sequence(
            {
                "start_token": datasets.Value("int64"),
                "end_token": datasets.Value("int64"),
                "start_byte": datasets.Value("int64"),
                "end_byte": datasets.Value("int64"),
                "text": datasets.Value("string"),
            }
        ),
        "yes_no_answer": datasets.features.ClassLabel(
            names=["NO", "YES"]
        ),  # Can also be -1 for NONE.
    }
)
```


### Data Splits

| name    |  train | validation |
|---------|-------:|-----------:|
| default | 307373 |       7830 |
| dev     |    N/A |       7830 |

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

[Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/).

### Citation Information

```

@article{47761,
title	= {Natural Questions: a Benchmark for Question Answering Research},
author	= {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
year	= {2019},
journal	= {Transactions of the Association of Computational Linguistics}
}

```


### Contributions
