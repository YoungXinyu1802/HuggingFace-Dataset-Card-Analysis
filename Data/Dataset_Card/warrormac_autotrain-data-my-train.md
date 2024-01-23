---
language:
- en
- es
task_categories:
- translation

---
# AutoTrain Dataset for project: my-train

## Dataset Description

This dataset has been automatically processed by AutoTrain for project my-train.

### Languages

The BCP-47 code for the dataset's language is en2es.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_eng": "eng",
    "feat_spa": "spa",
    "source": "Can you remember the first time you heard the Beatles?",
    "target": "\u00bfRecuerdas la primera vez que escuchaste a los Beatles?",
    "feat_Unnamed: 4": null,
    "feat_Unnamed: 5": null,
    "feat_Unnamed: 6": null,
    "feat_Unnamed: 7": null,
    "feat_Unnamed: 8": null,
    "feat_Unnamed: 9": null,
    "feat_Unnamed: 10": null,
    "feat_Unnamed: 11": null,
    "feat_Unnamed: 12": null,
    "feat_Unnamed: 13": null,
    "feat_Unnamed: 14": null,
    "feat_Unnamed: 15": null,
    "feat_Unnamed: 16": null,
    "feat_Unnamed: 17": null
  },
  {
    "feat_eng": "eng",
    "feat_spa": "spa",
    "source": "He is always talking big.",
    "target": "\u00c9l siempre est\u00e1 alardeando.",
    "feat_Unnamed: 4": null,
    "feat_Unnamed: 5": null,
    "feat_Unnamed: 6": null,
    "feat_Unnamed: 7": null,
    "feat_Unnamed: 8": null,
    "feat_Unnamed: 9": null,
    "feat_Unnamed: 10": null,
    "feat_Unnamed: 11": null,
    "feat_Unnamed: 12": null,
    "feat_Unnamed: 13": null,
    "feat_Unnamed: 14": null,
    "feat_Unnamed: 15": null,
    "feat_Unnamed: 16": null,
    "feat_Unnamed: 17": null
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_eng": "Value(dtype='string', id=None)",
  "feat_spa": "Value(dtype='string', id=None)",
  "source": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)",
  "feat_Unnamed: 4": "Value(dtype='string', id=None)",
  "feat_Unnamed: 5": "Value(dtype='string', id=None)",
  "feat_Unnamed: 6": "Value(dtype='string', id=None)",
  "feat_Unnamed: 7": "Value(dtype='string', id=None)",
  "feat_Unnamed: 8": "Value(dtype='string', id=None)",
  "feat_Unnamed: 9": "Value(dtype='string', id=None)",
  "feat_Unnamed: 10": "Value(dtype='string', id=None)",
  "feat_Unnamed: 11": "Value(dtype='string', id=None)",
  "feat_Unnamed: 12": "Value(dtype='string', id=None)",
  "feat_Unnamed: 13": "Value(dtype='string', id=None)",
  "feat_Unnamed: 14": "Value(dtype='string', id=None)",
  "feat_Unnamed: 15": "Value(dtype='string', id=None)",
  "feat_Unnamed: 16": "Value(dtype='string', id=None)",
  "feat_Unnamed: 17": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2028 |
| valid        | 507 |
