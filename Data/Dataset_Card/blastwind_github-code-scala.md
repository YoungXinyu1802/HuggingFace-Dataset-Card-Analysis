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
    num_bytes: 4163155675
    num_examples: 817502
  download_size: 1521070059
  dataset_size: 4163155675
task_categories:
- text-generation
size_categories:
- 100K<n<1M
---
# Dataset Card for "github-code-scala"

This contains just the scala data in [github-code-clean](https://huggingface.co/datasets/codeparrot/github-code). There are 817k samples with a total download size of 1.52GB.