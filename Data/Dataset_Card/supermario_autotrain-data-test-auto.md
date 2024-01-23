---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: test-auto

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project test-auto.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "aen: {R.C. Sproul: Holy, Holy, Holy}{65%}{85%}{blessing for Isaiah. Here we find a prophet doing som[...]",
    "target": "Instead of announcing God's curse upon the sinful nations who were in rebellion against Him, Isaiah [...]"
  },
  {
    "text": "aen: {Data Connector for Salesforce}{52%}{100%}{to point out is that we do have a SOQL editor availa[...]",
    "target": "This will allow you to customize the query further than is available in our graphic interface. Now t[...]"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 408041 |
| valid        | 102011 |
