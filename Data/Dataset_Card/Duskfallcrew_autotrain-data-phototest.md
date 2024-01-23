---
task_categories:
- image-classification
- text-to-image
license: creativeml-openrail-m
language:
- en
pretty_name: Phototest
size_categories:
- 1K<n<10K
---
# AutoTrain Dataset for project: phototest

## Dataset Description

This dataset has been automatically processed by AutoTrain for project phototest.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<768x768 RGB PIL image>",
    "target": 0
  },
  {
    "image": "<768x768 RGB PIL image>",
    "target": 3
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 72 |
| valid        | 19 |