---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: test

## Dataset Description

This dataset has been automatically processed by AutoTrain for project test.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_textID": "500d5b1751",
    "text": "Almost time to say Good Bye to my twimulations. I`ll miss my tweeps",
    "target": 0
  },
  {
    "feat_textID": "05832fb2c4",
    "text": "did you kno that  is amazing  and i`ve known him since he got twitter and his most tweeted words are `know` `haha` `****`..",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_textID": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['negative', 'positive'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2229 |
| valid        | 558 |
