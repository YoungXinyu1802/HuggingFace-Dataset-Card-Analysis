---
language:
- en
- jb
task_categories:
- translation

---
# AutoTrain Dataset for project: lojban-translation

## Dataset Description

This dataset has been automatically processed by AutoTrain for project lojban-translation.

### Languages

The BCP-47 code for the dataset's language is en2jb.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "source": "I read the poem for my child.",
    "target": "mi tcidu lo pemci te cu'u le panzi be mi"
  },
  {
    "source": "Jim is learning how to drive a car.",
    "target": "la jim cilre fi lo nu klasazri lo karce"
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
| train        | 8000 |
| valid        | 2000 |
