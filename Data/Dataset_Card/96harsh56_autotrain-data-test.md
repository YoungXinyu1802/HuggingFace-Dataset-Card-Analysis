---
{}

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
    "context": "The constitution of Jordan grants its monarch the right to withhold assent to laws passed by its parliament. Article 93 of that document gives the Jordanian sovereign six months to sign or veto any legislation sent to him from the National Assembly; if he vetoes it within that timeframe, the assembly may override his veto by a two-thirds vote of both houses; otherwise, the law does not go into effect (but it may be reconsidered in the next session of the assembly). If the monarch fails to act within six months of the bill being presented to him, it becomes law without his signature.",
    "question": "What happens if the soverign doesn't sign the bill within the six-month time frame?",
    "answers.text": [
      ", it becomes law without his signature"
    ],
    "answers.answer_start": [
      550
    ],
    "feat_id": [
      "572ab241be1ee31400cb818b"
    ],
    "feat_title": [
      "Royal_assent"
    ]
  },
  {
    "context": "The modern Greek theatre was born after the Greek independence, in the early 19th century, and initially was influenced by the Heptanesean theatre and melodrama, such as the Italian opera. The Nobile Teatro di San Giacomo di Corf\u00f9 was the first theatre and opera house of modern Greece and the place where the first Greek opera, Spyridon Xyndas' The Parliamentary Candidate (based on an exclusively Greek libretto) was performed. During the late 19th and early 20th century, the Athenian theatre scene was dominated by revues, musical comedies, operettas and nocturnes and notable playwrights included Spyridon Samaras, Dionysios Lavrangas, Theophrastos Sakellaridis and others.",
    "question": "What was the first Greek opera?",
    "answers.text": [
      "The Parliamentary Candidate"
    ],
    "answers.answer_start": [
      346
    ],
    "feat_id": [
      "57267a75dd62a815002e8683"
    ],
    "feat_title": [
      "Greece"
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
  "answers.answer_start": "Sequence(feature=Value(dtype='int32', id=None), length=-1, id=None)",
  "feat_id": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "feat_title": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 104204 |
| valid        | 26051 |
