---
language:
- es

---
# AutoTrain Dataset for project: karla

## Dataset Description

This dataset has been automatically processed by AutoTrain for project karla.

### Languages

The BCP-47 code for the dataset's language is es.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "Saludos",
    "question": "\u00bfC\u00f3mo est\u00e1s?",
    "answers.text": [
      "Estoy bien, gracias. \u00bfY t\u00fa?"
    ],
    "answers.answer_start": [
      20
    ]
  },
  {
    "context": "M\u00fasica",
    "question": "\u00bfQu\u00e9 tipo de m\u00fasica te gusta?",
    "answers.text": [
      "Me gusta la m\u00fasica rock y pop. \u00bfY a ti?"
    ],
    "answers.answer_start": [
      173
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
| train        | 19 |
| valid        | 5 |
