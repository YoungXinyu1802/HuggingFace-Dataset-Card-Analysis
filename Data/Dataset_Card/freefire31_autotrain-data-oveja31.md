---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: oveja31

## Dataset Description

This dataset has been automatically processed by AutoTrain for project oveja31.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<1424x1424 RGB PIL image>",
    "target": 0
  },
  {
    "image": "<1627x1627 RGB PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=1, names=['oveja'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 4 |
| valid        | 1 |
