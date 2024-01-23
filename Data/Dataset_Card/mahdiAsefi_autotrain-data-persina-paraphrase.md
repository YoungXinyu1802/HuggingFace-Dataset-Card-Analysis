---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: persina-paraphrase

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project persina-paraphrase.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": " \u0686\u0631\u0627 \u0645\u06cc \u06af\u0648\u06cc\u06cc\u0645 \"\u06cc\u06a9 \u0634\u0644\u0648\u0627\u0631\" \u0627\u06af\u0631 \u0641\u0642\u0637 \u06cc\u06a9 \u0686\u06cc\u0632 \u0627\u0633\u062a\u061f",
    "target": " \u0686\u0631\u0627 \u0645\u06cc \u06af\u0648\u06cc\u06cc\u0645 \u0634\u0644\u0648\u0627\u0631\u061f"
  },
  {
    "text": " \u0647\u0646\u062f \u0631\u0627 \u062f\u0631 \u06cc\u06a9 \u062e\u0637 \u0686\u06af\u0648\u0646\u0647 \u062a\u0639\u0631\u06cc\u0641 \u0645\u06cc \u06a9\u0646\u06cc\u062f\u061f",
    "target": " \u0686\u06af\u0648\u0646\u0647 \u0647\u0646\u062f \u0631\u0627 \u062f\u0631 \u06cc\u06a9 \u062c\u0645\u0644\u0647 \u062a\u0639\u0631\u06cc\u0641 \u06a9\u0646\u06cc\u0645\u061f"
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
| train        | 119410 |
| valid        | 29853 |
