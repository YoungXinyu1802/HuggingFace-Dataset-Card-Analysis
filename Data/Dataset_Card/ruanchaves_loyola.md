---
annotations_creators:
- expert-generated
language_creators:
- machine-generated
language:
- code
license:
- unknown
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- structure-prediction
task_ids: []
pretty_name: The Loyola University of Delaware Identifier Splitting Oracle
tags:
- word-segmentation
---

# Dataset Card for The Loyola University of Delaware Identifier Splitting Oracle

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
  
## Dataset Description

- **Repository:** [Loyola University of Delaware Identifier Splitting Oracle](http://www.cs.loyola.edu/~binkley/ludiso/)
- **Paper:** [An empirical study of identifier splitting techniques](https://dl.acm.org/doi/10.1007/s10664-013-9261-0)

### Dataset Summary

In programming languages, identifiers are tokens (also called symbols) which name language entities.
Some of the kinds of entities an identifier might denote include variables, types, labels, subroutines, and packages.

The Loyola University of Delaware Identifier Splitting Oracle is a dataset for identifier segmentation, 
i.e. the task of adding spaces between the words on a identifier.

### Languages

- Java
- C
- C++

## Dataset Structure

### Data Instances

```
{
    "index": 0,
    "identifier": "::CreateProcess",
    "segmentation": ":: Create Process",
    "language": "cpp",
    "source": "mozilla-source-1.1"
}
```

### Data Fields

- `index`: a numerical index.
- `identifier`: the original identifier.
- `segmentation`: the gold segmentation for the identifier.
- `language`: the programming language of the source.
- `source`: the source of the identifier.

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

### Citation Information

```
@article{hill2014empirical,
  title={An empirical study of identifier splitting techniques},
  author={Hill, Emily and Binkley, David and Lawrie, Dawn and Pollock, Lori and Vijay-Shanker, K},
  journal={Empirical Software Engineering},
  volume={19},
  number={6},
  pages={1754--1780},
  year={2014},
  publisher={Springer}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.