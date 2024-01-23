---
dataset_info:
  features:
  - name: choice
    dtype: int64
  - name: k
    dtype: int64
  - name: k1
    dtype: int64
  - name: n
    dtype: float64
  - name: n1
    dtype: float64
  - name: word
    dtype: string
  - name: word0
    dtype: string
  - name: word1
    dtype: string
  - name: model0
    dtype: string
  - name: model1
    dtype: string
  - name: img0
    dtype: image
  - name: img1
    dtype: image
  splits:
  - name: test
    num_bytes: 3686021.0
    num_examples: 3712
  - name: train
    num_bytes: 14024307.25
    num_examples: 14283
  - name: valid
    num_bytes: 3184961.75
    num_examples: 3237
  download_size: 17726271
  dataset_size: 20895290.0
---
# Dataset Card for "LEGIT-2023"

Label key:
  - 0 or 1: word 0 or 1 is more legible, other unknown
  - 2: both words are equally legible
  - 3: neither word is legible