---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: ashwin_sentiment140dataset

## Dataset Description

This dataset has been automatically processed by AutoTrain for project ashwin_sentiment140dataset.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "@JordainFTW i didnt watch them BUT CALEB PLAYS NAZI ZOMBIES TOOOOOO!!!!!!!!!! OMG OMG OMG! HE IS MY BESTFREIND!  what do u needa tell me?",
    "target": 1
  },
  {
    "text": "@Jennymac22 too much info! good for you hun. I'm pleased for you. ",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '4'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2399 |
| valid        | 601 |
