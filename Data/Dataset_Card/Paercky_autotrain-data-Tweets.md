---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: Tweets

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project Tweets.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "So the mask mandate goes away the day after #Furnal2022 ends, and you know what will happen after th[...]",
    "target": 0
  },
  {
    "text": "@EwanMacKenna Also does anyone know whether Margaret Buttimer of Bandon is still in prison for the '[...]",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=3, names=['1', '2', '3'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1679 |
| valid        | 420 |
