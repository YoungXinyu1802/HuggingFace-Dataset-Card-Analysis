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
    num_bytes: 298298
    num_examples: 1442
  - name: train_all
    num_bytes: 12030615
    num_examples: 53417
  - name: dev_clean
    num_bytes: 293075
    num_examples: 1343
  - name: train
    num_bytes: 1517902
    num_examples: 5919
  - name: test
    num_bytes: 312688
    num_examples: 1517
  - name: dev
    num_bytes: 297598
    num_examples: 1364
  download_size: 6215944
  dataset_size: 14750176
---
# Dataset Card for "trecqa"

TREC-QA dataset for Answer Sentence Selection. The dataset contains 2 additional splits which are `clean` versions of the original development and test sets. `clean` versions contain only questions which have at least a positive and a negative answer candidate.