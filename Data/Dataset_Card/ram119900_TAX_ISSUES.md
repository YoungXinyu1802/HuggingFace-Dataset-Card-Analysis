---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: tax_issues

## Dataset Description

This dataset has been automatically processed by AutoTrain for project tax_issues.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "How is Inheritance Tax calculated?",
    "target": 10,
    "feat_Unnamed: 2": null,
    "feat_Unnamed: 3": null,
    "feat_Unnamed: 4": null
  },
  {
    "text": "What happens if I work part-time or have multiple jobs as an international student in the UK?",
    "target": 13,
    "feat_Unnamed: 2": null,
    "feat_Unnamed: 3": null,
    "feat_Unnamed: 4": null
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['Question1', 'Question10', 'Question11', 'Question12', 'Question13', 'Question14', 'Question15', 'Question16', 'Question17', 'Question18', 'Question19', 'Question2', 'Question20', 'Question21', 'Question22', 'Question23', 'Question24', 'Question25', 'Question26', 'Question27', 'Question28', 'Question29', 'Question3', 'Question30', 'Question31', 'Question32', 'Question33', 'Question34', 'Question35', 'Question36', 'Question37', 'Question38', 'Question39', 'Question4', 'Question40', 'Question41', 'Question42', 'Question43', 'Question44', 'Question45', 'Question46', 'Question47', 'Question49', 'Question5', 'Question50', 'Question6', 'Question7', 'Question8', 'Question9', 'question48'], id=None)",
  "feat_Unnamed: 2": "Value(dtype='float64', id=None)",
  "feat_Unnamed: 3": "Value(dtype='float64', id=None)",
  "feat_Unnamed: 4": "Value(dtype='float64', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2377 |
| valid        | 622 |
