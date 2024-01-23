---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: test_row2

## Dataset Description

This dataset has been automatically processed by AutoTrain for project test_row2.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<316x316 RGB PIL image>",
    "target": 1
  },
  {
    "image": "<316x316 RGB PIL image>",
    "target": 3
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=5, names=['animals', 'dance', 'food', 'sport', 'tech'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 392 |
| valid        | 101 |
