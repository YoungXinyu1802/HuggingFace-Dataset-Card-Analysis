---
{}

---
# AutoTrain Dataset for project: MedicalTokenClassification

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project MedicalTokenClassification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_id": "13104",
    "tokens": [
      "Jackie",
      "Frank"
    ],
    "feat_pos_tags": [
      21,
      21
    ],
    "feat_chunk_tags": [
      5,
      16
    ],
    "tags": [
      3,
      7
    ]
  },
  {
    "feat_id": "9297",
    "tokens": [
      "U.S.",
      "lauds",
      "Russian-Chechen",
      "deal",
      "."
    ],
    "feat_pos_tags": [
      21,
      20,
      15,
      20,
      7
    ],
    "feat_chunk_tags": [
      5,
      16,
      16,
      16,
      22
    ],
    "tags": [
      0,
      8,
      1,
      8,
      8
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_id": "Value(dtype='string', id=None)",
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "feat_pos_tags": "Sequence(feature=ClassLabel(num_classes=47, names=['\"', '#', '$', \"''\", '(', ')', ',', '.', ':', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'NN|SYM', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', '``'], id=None), length=-1, id=None)",
  "feat_chunk_tags": "Sequence(feature=ClassLabel(num_classes=23, names=['B-ADJP', 'B-ADVP', 'B-CONJP', 'B-INTJ', 'B-LST', 'B-NP', 'B-PP', 'B-PRT', 'B-SBAR', 'B-UCP', 'B-VP', 'I-ADJP', 'I-ADVP', 'I-CONJP', 'I-INTJ', 'I-LST', 'I-NP', 'I-PP', 'I-PRT', 'I-SBAR', 'I-UCP', 'I-VP', 'O'], id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=9, names=['B-LOC', 'B-MISC', 'B-ORG', 'B-PER', 'I-LOC', 'I-MISC', 'I-ORG', 'I-PER', 'O'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 10014 |
| valid        | 4028 |
