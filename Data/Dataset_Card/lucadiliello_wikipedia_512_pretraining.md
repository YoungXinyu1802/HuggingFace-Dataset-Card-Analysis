---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 9828026640.785877
    num_examples: 6699666
  - name: dev
    num_bytes: 146694277.60706097
    num_examples: 100000
  - name: test
    num_bytes: 146694277.60706097
    num_examples: 100000
  download_size: 6454536577
  dataset_size: 10121415196
language:
- en
pretty_name: Wikipedia preprocessed for 512 tokens pretraining.
size_categories:
- 1M<n<10M
---
# Dataset Card for "wikipedia_512_pretraining"

Wikipedia preprocessed for pretraining of models. Each sample in the dataset has an average tokenized length of 512 tokens.