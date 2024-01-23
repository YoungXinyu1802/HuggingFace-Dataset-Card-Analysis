---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: TweetClimateAnalysis

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project TweetClimateAnalysis.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "What do you do if you are a global warming alarmist and real-world temperatures do not warm as much [...]",
    "target": 16
  },
  {
    "text": "(2.) A sun-blocking volcanic aerosols component to explain the sudden but temporary cooling of globa[...]",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=18, names=['0_0', '1_1', '1_2', '1_3', '1_4', '1_6', '1_7', '2_1', '2_3', '3_1', '3_2', '3_3', '4_1', '4_2', '4_4', '4_5', '5_1', '5_2'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 23436 |
| valid        | 2898 |
