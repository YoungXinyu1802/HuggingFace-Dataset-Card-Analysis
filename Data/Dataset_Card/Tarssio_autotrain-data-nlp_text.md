---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: nlp_text

## Dataset Description

This dataset has been automatically processed by AutoTrain for project nlp_text.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "isso pq ele se considera um enviado de Deus!!!! esse cara \u00e9 pat\u00e9tico!",
    "target": 1
  },
  {
    "text": "#forabolsonaro #forabolsominionsestupidos #lulapresopolitico #amazoniaficabolsonarosai #amazoniafica",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5600 |
| valid        | 1400 |
