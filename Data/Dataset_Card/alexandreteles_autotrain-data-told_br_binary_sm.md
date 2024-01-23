---
language:
- pt
task_categories:
- text-classification

---
# AutoTrain Dataset for project: told_br_binary_sm

## Dataset Description

This dataset has been automatically processed by AutoTrain for project told_br_binary_sm.

### Languages

The BCP-47 code for the dataset's language is pt.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "@user agora n\u00e3o me d\u00e1 mais, mas antes, porra",
    "target": 1
  },
  {
    "text": "pires \u00e9 fodido fds mais um",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5599 |
| valid        | 1401 |
