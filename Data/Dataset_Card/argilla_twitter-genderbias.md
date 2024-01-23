---
language:
- es
license:
- unknown
size_categories:
- 1K<n<10K
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
    dtype: 'null'
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
    num_bytes: 573508
    num_examples: 1914
  download_size: 373847
  dataset_size: 573508
---
# Dataset Card for "twitter-genderbias"

## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/kevinmorgado/gender-bias-spanish
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

This dataset contains more than 1900 labeled Spanish tweets with the category biased or non-biased. This was made for a Hackathon to reduce gender bias on the internet.

- contents: Text
- label:
  - biased
  - non-biased

### Languages

spanish 

### Citation Information

https://www.kaggle.com/datasets/kevinmorgado/gender-bias-spanish

### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.