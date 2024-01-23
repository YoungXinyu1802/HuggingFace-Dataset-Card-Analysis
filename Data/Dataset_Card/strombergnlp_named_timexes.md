---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Named Temporal Expressions dataset
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- token-classification
task_ids: []
---

# Dataset Card for named_timexes

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

- **Homepage:** 
- **Repository:** 
- **Paper:** [https://aclanthology.org/R13-1015/](https://aclanthology.org/R13-1015/)
- **Leaderboard:** 
- **Point of Contact:** [Leon Derczynski](https://github.com/leondz)

### Dataset Summary

This is a dataset annotated for _named temporal expression_ chunks.

The
commonest temporal expressions typically
contain date and time words, like April or
hours. Research into recognising and interpreting these typical expressions is mature in many languages. However, there is
a class of expressions that are less typical,
very varied, and difficult to automatically
interpret. These indicate dates and times,
but are harder to detect because they often do not contain time words and are not
used frequently enough to appear in conventional temporally-annotated corpora –
for example *Michaelmas* or *Vasant Panchami*.

For more details see [Recognising and Interpreting Named Temporal Expressions](https://aclanthology.org/R13-1015.pdf)

### Supported Tasks and Leaderboards

* Task: Named Entity Recognition (temporal expressions)

### Languages

Englsih

## Dataset Structure

### Data Instances

### Data Fields

Each tweet contains an ID, a list of tokens, and a list of timex chunk flags.


- `id`: a `string` feature.
- `tokens`: a `list` of `strings` .
- `ntimex_tags`: a `list` of class IDs (`int`s) for whether a token is out-of-timex or in a timex chunk.

```
  0: O
  1: T
```

### Data Splits

Section|Token count
---|---:
train|87 050
test|30 010

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

[Needs More Information]

### Licensing Information

Creative Commons Attribution 4.0 International (CC BY 4.0)

### Citation Information

```
@inproceedings{brucato-etal-2013-recognising,
    title = "Recognising and Interpreting Named Temporal Expressions",
    author = "Brucato, Matteo  and
      Derczynski, Leon  and
      Llorens, Hector  and
      Bontcheva, Kalina  and
      Jensen, Christian S.",
    booktitle = "Proceedings of the International Conference Recent Advances in Natural Language Processing {RANLP} 2013",
    month = sep,
    year = "2013",
    address = "Hissar, Bulgaria",
    publisher = "INCOMA Ltd. Shoumen, BULGARIA",
    url = "https://aclanthology.org/R13-1015",
    pages = "113--121",
}
```

### Contributions

Author-added dataset [@leondz](https://github.com/leondz) 
