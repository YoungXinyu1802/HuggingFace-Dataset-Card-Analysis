---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: osdg-sdg-classifier

## Dataset Descritpion

This dataset has been pre-processed using standard python cleaning functions and further automatically processed by AutoTrain for project osdg-sdg-classifier.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "teams of technical experts elaborate and validate these plans in collaboration with the local commun[...]",
    "target": 14
  },
  {
    "text": "yet commitments to promote the cohesion of families cannot be seen in isolation from two critical el[...]",
    "target": 10
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=15, names=['1', '10', '11', '12', '13', '14', '15', '2', '3', '4', '5', '6', '7', '8', '9'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 14098 |
| valid        | 3533 |
