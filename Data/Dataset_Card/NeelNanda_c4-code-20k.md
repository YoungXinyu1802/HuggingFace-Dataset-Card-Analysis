---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 101351288
    num_examples: 20000
  download_size: 42778874
  dataset_size: 101351288
---
# Dataset Card for "c4-code-10k"

10K elements of C4 and 10K elements of code parrot clean (Python code).

Note that these are the datasets used to train my interpretability-friendly models, but is *not* of the correct mixture. Those models were trained on 83% C4 and 17% Python Code (ish) by tokens. This dataset has 10K strings of each, and by tokens is about 22M of code and 5M of C4 (code is longer and harder to compress!)

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)