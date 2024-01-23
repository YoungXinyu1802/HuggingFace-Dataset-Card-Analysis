---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: rottentomato

## Dataset Description

This dataset has been automatically processed by AutoTrain for project rottentomato.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "too much of storytelling moves away from solondz's social critique , casting its audience as that of intellectual lector in contemplation of the auteur's professional injuries .",
    "target": 1
  },
  {
    "text": "what the audience feels is exhaustion , from watching a movie that is dark ( dark green , to be exact ) , sour , bloody and mean .",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['neg', 'pos'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 852 |
| valid        | 214 |
