---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: chest-xray-demo

## Dataset Description

This dataset has been automatically processed by AutoTrain for project chest-xray-demo.

The original dataset is located at https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

## Dataset Structure

```
├── train
│   ├── NORMAL
│   └── PNEUMONIA
└── valid
    ├── NORMAL
    └── PNEUMONIA
```

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<2090x1858 L PIL image>",
    "target": 0
  },
  {
    "image": "<1422x1152 L PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=2, names=['NORMAL', 'PNEUMONIA'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follows:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5216 |
| valid        | 624 |
