---
task_categories:
- token-classification

---
# AutoTrain Dataset for project: multiconer2-test1

## Dataset Description

This dataset has been automatically processed by AutoTrain for project multiconer2-test1.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tokens": [
      "robert",
      "gottschalk",
      "1939",
      "academy",
      "award",
      "winner",
      "and",
      "founder",
      "of",
      "panavision"
    ],
    "tags": [
      18,
      49,
      62,
      29,
      60,
      62,
      62,
      62,
      62,
      16
    ]
  },
  {
    "tokens": [
      "during",
      "the",
      "reign",
      "of",
      "the",
      "tongzhi",
      "emperor",
      "(",
      "r",
      ".",
      "1861",
      "\u2013",
      "1875",
      ")",
      ":"
    ],
    "tags": [
      62,
      62,
      62,
      62,
      62,
      18,
      49,
      62,
      62,
      62,
      62,
      62,
      62,
      62,
      62
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=63, names=['B-AnatomicalStructure', 'B-ArtWork', 'B-Artist', 'B-Athlete', 'B-CarManufacturer', 'B-Cleric', 'B-Clothing', 'B-Disease', 'B-Drink', 'B-Facility', 'B-Food', 'B-HumanSettlement', 'B-MedicalProcedure', 'B-Medication/Vaccine', 'B-MusicalGRP', 'B-MusicalWork', 'B-ORG', 'B-OtherLOC', 'B-OtherPER', 'B-OtherPROD', 'B-Politician', 'B-PrivateCorp', 'B-PublicCorp', 'B-Scientist', 'B-Software', 'B-SportsGRP', 'B-SportsManager', 'B-Station', 'B-Vehicle', 'B-VisualWork', 'B-WrittenWork', 'I-AnatomicalStructure', 'I-ArtWork', 'I-Artist', 'I-Athlete', 'I-CarManufacturer', 'I-Cleric', 'I-Clothing', 'I-Disease', 'I-Drink', 'I-Facility', 'I-Food', 'I-HumanSettlement', 'I-MedicalProcedure', 'I-Medication/Vaccine', 'I-MusicalGRP', 'I-MusicalWork', 'I-ORG', 'I-OtherLOC', 'I-OtherPER', 'I-OtherPROD', 'I-Politician', 'I-PrivateCorp', 'I-PublicCorp', 'I-Scientist', 'I-Software', 'I-SportsGRP', 'I-SportsManager', 'I-Station', 'I-Vehicle', 'I-VisualWork', 'I-WrittenWork', 'O'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2169 |
| valid        | 829 |
