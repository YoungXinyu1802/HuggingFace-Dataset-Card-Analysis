---
language:
- es
task_categories:
- text-classification
---
# AutoNLP Dataset for project: pruebapoems

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project pruebapoems.

### Languages

The BCP-47 code for the dataset's language is es.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "When I was fair and young, then favor graced me.\r\nOf many was I sought their mistress for to be.\r\nBu[...]",
    "target": 1
  },
  {
    "text": "Sigh no more, ladies, sigh no more.\r\n    Men were deceivers ever,\r\nOne foot in sea, and one on shore[...]",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=3, names=['Love', 'Mythology & Folklore', 'Nature'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 457 |
| valid        | 116 |
