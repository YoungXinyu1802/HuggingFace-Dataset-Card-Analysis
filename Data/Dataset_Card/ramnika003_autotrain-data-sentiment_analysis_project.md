---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: sentiment_analysis_project

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project sentiment_analysis_project.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Realizing that I don`t have school today... or tomorrow... or for the next few months.  I really nee[...]",
    "target": 1
  },
  {
    "text": "Good morning tweeps. Busy this a.m. but not in a working way",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=3, names=['negative', 'neutral', 'positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 16180 |
| valid        | 4047 |
