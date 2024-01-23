---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: acc_keys

## Dataset Description

This dataset has been automatically processed by AutoTrain for project acc_keys.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 2,
    "text": " workon"
  },
  {
    "target": 5,
    "text": " contact"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=11, names=['A101', 'A102', 'A103', 'A104', 'A105', 'A106', 'A107', 'A108', 'A109', 'A110', 'A112'], id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 457 |
| valid        | 120 |
