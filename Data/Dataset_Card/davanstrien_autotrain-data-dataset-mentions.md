---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: dataset-mentions

## Dataset Description

This dataset has been automatically processed by AutoTrain for project dataset-mentions.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": " How to use  ```python from transformers import AutoTokenizer, AutoModel  tokenizer = AutoTokenizer.from_pretrained(\"Geotrend/bert-base-en-fr-zh-ja-vi-cased\") model = AutoModel.from_pretrained(\"Geotrend/bert-base-en-fr-zh-ja-vi-cased\")  ```  To generate other smaller versions of multilingual transformers please visit [our Github repo](https://github.com/Geotrend-research/smaller-transformers).  ",
    "target": 0
  },
  {
    "text": " Training hyperparameters  The following hyperparameters were used during training: - learning_rate: 5e-05 - train_batch_size: 24 - eval_batch_size: 24 - seed: 42 - optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08 - lr_scheduler_type: linear - num_epochs: 3  ",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['dataset_mention', 'no_dataset_mention'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 7428 |
| valid        | 1858 |
