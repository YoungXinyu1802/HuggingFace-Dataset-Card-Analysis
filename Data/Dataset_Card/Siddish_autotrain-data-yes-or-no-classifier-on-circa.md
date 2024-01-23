---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: yes-or-no-classifier-on-circa

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project yes-or-no-classifier-on-circa.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Situation: X wants to know about Y's food preferences.\nQ: Do you like burritos\nA: Any Mexican food i[...]",
    "target": 6
  },
  {
    "text": "Situation: X wants to know about Y's music preferences.\nQ: Would you like to go to a music club?\nA: [...]",
    "target": 7
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=8, names=['I am not sure how X will interpret Y\u2019s answer', 'In the middle, neither yes nor no', 'No', 'Other', 'Probably no', 'Probably yes / sometimes yes', 'Yes', 'Yes, subject to some conditions'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 25218 |
| valid        | 6307 |
