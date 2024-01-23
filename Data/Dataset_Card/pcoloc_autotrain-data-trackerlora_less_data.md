---
{}

---
# AutoTrain Dataset for project: trackerlora_less_data

## Dataset Description

This dataset has been automatically processed by AutoTrain for project trackerlora_less_data.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "id": 444,
    "feat_rssi": -113.0,
    "feat_snr": -9.25,
    "feat_spreading_factor": 7,
    "feat_potencia": 14,
    "target": 308.0
  },
  {
    "id": 144,
    "feat_rssi": -77.0,
    "feat_snr": 8.800000190734863,
    "feat_spreading_factor": 7,
    "feat_potencia": 14,
    "target": 126.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "id": "Value(dtype='int64', id=None)",
  "feat_rssi": "Value(dtype='float64', id=None)",
  "feat_snr": "Value(dtype='float64', id=None)",
  "feat_spreading_factor": "Value(dtype='int64', id=None)",
  "feat_potencia": "Value(dtype='int64', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 139 |
| valid        | 40 |
