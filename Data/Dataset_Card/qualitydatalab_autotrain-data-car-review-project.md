---
language:
- en
task_categories:
- text-classification
---
# AutoTrain Dataset for project: car-review-project

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project car-review-project. It contains consumer car ratings and reviews from [Edmunds website](https://www.kaggle.com/datasets/ankkur13/edmundsconsumer-car-ratings-and-reviews)

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": " ",
    "target": 1
  },
  {
    "text": " Mazda truck costs less than the sister look-a-like Ford; Mazda is a \"A\" series of the Ford Ranger, [...]",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=3, names=['great', 'ok', 'poor'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 19731 |
| valid        | 4935 |
