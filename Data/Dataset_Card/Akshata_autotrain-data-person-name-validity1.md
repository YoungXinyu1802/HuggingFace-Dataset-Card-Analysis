---
language:
- en

---
# AutoTrain Dataset for project: person-name-validity1

## Dataset Description

This dataset has been automatically processed by AutoTrain for project person-name-validity1.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tokens": [
      "divided"
    ],
    "tags": [
      0
    ]
  },
  {
    "tokens": [
      "nusrat"
    ],
    "tags": [
      1
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=2, names=['0', '2'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2499 |
| valid        | 499 |
