---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: guitarsproject

## Dataset Description

This dataset has been automatically processed by AutoTrain for project guitarsproject.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<1990x2520 RGB PIL image>",
    "target": 1
  },
  {
    "image": "<6000x4000 RGB PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['LesPaul', 'Stratocaster'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 80 |
| valid        | 21 |
