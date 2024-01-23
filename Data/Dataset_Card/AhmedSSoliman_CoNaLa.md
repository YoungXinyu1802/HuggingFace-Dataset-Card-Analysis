---
task_categories:
- Code Generation
- Translation
- Text2Text generation
---
# CoNaLa Dataset for Code Generation

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been processed for Code Generation. CMU CoNaLa, the Code/Natural Language Challenge is a joint project of the Carnegie Mellon University NeuLab and STRUDEL Lab. This dataset was designed to test systems for generating program snippets from natural language. It is avilable at https://conala-corpus.github.io/ , and this is about 13k records from the full corpus of about 600k examples.


### Languages

English

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "intent": "convert a list to a dictionary in python",
    "snippet": "b = dict(zip(a[0::2], a[1::2]))"
  },
  {
    "intent": "python - sort a list of nested lists",
    "snippet": "l.sort(key=sum_nested)"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "intent": "Value(dtype='string', id=None)",
  "snippet": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train, validation and test split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 11125 |
| valid        | 1237 |
| test         | 500 |
