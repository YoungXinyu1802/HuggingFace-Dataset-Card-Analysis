---
task_categories:
- summarization

---
# AutoTrain Dataset for project: flan-xl-conversation

## Dataset Description

This dataset has been automatically processed by AutoTrain for project flan-xl-conversation.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "What is the largest insect in the world?",
    "target": "The largest insect in the world is the Goliath Beetle."
  },
  {
    "text": "What is the largest amphibian in the world?",
    "target": "The largest amphibian in the world is the Chinese giant salamander."
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
| train        | 158 |
| valid        | 40 |
