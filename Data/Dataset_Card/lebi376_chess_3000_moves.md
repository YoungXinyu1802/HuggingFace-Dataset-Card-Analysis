---
task_categories:
- translation

---
# AutoTrain Dataset for project: chessbig

## Dataset Description

This dataset has been automatically processed by AutoTrain for project chessbig.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "source": "r1b1k1nr/p6p/2p1p1p1/1p1pPp2/B2P4/2P5/PP2KP1P/RN3R2 b kq - 0 16",
    "target": "b5a4"
  },
  {
    "source": "r1b1k2r/ppbp1ppp/2n3q1/8/2B1Pp2/3P1Q2/PPP2PPP/R4RK1 b kq - 1 11",
    "target": "c6d4"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "source": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2387 |
| valid        | 597 |
