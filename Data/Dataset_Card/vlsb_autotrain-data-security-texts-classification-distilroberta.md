---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: security-texts-classification-distilroberta

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project security-texts-classification-distilroberta.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Netgear launches Bug Bounty Program for Hacker; Offering up to $15,000 in Rewards It might be the ea[...]",
    "target": 0
  },
  {
    "text": "Popular Malware Families Using 'Process Doppelg\u00e4nging' to Evade Detection The fileless code injectio[...]",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['irrelevant', 'relevant'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 780 |
| valid        | 196 |
