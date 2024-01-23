---
language:
- en
---
# AutoTrain Dataset for project: company

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project company.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tokens": [
      "sahil",
      "prasad",
      "president",
      "www",
      "swimcentre",
      "com",
      "banik",
      "baalkrishan",
      "gandhi",
      "com",
      "no",
      "satish",
      "nagar",
      "hisar"
    ],
    "tags": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  },
  {
    "tokens": [
      "olivia",
      "wilson",
      "real",
      "estate",
      "agent",
      "reallygreatsite",
      "com",
      "anywhere",
      "st",
      "any",
      "city",
      "st",
      "www",
      "reallygreatsite",
      "com"
    ],
    "tags": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=2, names=['0', '9'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 999651 |
| valid        | 499630 |
