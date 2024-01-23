---
{}

---
# AutoTrain Dataset for project: ZuoZhuan

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project ZuoZhuan.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tokens": [
      "\u4e09",
      "\u5de1",
      "\u6578",
      "\u4e4b",
      "\u3002"
    ],
    "tags": [
      6,
      23,
      23,
      15,
      24
    ]
  },
  {
    "tokens": [
      "\u9042",
      "\u6b78",
      "\uff0c",
      "\u5fa9",
      "\u547d",
      "\uff0c",
      "\u800c",
      "\u81ea",
      "\u62d8",
      "\u65bc",
      "\u53f8",
      "\u6557",
      "\u3002"
    ],
    "tags": [
      3,
      23,
      24,
      23,
      8,
      24,
      2,
      15,
      23,
      13,
      8,
      8,
      24
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=28, names=['/a', '/b', '/c', '/d', '/f', '/j', '/m', '/mr', '/n', '/nn', '/nr', '/ns', '/nsr', '/p', '/q', '/r', '/rn', '/rr', '/rs', '/s', '/sv', '/t', '/u', '/v', '/w', '/wv', '/y', '/yv'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5836 |
| valid        | 2860 |
