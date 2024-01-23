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
pretty_name: BT11
tags:
- word-segmentation
---

# Dataset Card for BT11

## Dataset Description

- **Paper:** [Helpful or Not? An investigation on the feasibility of identifier splitting via CNN-BiLSTM-CRF](https://ksiresearch.org/seke/seke18paper/seke18paper_167.pdf)

### Dataset Summary

In programming languages, identifiers are tokens (also called symbols) which name language entities.
Some of the kinds of entities an identifier might denote include variables, types, labels, subroutines, and packages.

BT11 is a dataset for identifier segmentation, i.e. the task of adding spaces between the words on a identifier.

### Languages

- Java

## Dataset Structure

### Data Instances

```
{
    "index": 20170,
    "identifier": "currentLineHighlight",
    "segmentation": "current Line Highlight"
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
@inproceedings{butler2011improving,
  title={Improving the tokenisation of identifier names},
  author={Butler, Simon and Wermelinger, Michel and Yu, Yijun and Sharp, Helen},
  booktitle={European Conference on Object-Oriented Programming},
  pages={130--154},
  year={2011},
  organization={Springer}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.