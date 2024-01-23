---
{}

---
# AutoTrain Dataset for project: dragino-7-7-max_495m

## Dataset Description

This dataset has been automatically processed by AutoTrain for project dragino-7-7-max_495m.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_rssi": -91,
    "feat_snr": 7.5,
    "target": 125.0
  },
  {
    "feat_rssi": -96,
    "feat_snr": 5.0,
    "target": 125.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_rssi": "Value(dtype='int64', id=None)",
  "feat_snr": "Value(dtype='float64', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 853 |
| valid        | 286 |
