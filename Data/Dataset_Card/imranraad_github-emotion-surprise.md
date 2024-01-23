---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: github-emotion-surprise

## Dataset Description

Dataset used in the paper: Imran et al., ["Data Augmentation for Improving Emotion Recognition in Software Engineering Communication"](https://arxiv.org/abs/2208.05573), ASE-2022.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_id": 704844644,
    "text": "This change doesn't affect anything but makes the code more clear. If you look at the line about, `currentUrlTree` is set to `urlAfterRedirects`.",
    "feat_Anger": 0,
    "feat_Love": 0,
    "feat_Fear": 0,
    "feat_Joy": 1,
    "feat_Sadness": 0,
    "target": 0
  },
  {
    "feat_id": 886568180,
    "text": "Thanks very much for your feedback [USER] Your point is totally fair. My intention was to highlight that camelCase or dash-case class names are perfectly fine to use in Angular templates. Most people, especially beginners, do not know that and end up using the `ngClass` directive. Do you think that rewording the alert towards that direction would make sense?",
    "feat_Anger": 0,
    "feat_Love": 1,
    "feat_Fear": 0,
    "feat_Joy": 0,
    "feat_Sadness": 0,
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_id": "Value(dtype='int64', id=None)",
  "text": "Value(dtype='string', id=None)",
  "feat_Anger": "Value(dtype='int64', id=None)",
  "feat_Love": "Value(dtype='int64', id=None)",
  "feat_Fear": "Value(dtype='int64', id=None)",
  "feat_Joy": "Value(dtype='int64', id=None)",
  "feat_Sadness": "Value(dtype='int64', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1600 |
| valid        | 400 |
