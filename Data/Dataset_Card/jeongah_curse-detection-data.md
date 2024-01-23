---
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: document
    dtype: string
  - name: ' label'
    dtype: int64
  splits:
  - name: train
    num_bytes: 429333
    num_examples: 4452
  - name: test
    num_bytes: 106670
    num_examples: 1113
  download_size: 364473
  dataset_size: 536003
---
train 문장 4452개, test 문장 1113개로 구성되어 있습니다.
욕설일 경우 spam 값이 1, 욕설에 해당하지 않는 경우 0으로 라벨링 되어 있습니다.

https://github.com/2runo/Curse-detection-data

---
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: sentence
    dtype: string
  - name: ' spam'
    dtype: int64
  splits:
  - name: train
    num_bytes: 429333
    num_examples: 4452
  - name: test
    num_bytes: 106670
    num_examples: 1113
  download_size: 364457
  dataset_size: 536003
---
# Dataset Card for "curse-detection-data"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)