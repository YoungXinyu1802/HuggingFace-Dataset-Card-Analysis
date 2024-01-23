---
dataset_info:
  features:
  - name: did
    dtype: int64
  - name: query
    dtype: string
  - name: name
    dtype: string
  - name: duplicate_id
    dtype: int64
  - name: metalabel
    dtype: int64
  splits:
  - name: train
    num_bytes: 147176
    num_examples: 1040
  - name: eval
    num_bytes: 100846
    num_examples: 671
  download_size: 113268
  dataset_size: 248022
task_categories:
- sentence-similarity
language:
- en
size_categories:
- 1K<n<10K
---
# Dataset Card for "eclassQuery"

This Dataset consists of paraphrases of ECLASS-standard pump-properties. It can be used to evaluate models on the task of matching these paraphrases to the actual ECLASS-standard pump-properties based on their semantics.