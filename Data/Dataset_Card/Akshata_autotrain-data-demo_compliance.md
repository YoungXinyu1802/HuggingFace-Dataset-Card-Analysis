---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: demo_compliance

## Dataset Description

This dataset has been automatically processed by AutoTrain for project demo_compliance.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Welcome back Abhishek!  What can I do to help? ",
    "target": 0
  },
  {
    "text": "Hi , I am calling from ABC finance. I would like to inform you that you are eligible for a Personal Loan",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['Negative', 'Positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 31 |
| valid        | 9 |
