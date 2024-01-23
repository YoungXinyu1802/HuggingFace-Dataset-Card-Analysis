---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: ethos-sentiments

## Dataset Description

This dataset has been automatically processed by AutoTrain for project ethos-sentiments.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "well it's clear now why europeans can't differ niggers and shitskins from human",
    "target": 0
  },
  {
    "text": "These boys will then grow up with people making fun of them and they will then hate their parents for ruining their lives.",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['hate_speech', 'no_hate_speech'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 798 |
| valid        | 200 |
