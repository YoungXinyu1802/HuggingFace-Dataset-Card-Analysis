---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: swin-muppet

## Dataset Description

This dataset has been automatically processed by AutoTrain for project swin-muppet.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<286x286 RGB PIL image>",
    "target": 7
  },
  {
    "image": "<169x170 RGB PIL image>",
    "target": 13
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=24, names=['Animal', 'Beaker', 'Bert', 'BigBird', 'Bunsen', 'Camilla', 'CookieMonster', 'Elmo', 'Ernie', 'Floyd', 'Fozzie', 'Gonzo', 'Grover', 'Kermit', 'Oscar', 'Pepe', 'Piggy', 'Rowlf', 'Scooter', 'Statler', 'SwedishChef', 'TheCount', 'Waldorf', 'Zoot'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 599 |
| valid        | 162 |
