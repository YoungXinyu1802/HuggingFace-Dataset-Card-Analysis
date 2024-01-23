---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: diffusion-emotion-facial-expression-recognition

## Dataset Description

This dataset has been automatically processed by AutoTrain for project diffusion-emotion-facial-expression-recognition.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<224x224 RGB PIL image>",
    "target": 3
  },
  {
    "image": "<224x224 RGB PIL image>",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1028 |
| valid        | 261 |
