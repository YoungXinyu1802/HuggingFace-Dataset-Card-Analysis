---
language:
- en
license:
- cc-by-nc-4.0
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids:
- news-articles-summarization
dataset_info:
  features:
  - name: text
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: train
    num_bytes: 221357.01754385966
    num_examples: 100
  - name: test
    num_bytes: 30989.98245614035
    num_examples: 14
  download_size: 106376
  dataset_size: 252347.0
---
# Dataset Card for "news-summary"


## Dataset Description

- **Homepage:** Kaggle Challenge
- **Repository:** https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?select=True.csv
- **Paper:** N.A.
- **Leaderboard:** N.A.
- **Point of Contact:** N.A.

### Dataset Summary

Officially it was supposed to be used for classification but, can you use this data set to summarize news articles?

### Languages

english 

### Citation Information

Acknowledgements

Ahmed H, Traore I, Saad S. “Detecting opinion spams and fake news using text classification”, Journal of Security and Privacy, Volume 1, Issue 1, Wiley, January/February 2018.
Ahmed H, Traore I, Saad S. (2017) “Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques. In: Traore I., Woungang I., Awad A. (eds) Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments. ISDDC 2017. Lecture Notes in Computer Science, vol 10618. Springer, Cham (pp. 127-138).

### Contributions

Thanks to [@davidberenstein1957](https://github.com/davidberenstein1957) for adding this dataset.