---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: weather-classification

## Dataset Description

This dataset has been automatically processed by AutoTrain for project weather-classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<771x514 RGB PIL image>",
    "target": 2
  },
  {
    "image": "<269x254 RGB PIL image>",
    "target": 8
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['dew', 'fogsmog', 'frost', 'glaze', 'hail', 'lightning', 'rain', 'rainbow', 'rime', 'sandstorm', 'snow'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5484 |
| valid        | 1378 |
