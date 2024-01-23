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
    num_bytes: 203150123
    num_examples: 112052
  - name: test
    num_bytes: 22606646
    num_examples: 12451
  download_size: 136150742
  dataset_size: 225756769
---
# Dataset Card for "full-hh-rlhf"

Anthropic's HH dataset reformatted into prompt, chosen, rejected samples.