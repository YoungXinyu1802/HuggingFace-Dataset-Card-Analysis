---
language:
- en

---
# AutoTrain Dataset for project: testjumeee

## Dataset Description

This dataset has been automatically processed by AutoTrain for project testjumeee.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "766",
    "question": "Mass analysis is based on analyzing debitage populations based on their size distribution across specified size grades.",
    "answers.text": [
      "One form of debitage analysis is based on analyzing debitage populations based on their size distribution across specified size grades."
    ],
    "answers.answer_start": [
      0
    ]
  },
  {
    "context": "658",
    "question": "Just watched the first 15 minutes, got bored, skipped to the magic bit, it's funnier as a GIF.",
    "answers.text": [
      "Just watched the first 30 minutes, got bored, skipped to the magic bit, it's funnier as a GIF."
    ],
    "answers.answer_start": [
      1
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "context": "Value(dtype='string', id=None)",
  "question": "Value(dtype='string', id=None)",
  "answers.text": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "answers.answer_start": "Sequence(feature=Value(dtype='int32', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 883 |
| valid        | 221 |
