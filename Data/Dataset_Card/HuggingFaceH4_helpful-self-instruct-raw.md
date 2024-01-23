---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: demonstration
    dtype: string
  splits:
  - name: train
    num_bytes: 20412870
    num_examples: 82612
  download_size: 12532431
  dataset_size: 20412870
license: apache-2.0
tags:
- human-feedback
---
# Dataset Card for "helpful-self-instruct-raw"

This dataset is derived from the `finetuning` subset of [Self-Instruct](https://github.com/yizhongw/self-instruct), with some light formatting to remove trailing spaces and `<|endoftext|>` tokens.

