---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: ex-and-pt

## Dataset Description

This dataset has been automatically processed by AutoTrain for project ex-and-pt.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<3840x2160 RGB PIL image>",
    "target": 2
  },
  {
    "image": "<3840x2160 RGBA PIL image>",
    "target": 5
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['EX and PT', 'EX and PT Logo', 'EX and PT Mutant', 'EX and PT Mutants', 'EX and PT TCG', 'Vagitron'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 15 |
| valid        | 7 |
