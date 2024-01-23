---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: histopathological_image_classification

## Dataset Description

This dataset has been automatically processed by AutoTrain for project histopathological_image_classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<700x460 RGB PIL image>",
    "target": 6
  },
  {
    "image": "<700x460 RGB PIL image>",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['1', '2', '3', '4', '5', '6', '7', '8'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 333 |
| valid        | 89 |
