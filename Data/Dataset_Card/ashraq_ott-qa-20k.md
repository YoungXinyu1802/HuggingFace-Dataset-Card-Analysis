---
dataset_info:
  features:
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: header
    sequence: string
  - name: data
    sequence:
      sequence: string
  - name: section_title
    dtype: string
  - name: section_text
    dtype: string
  - name: uid
    dtype: string
  - name: intro
    dtype: string
  splits:
  - name: train
    num_bytes: 41038376
    num_examples: 20000
  download_size: 23329221
  dataset_size: 41038376
---
# Dataset Card for "ott-qa-20k"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

The data was obtained from [here](https://github.com/wenhuchen/OTT-QA)