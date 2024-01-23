---
dataset_info:
  features:
  - name: token
    dtype: int64
  - name: Java
    dtype: int64
  - name: JavaScript
    dtype: int64
  - name: Python
    dtype: int64
  splits:
  - name: train
    num_bytes: 1571808
    num_examples: 49119
  download_size: 1165252
  dataset_size: 1571808
---
# Dataset Card for "santacoder-token-usage"

Token usage count per language when tokenizing the `"bigcode/stack-dedup-alt-comments"` dataset with the `santacoder` tokenizer. There are less tokens than in the tokenizer because of vocabulary mismatch between the datasets used to train the tokenizer and the ones that ended up being used to train the model.

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)