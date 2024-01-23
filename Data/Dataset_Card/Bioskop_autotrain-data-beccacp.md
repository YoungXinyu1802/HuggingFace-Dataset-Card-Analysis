---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: beccacp

## Dataset Description

This dataset has been automatically processed by AutoTrain for project beccacp.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<1600x838 RGB PIL image>",
    "target": 1
  },
  {
    "image": "<1200x628 RGB PIL image>",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=2, names=['Becca', 'Lucy'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 9 |
| valid        | 4 |
