---
dataset_info:
  features:
  - name: label
    dtype: int64
  - name: answer
    dtype: string
  - name: key
    dtype: int64
  - name: question
    dtype: string
  splits:
  - name: test_clean
    num_bytes: 449691
    num_examples: 2341
  - name: dev_clean
    num_bytes: 214886
    num_examples: 1126
  - name: train
    num_bytes: 4017460
    num_examples: 20360
  - name: test
    num_bytes: 1208042
    num_examples: 6165
  - name: dev
    num_bytes: 530358
    num_examples: 2733
  download_size: 3111254
  dataset_size: 6420437
---
# Dataset Card for "wikiqa"

WikiQA dataset for Answer Sentence Selection. The dataset contains 2 additional splits which are `clean` versions of the original development and test sets. `clean` versions contain only questions which have at least a positive and a negative answer candidate.