---
language:
- en

---
# AutoTrain Dataset for project: mysheet

## Dataset Description

This dataset has been automatically processed by AutoTrain for project mysheet.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "The term \u201cpseudocode\u201d refers to writing code in a humanly understandable language such as English, and breaking it down to its core concepts.",
    "question": "What is pseudocode?",
    "answers.text": [
      "Pseudocode is breaking down your code in English."
    ],
    "answers.answer_start": [
      33
    ]
  },
  {
    "context": "Python is an interactive programming language designed for API and Machine Learning use.",
    "question": "What is Python?",
    "answers.text": [
      "Python is an interactive programming language."
    ],
    "answers.answer_start": [
      0
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
| train        | 3 |
| valid        | 1 |
