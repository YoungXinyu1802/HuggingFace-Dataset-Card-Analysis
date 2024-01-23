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
pretty_name: Binkley
tags:
- word-segmentation
---

# Dataset Card for Binkley

## Dataset Description

- **Paper:** [Normalizing Source Code Vocabulary](https://www.researchgate.net/publication/224198190_Normalizing_Source_Code_Vocabulary)

### Dataset Summary

In programming languages, identifiers are tokens (also called symbols) which name language entities.
Some of the kinds of entities an identifier might denote include variables, types, labels, subroutines, and packages.

Binkley is a dataset for identifier segmentation, i.e. the task of adding spaces between the words on a identifier.

### Languages

- C
- C++
- Java

## Dataset Structure

### Data Instances

```
{
    "index": 0,
    "identifier": "init_g16_i",
    "segmentation": "init _ g 16 _ i"
}
```

### Data Fields

- `index`: a numerical index.
- `identifier`: the original identifier.
- `segmentation`: the gold segmentation for the identifier.

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

## Additional Information

### Citation Information

```
@inproceedings{inproceedings,
author = {Lawrie, Dawn and Binkley, David and Morrell, Christopher},
year = {2010},
month = {11},
pages = {3 - 12},
title = {Normalizing Source Code Vocabulary},
journal = {Proceedings - Working Conference on Reverse Engineering, WCRE},
doi = {10.1109/WCRE.2010.10}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.