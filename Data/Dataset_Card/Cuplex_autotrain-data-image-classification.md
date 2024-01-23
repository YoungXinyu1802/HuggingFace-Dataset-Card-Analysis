---
task_categories:
- image-classification
license: apache-2.0
tags:
- flowers
pretty_name: Autotrained Flowers
---
# AutoTrain Dataset for project: image-classification

## Dataset Description

This dataset has been automatically processed by AutoTrain for project image-classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<500x333 RGB PIL image>",
    "target": 0
  },
  {
    "image": "<320x240 RGB PIL image>",
    "target": 4
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=5, names=['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 160 |
| valid        | 40 |