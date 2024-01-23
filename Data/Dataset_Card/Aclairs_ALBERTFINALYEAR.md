---
{}

---
# AutoNLP Dataset for project: ALBERTFINALYEAR

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project ALBERTFINALYEAR.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "Hasidic or Chasidic Judaism overlaps significantly with Haredi Judaism in its engagement with the se[...]",
    "question": "What overlaps significantly with Haredi Judiasm?",
    "answers.text": [
      "Chasidic Judaism"
    ],
    "answers.answer_start": [
      11
    ]
  },
  {
    "context": "Data compression can be viewed as a special case of data differencing: Data differencing consists of[...]",
    "question": "What can classified as data differencing with empty source data?",
    "answers.text": [
      "Data compression",
      "data compression"
    ],
    "answers.answer_start": [
      0,
      400
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "context": "Value(dtype='string', id=None)",
  "question": "Value(dtype='string', id=None)",
  "answers.text": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "answers.answer_start": "Sequence(feature=Value(dtype='int32', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 87433 |
| valid        | 10544 |
