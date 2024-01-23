---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: i-bert-twitter-sentiment

## Dataset Description

This dataset has been automatically processed by AutoTrain for project i-bert-twitter-sentiment.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Thanks\\u002c Dave! Great show tonight.  Sorry\\u002c Craig. I\\u2019ve got to get to bed. I\\u2019ll catch you tomorrow. @user  David Letterman",
    "target": 2
  },
  {
    "text": "\"I've been watching Gilmore Girls for the past 3 hours. Oops, happy Thursday!\"",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['negative', 'neutral', 'positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 36491 |
| valid        | 9124 |
