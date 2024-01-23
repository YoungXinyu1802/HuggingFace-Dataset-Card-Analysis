---
task_categories:
- image-classification

---
# Dataset for project: food-classification

## Dataset Description

This dataset has been processed for project food-classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<308x512 RGB PIL image>",
    "target": 0
  },
  {
    "image": "<512x512 RGB PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['apple_pie', 'falafel', 'french_toast', 'ice_cream', 'ramen', 'sushi', 'tiramisu'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1050 |
| valid        | 350 |
