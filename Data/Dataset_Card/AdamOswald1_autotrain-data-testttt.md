---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: testttt

## Dataset Description

This dataset has been automatically processed by AutoTrain for project testttt.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<113x220 RGB PIL image>",
    "target": 2
  },
  {
    "image": "<1280x720 RGB PIL image>",
    "target": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['Adult Chara', 'Adult Chara and Young Chara', 'Chara', 'Female Kris', 'Kris', 'Kris and Adult Chara', 'Kris and Chara', 'Kris and Female Chara', 'Kris and Male Chara', 'Kris and The Player', 'Kris and a Soul', 'Kris next to the Ghost of Chara', 'Male Kris', 'Male Kris and Female Kris', 'StoryShift Chara', 'StoryShift Chara and Young Chara', 'Teen Chara and Young Chara', 'Teenager Chara and Young Chara', 'Young Chara'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 184 |
| valid        | 58 |
