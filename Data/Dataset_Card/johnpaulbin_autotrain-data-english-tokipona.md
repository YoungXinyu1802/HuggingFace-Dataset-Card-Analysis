---
task_categories:
- translation

---
# AutoTrain Dataset for project: english-tokipona

## Dataset Description

This dataset has been automatically processed by AutoTrain for project english-tokipona.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": "mi kama jo e pali ante.",
    "source": "I'll find another job."
  },
  {
    "target": "tenpo pini weka la mi moku lon poka sina.",
    "source": "It's been a while since we've had lunch together."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "Value(dtype='string', id=None)",
  "source": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 16824 |
| valid        | 4206 |
