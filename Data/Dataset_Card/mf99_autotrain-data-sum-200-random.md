---
language:
- en
task_categories:
- conditional-text-generation
---
# AutoTrain Dataset for project: sum-200-random

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project sum-200-random.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "aen: {Forest hermit to Professor, it's never too late to change. | Dr. Gregory P. Smith | TEDxByronB[...]",
    "target": "Fire, plenty of ferns to sleep on and an endless supply of alcohol. 65"
  },
  {
    "text": "aen: {William Noel: Revealing the lost codex of Archimedes}{from 62% to 72%}{And combinatorics is a [...]",
    "target": "The really astonishing thing though about this manuscript is that we looked at the other manuscripts[...]"
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
| train        | 451280 |
| valid        | 112821 |
