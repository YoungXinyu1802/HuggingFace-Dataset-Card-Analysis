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
- code-generation
- conditional-text-generation
task_ids: []
pretty_name: Lynx
tags:
- word-segmentation
---

# Dataset Card for Lynx

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

- **Paper:** [Helpful or Not? An investigation on the feasibility of identifier splitting via CNN-BiLSTM-CRF](https://ksiresearch.org/seke/seke18paper/seke18paper_167.pdf)

### Dataset Summary

In programming languages, identifiers are tokens (also called symbols) which name language entities.
Some of the kinds of entities an identifier might denote include variables, types, labels, subroutines, and packages.

Lynx is a dataset for identifier segmentation, i.e. the task of adding spaces between the words on a identifier.

Besides identifier segmentation, the gold labels for this dataset also include abbreviation expansion.

### Languages

- C

## Dataset Structure

### Data Instances

```
{
    "index": 3,
    "identifier": "abspath",
    "segmentation": "abs path",
    "expansion": "absolute path",
    "spans": {
        "text": [
            "abs"
        ],
        "expansion": [
            "absolute"
        ],
        "start": [
            0
        ],
        "end": [
            4
        ]
    }
}
```

### Data Fields

- `index`: a numerical index.
- `identifier`: the original identifier.
- `segmentation`: the gold segmentation for the identifier, without abbreviation expansion.
- `expansion`: the gold segmentation for the identifier, with abbreviation expansion.
- `spans`: the start and end index of each abbreviation, the text of the abbreviation and its corresponding expansion.

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

### Citation Information

```
@inproceedings{madani2010recognizing,
  title={Recognizing words from source code identifiers using speech recognition techniques},
  author={Madani, Nioosha and Guerrouj, Latifa and Di Penta, Massimiliano and Gueheneuc, Yann-Gael and Antoniol, Giuliano},
  booktitle={2010 14th European Conference on Software Maintenance and Reengineering},
  pages={68--77},
  year={2010},
  organization={IEEE}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.