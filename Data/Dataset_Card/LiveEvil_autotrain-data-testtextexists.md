---
language:
- en
task_categories:
- text-scoring

---
# AutoTrain Dataset for project: testtextexists

## Dataset Description

This dataset has been automatically processed by AutoTrain for project testtextexists.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "According to the National Soft Drink Association, the annual consumption of soda by the U.S. citizens is 600 cans",
    "target": 66.0
  },
  {
    "text": "Experts say new vaccines are fake!",
    "target": 50.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 19 |
| valid        | 18 |
