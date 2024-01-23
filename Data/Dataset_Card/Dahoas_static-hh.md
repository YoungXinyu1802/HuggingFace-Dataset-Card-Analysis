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
    num_bytes: 143664651
    num_examples: 96256
  - name: test
    num_bytes: 7649255
    num_examples: 5103
  download_size: 90825631
  dataset_size: 151313906
---
Static split of Anthropic's Helpful Harmless dataset. Contains base-online and rejection sampled outputs.