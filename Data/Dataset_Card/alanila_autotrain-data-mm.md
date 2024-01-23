---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: mm

## Dataset Description

This dataset has been automatically processed by AutoTrain for project mm.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Email from attorney A Dutkanych regarding executed Settlement Agreement",
    "target": "Email from attorney A Dutkanych regarding executed Settlement Agreement"
  },
  {
    "text": "Telephone conference with A Royer regarding additional factual background information relating to O Stapletons Charge of Discrimination allegations",
    "target": "Telephone conference with A Royer regarding additional factual background information as to O Stapletons Charge of Discrimination allegations"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 88 |
| valid        | 22 |
