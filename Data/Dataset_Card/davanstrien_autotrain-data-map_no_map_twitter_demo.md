---
task_categories:
- image-classification

---
# AutoTrain Dataset for project: map_no_map_twitter_demo

## Dataset Description

This dataset has been automatically processed by AutoTrain for project map_no_map_twitter_demo.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "image": "<260x365 RGB PIL image>",
    "target": 1,
    "feat_created_at": "2023-03-08T13:56:12.283125Z",
    "feat_lead_time": 0.768,
    "feat_annotation_id": 23,
    "feat_id": 24,
    "feat_annotator": 1,
    "feat_updated_at": "2023-03-08T13:56:12.283151Z"
  },
  {
    "image": "<639x1298 RGB PIL image>",
    "target": 0,
    "feat_created_at": "2023-03-08T13:59:10.554628Z",
    "feat_lead_time": 0.533,
    "feat_annotation_id": 87,
    "feat_id": 88,
    "feat_annotator": 1,
    "feat_updated_at": "2023-03-08T13:59:10.554650Z"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "image": "Image(decode=True, id=None)",
  "target": "ClassLabel(names=['map', 'no_map'], id=None)",
  "feat_created_at": "Value(dtype='string', id=None)",
  "feat_lead_time": "Value(dtype='float64', id=None)",
  "feat_annotation_id": "Value(dtype='int64', id=None)",
  "feat_id": "Value(dtype='int64', id=None)",
  "feat_annotator": "Value(dtype='int64', id=None)",
  "feat_updated_at": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 72 |
| valid        | 19 |
