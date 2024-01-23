---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: dog-classifiers

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project dog-classifiers.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<474x592 RGB PIL image>",
    "target": 1
  },
  {
    "image": "<474x296 RGB PIL image>",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=5, names=['akita inu', 'corgi', 'leonberger', 'samoyed', 'shiba inu'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 598 |
| valid        | 150 |