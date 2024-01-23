---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: donut-vs-croissant

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project donut-vs-croissant.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<512x512 RGB PIL image>",
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
  "target": "ClassLabel(num_classes=2, names=['croissant', 'donut'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 133 |
| valid        | 362 |
