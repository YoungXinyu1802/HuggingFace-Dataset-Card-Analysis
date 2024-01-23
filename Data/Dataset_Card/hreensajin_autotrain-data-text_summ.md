---
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: text_summ

## Dataset Description

This dataset has been automatically processed by AutoTrain for project text_summ.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_guid": "klue-nli-v1_train_06870",
    "feat_source": "policy",
    "text": "\ub610\ud55c \ub3c5\ub9bd\ucd9c\ud310\ubb3c \uc81c\uc791 \uc6cc\ud06c\uc20d\uc774\ub791 \uae00\uc4f0\uae30 \uc18c\uc124 \uc4f0\uae30 \uc6cc\ud06c\uc20d\ub3c4 \uc9c4\ud589\ud558\uba70 \uc6d0\ub370\uc774 \uc218\uc5c5\uc744 \ud1b5\ud574 \ub2e4\uc591\ud55c \ud65c\ub3d9\uc744 \ud558\ub294 \uc54c\ucc2c \ubcf5\ud569\uc801\uc778 \uacf5\uac04\uc774\ub2e4.",
    "target": "\ub3c5\ub9bd\ucd9c\ud310\ubb3c \uc81c\uc791 \uc6cc\ud06c\uc20d\uc740 \uc5b8\ub860\uc0ac\uc758 \ud6c4\uc6d0\ud558\uc5d0 \uc9c4\ud589\ub41c\ub2e4.",
    "feat_label": 2
  },
  {
    "feat_guid": "klue-nli-v1_train_02196",
    "feat_source": "wikitree",
    "text": "\uacf5\uc720\ub41c \uc0ac\uc9c4\uc5d0\ub294 \uc790\uc6b1\ud558\uac8c \uc548\uac1c\uc640 \ubbf8\uc138\uba3c\uc9c0\uac00 \ub0b4\ub824\uc549\uc740 \uc0ac\uc9c4\uc774 \uacf5\uc720\ub410\ub2e4.",
    "target": "\uc790\uc6b1\ud55c \uc548\uac1c\uc640 \ubbf8\uc138\uba3c\uc9c0\ub9cc \ub0b4\ub824\uc549\uc558\ub2e4.",
    "feat_label": 2
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_guid": "Value(dtype='string', id=None)",
  "feat_source": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)",
  "feat_label": "ClassLabel(num_classes=3, names=['contradiction', 'entailment', 'neutral'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 22398 |
| valid        | 5600 |
