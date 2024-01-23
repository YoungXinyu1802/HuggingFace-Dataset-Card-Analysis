---
language:
- en
license:
- unknown
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- sentiment-classification
- sentiment-analysis
dataset_info:
  features:
  - name: text
    dtype: string
  - name: inputs
    struct:
    - name: text
      dtype: string
  - name: prediction
    list:
    - name: label
      dtype: string
    - name: score
      dtype: float64
  - name: prediction_agent
    dtype: string
  - name: annotation
    dtype: 'null'
  - name: annotation_agent
    dtype: 'null'
  - name: multi_label
    dtype: bool
  - name: explanation
    dtype: 'null'
  - name: id
    dtype: string
  - name: metadata
    struct:
    - name: location
      dtype: string
    - name: screen_name
      dtype: int64
    - name: split
      dtype: string
    - name: user_name
      dtype: int64
  - name: status
    dtype: string
  - name: event_timestamp
    dtype: timestamp[us]
  - name: metrics
    struct:
    - name: text_length
      dtype: int64
  splits:
  - name: train
    num_bytes: 25394534
    num_examples: 44955
  download_size: 15712627
  dataset_size: 25394534
---
# Dataset Card for "twitter-coronavirus"

## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

Perform Text Classification on the data. The tweets have been pulled from Twitter and manual tagging has been done then.
The names and usernames have been given codes to avoid any privacy concerns.

Columns:
1) Location
2) Tweet At
3) Original Tweet
4) Label
  - Extremely Negative
  - Negative
  - Neutral
  - Positive
  - Extremely Positive

### Languages

english 

### Citation Information

https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification


### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.