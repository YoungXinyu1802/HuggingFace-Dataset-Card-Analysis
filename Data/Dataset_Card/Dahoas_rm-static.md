---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: response
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 113850006
    num_examples: 76256
  - name: test
    num_bytes: 7649255
    num_examples: 5103
  download_size: 73006535
  dataset_size: 121499261
---
# Dataset Card for "rm-static"

Split of [hh-static](https://huggingface.co/datasets/Dahoas/static-hh) used for training reward models after supervised fine-tuning.