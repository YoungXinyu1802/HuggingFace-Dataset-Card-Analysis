---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: procell-expert

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project procell-expert.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "We studied the antitumor activity and toxicity of ZD1694 (tomudex), a specific inhibitor of thymidyl[...]",
    "target": 0
  },
  {
    "text": "Here we provide data that human prostate cancer cell lines express the platelet-type isoform of 12-L[...]",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['accept', 'reject'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 155 |
| valid        | 40 |
