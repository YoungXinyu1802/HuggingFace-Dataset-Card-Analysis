---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: kor_hate_eval

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project kor_hate_eval.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "(\ud604\uc7ac \ud638\ud154\uc8fc\uc778 \uc2ec\uc815) \uc54418 \ub09c \ub9c8\ub978\ud558\ub298\uc5d0 \ub0a0\ubcbc\ub77d\ub9de\uace0 \ud638\ud154\ub9dd\ud558\uac8c\uc0dd\uacbc\ub294\ub370 \ub204\uad70 \uacc4\uc18d \ucd94\ubaa8\ubc1b\ub124....",
    "target": 1
  },
  {
    "text": "....\ud55c\uad6d\uc801\uc778 \ubbf8\uc778\uc758 \ub300\ud45c\uc801\uc778 \ubd84...\ub108\ubb34\ub098 \uacf1\uace0\uc544\ub984\ub2e4\uc6b4\ubaa8\uc2b5...\uadf8\ubaa8\uc2b5\ub4a4\uc758 \uc2ac\ud514\uc744 \ubbf8\ucc98 \uc54c\uc9c0\ubabb\ud588\ub124\uc694\u3160",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['Default', 'Spoiled'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 7896 |
| valid        | 3770 |
