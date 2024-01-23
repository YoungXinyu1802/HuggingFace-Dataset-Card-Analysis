---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: image-classification-test-18

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project image-classification-test-18.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<224x224 RGB PIL image>",
    "target": 2
  },
  {
    "image": "<224x224 RGB PIL image>",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(num_classes=3, names=['ADONIS', 'AFRICAN GIANT SWALLOWTAIL', 'AMERICAN SNOOT'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 269 |
| valid        | 69 |
