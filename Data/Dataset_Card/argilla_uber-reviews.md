---
language:
- en
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
    num_bytes: 2761597
    num_examples: 2347
  download_size: 1691346
  dataset_size: 2761597
---
# Dataset Card for "uber-reviews"

## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/jschne61701/uber-rides-costumer-reviews-dataset
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

Using Python's Beautiful Soup library and Scrappy framework, scraped date, star rating, and comment from all reviews from 2013 - 2019. 

### Languages

english 

### Citation Information

https://www.kaggle.com/datasets/jschne61701/uber-rides-costumer-reviews-dataset
https://www.sitejabber.com/reviews/uber.com
https://www.consumeraffairs.com/travel/uber.html
https://www.kaggle.com/purvank/uber-rider-reviews-dataset

### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.
