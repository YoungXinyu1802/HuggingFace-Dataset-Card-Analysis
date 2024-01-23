---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: nllb_600_ft

## Dataset Description

This dataset has been automatically processed by AutoTrain for project nllb_600_ft.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_id": "772",
    "feat_URL": "https://en.wikivoyage.org/wiki/Apia",
    "feat_domain": "wikivoyage",
    "feat_topic": "Travel",
    "feat_has_image": "0",
    "feat_has_hyperlink": "0",
    "text": "All the ships were sunk, except for one British cruiser. Nearly 200 American and German lives were lost.",
    "target": "\u0628\u0647\u200c\u062c\u0632 \u06cc\u06a9 \u06a9\u0634\u062a\u06cc \u062c\u0646\u06af\u06cc \u0627\u0646\u06af\u0644\u06cc\u0633\u06cc \u0647\u0645\u0647 \u06a9\u0634\u062a\u06cc\u200c\u0647\u0627 \u063a\u0631\u0642 \u0634\u062f\u0646\u062f\u060c \u0648 \u0646\u0632\u062f\u06cc\u06a9 \u0628\u0647 200 \u0646\u0641\u0631 \u0622\u0645\u0631\u06cc\u06a9\u0627\u06cc\u06cc \u0648 \u0622\u0644\u0645\u0627\u0646\u06cc \u062c\u0627\u0646 \u062e\u0648\u062f \u0631\u0627 \u0627\u0632 \u062f\u0633\u062a \u062f\u0627\u062f\u0646\u062f."
  },
  {
    "feat_id": "195",
    "feat_URL": "https://en.wikinews.org/wiki/Mitt_Romney_wins_Iowa_Caucus_by_eight_votes_over_surging_Rick_Santorum",
    "feat_domain": "wikinews",
    "feat_topic": "Politics",
    "feat_has_image": "0",
    "feat_has_hyperlink": "0",
    "text": "Bachmann, who won the Ames Straw Poll in August, decided to end her campaign.",
    "target": "\u0628\u0627\u062e\u0645\u0646\u060c \u06a9\u0647 \u062f\u0631 \u0645\u0627\u0647 \u0622\u06af\u0648\u0633\u062a \u0628\u0631\u0646\u062f\u0647 \u0646\u0638\u0631\u0633\u0646\u062c\u06cc \u0622\u0645\u0633 \u0627\u0633\u062a\u0631\u0627\u0648 \u0634\u062f\u060c \u062a\u0635\u0645\u06cc\u0645 \u06af\u0631\u0641\u062a \u06a9\u0645\u067e\u06cc\u0646 \u062e\u0648\u062f \u0631\u0627 \u062e\u0627\u062a\u0645\u0647 \u062f\u0647\u062f."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_id": "Value(dtype='string', id=None)",
  "feat_URL": "Value(dtype='string', id=None)",
  "feat_domain": "Value(dtype='string', id=None)",
  "feat_topic": "Value(dtype='string', id=None)",
  "feat_has_image": "Value(dtype='string', id=None)",
  "feat_has_hyperlink": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1608 |
| valid        | 402 |
