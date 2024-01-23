---
{}

---
# Filipino Storytelling Books

## Dataset Description
The dataset consists of 148 Filipino storytelling books, 5,005 total sentences, 45,792 total tokens, and 5,646 unique tokens.
This NER model only supports the Filipino language and does not include proper nouns, verbs, adjectives, and adverbs as of the moment
The input must undergo preprocessing. Soon I will upload the code to GitHub for preprocessing the input
To replicate the preprocessed input use this example as a guide
Input: "May umaapoy na bahay "
Preprocessed Input: "apoy bahay"
### Languages

The BCP-47 code for the dataset's language is Filipino.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "tokens": [
      "toot"
    ],
    "tags": [
      3
    ]
  },
  {
    "tokens": [
      "hindi",
      "ako",
      "yun",
      "boltu"
    ],
    "tags": [
      3,
      1,
      3,
      3
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "tokens": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "tags": "Sequence(feature=ClassLabel(num_classes=7, names=['Animals', 'Humans_Body', 'Natural_Environment', 'O', 'Objects', 'Transportation', 'Urban_Environment'], id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 3279 |
| valid        | 1244 |
