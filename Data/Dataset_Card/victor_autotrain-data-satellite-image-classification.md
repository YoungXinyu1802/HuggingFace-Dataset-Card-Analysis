---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: satellite-image-classification

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project satellite-image-classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<256x256 CMYK PIL image>",
    "target": 0
  },
  {
    "image": "<256x256 CMYK PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=1, names=['cloudy'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1200 |
| valid        | 300 |
