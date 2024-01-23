---
task_categories:
- image-classification

---
# Dataset for project: csgo-weapon-classification

## Dataset Description

This dataset has for project csgo-weapon-classification was collected with the help of a bulk google image downloader.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<1768x718 RGB PIL image>",
    "target": 0
  },
  {
    "image": "<716x375 RGBA PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['AK-47', 'AWP', 'Famas', 'Galil-AR', 'Glock', 'M4A1', 'M4A4', 'P-90', 'SG-553', 'UMP', 'USP'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1100 |
| valid        | 275 |
