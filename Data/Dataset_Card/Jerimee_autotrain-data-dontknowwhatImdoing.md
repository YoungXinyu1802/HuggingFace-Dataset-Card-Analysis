---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: dontknowwhatImdoing

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project dontknowwhatImdoing.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Gaston",
    "target": 1
  },
  {
    "text": "Churchundyr",
    "target": 0
  }
]
```

Note that, sadly, it flipped the boolean, using 1 for mundane and 0 for goblin.

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['Goblin', 'Mundane'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 965 |
| valid        | 242 |
