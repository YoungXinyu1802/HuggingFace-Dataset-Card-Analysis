---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: description
    dtype: string
  - name: url
    dtype: string
  - name: sim_score
    dtype: float64
  - name: name
    dtype: string
  splits:
  - name: train
    num_bytes: 369545620.0
    num_examples: 10000
  download_size: 367769662
  dataset_size: 369545620.0
---
# Dataset Card for "butterflies_names"

Processed version of https://huggingface.co/datasets/huggan/inat_butterflies_top10k -- taking the description and extracting the scientific name in parentheses.