---
{}

---
# AutoTrain Dataset for project: air

## Dataset Description

This dataset has been automatically processed by AutoTrain for project air.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 0.04100000113248825,
    "id": 1,
    "feat_split": "train"
  },
  {
    "target": 0.04800000041723251,
    "id": 2,
    "feat_split": "train"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "Value(dtype='float32', id=None)",
  "id": "Value(dtype='int64', id=None)",
  "feat_split": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1467 |
| valid        | 1467 |
