---
language:
- en
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
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
    num_bytes: 227222498
    num_examples: 44898
  download_size: 138350597
  dataset_size: 227222498
---
# Dataset Card for "news-fakenews"

## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=True.csv
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

Can you use this data set to make an algorithm able to determine if an article is fake news or not ?

### Languages

english 

### Citation Information

Acknowledgements

Ahmed H, Traore I, Saad S. “Detecting opinion spams and fake news using text classification”, Journal of Security and Privacy, Volume 1, Issue 1, Wiley, January/February 2018.
Ahmed H, Traore I, Saad S. (2017) “Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques. In: Traore I., Woungang I., Awad A. (eds) Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments. ISDDC 2017. Lecture Notes in Computer Science, vol 10618. Springer, Cham (pp. 127-138).

### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.