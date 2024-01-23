---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: consunmer-complain-multiclass-classification

## Dataset Description

This dataset has been automatically processed by AutoTrain for project consunmer-complain-multiclass-classification.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_Unnamed: 0": null,
    "text": "This is awful and borderline abuse. I can't imagine thinking that's even slightly okay",
    "target": 5
  },
  {
    "feat_Unnamed: 0": null,
    "text": "i didnt feel so hot",
    "target": 3
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_Unnamed: 0": "Value(dtype='int64', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['0', '1', '2', '3', '4', '5'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 20663 |
| valid        | 5167 |
