---
dataset_info:
  features:
  - name: code
    dtype: string
  - name: repo_name
    dtype: string
  - name: path
    dtype: string
  - name: language
    dtype: string
  - name: license
    dtype: string
  - name: size
    dtype: int64
  splits:
  - name: train
    num_bytes: 2006765511
    num_examples: 339895
  download_size: 798352074
  dataset_size: 2006765511
task_categories:
- text-generation
tags:
- github-code
size_categories:
- 100K<n<1M
---
# Dataset Card for "github-code-haskell"

This contains just the haskell data in [github-code-clean](https://huggingface.co/datasets/codeparrot/github-code). There are 339k samples with a total download size of 798MB.