---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: led-samsum-dialogsum

## Dataset Description

This dataset has been automatically processed by AutoTrain for project led-samsum-dialogsum.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_Unnamed: 0": 0,
    "feat_id": 0,
    "text": "Amanda: I baked  cookies. Do you want some?\nJerry: Sure!\nAmanda: I'll bring you tomorrow :-)",
    "target": "Amanda baked cookies and will bring Jerry some tomorrow."
  },
  {
    "feat_Unnamed: 0": 1,
    "feat_id": 1,
    "text": "Olivia: Who are you voting for in this election? \nOliver: Liberals as always.\nOlivia: Me too!!\nOliver: Great",
    "target": "Olivia and Olivier are voting for liberals in this election. "
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_Unnamed: 0": "Value(dtype='int64', id=None)",
  "feat_id": "Value(dtype='int64', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 27191 |
| valid        | 1318 |
