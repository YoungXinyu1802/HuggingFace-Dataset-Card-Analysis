---
language:
- pt
---
# AutoNLP Dataset for project: pos-tag-bosque

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project pos-tag-bosque.

### Languages

The BCP-47 code for the dataset's language is pt.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tags": [
      5,
      7,
      0
    ],
    "tokens": [
      "Um",
      "revivalismo",
      "refrescante"
    ]
  },
  {
    "tags": [
      5,
      11,
      11,
      11,
      3,
      5,
      7,
      1,
      5,
      7,
      0,
      12
    ],
    "tokens": [
      "O",
      "7",
      "e",
      "Meio",
      "\u00e9",
      "um",
      "ex-libris",
      "de",
      "a",
      "noite",
      "algarvia",
      "."
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tags": "Sequence(feature=ClassLabel(num_classes=17, names=['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X'], names_file=None, id=None), length=-1, id=None)",
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 8328 |
| valid        | 476 |
