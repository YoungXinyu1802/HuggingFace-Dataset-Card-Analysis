---
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: text
    dtype: string
  splits:
  - name: development
    num_bytes: 6030729
    num_examples: 59
  - name: test
    num_bytes: 8229224
    num_examples: 71
  - name: train
    num_bytes: 29128904
    num_examples: 300
  download_size: 43004020
  dataset_size: 43388857
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
language:
- gos
---
# Gronings transcribed speech

Demonstration dataset with Gronings transcribed speech based on the dataset released by [San et al. (2021)](https://github.com/fauxneticien/qbe-std_feats_eval).

For more information see the corresponding [ASRU 2021 paper](https://ieeexplore.ieee.org/abstract/document/9688301).