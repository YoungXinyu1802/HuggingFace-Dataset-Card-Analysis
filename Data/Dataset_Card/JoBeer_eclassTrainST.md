---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: entailment
    dtype: string
  - name: contradiction
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 327174992
    num_examples: 698880
  - name: eval
    num_bytes: 219201779
    num_examples: 450912
  download_size: 46751846
  dataset_size: 546376771
task_categories:
- sentence-similarity
language:
- en
size_categories:
- 100K<n<1M
---
# Dataset Card for "eclassTrainST"

This NLI-Dataset can be used to fine-tune Models for the task of sentence-simularity. It consists of names and descriptions of pump-properties from the ECLASS-standard.