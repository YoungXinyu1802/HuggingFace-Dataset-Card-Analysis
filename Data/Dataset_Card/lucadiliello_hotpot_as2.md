---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 132583963
    num_examples: 489238
  - name: dev
    num_bytes: 6483895
    num_examples: 25295
  - name: test
    num_bytes: 6364224
    num_examples: 24846
  download_size: 55519634
  dataset_size: 145432082
---
# Dataset Card for "hotpot_as2"

Answer Sentence Selection version of the HotpotQA dataset. For more info, check out the original [repository](https://github.com/lucadiliello/answer-selection).