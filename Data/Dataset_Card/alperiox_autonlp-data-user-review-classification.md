---
language:
- en
task_categories:
- text-classification
---
# AutoNLP Dataset for project: user-review-classification

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project user-review-classification.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "awful",
    "target": 3
  },
  {
    "text": "it says you can only read three stories a month and yet everything i clicked on was blank and now it[...]",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=4, names=['CONTENT', 'INTERFACE', 'SUBSCRIPTION', 'USER_EXPERIENCE'], names_file=None, id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 275 |
| valid        | 71 |
