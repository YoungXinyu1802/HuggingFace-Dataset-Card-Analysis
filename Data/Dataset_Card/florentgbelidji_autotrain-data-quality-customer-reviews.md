---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: quality-customer-reviews

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project quality-customer-reviews.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": " Love this truck, I think it is light years better than the competition. I have driven or owned all [...]",
    "target": 1
  },
  {
    "text": " I purchased this to haul our 4 horse trailer since the standard iterations of the domestic vehicles[...]",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=5, names=['good', 'great', 'ok', 'poor', 'terrible'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 9166 |
| valid        | 2295 |
