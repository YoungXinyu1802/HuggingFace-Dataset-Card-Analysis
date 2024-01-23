---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: id2
    dtype: int64
  - name: title
    dtype: string
  - name: text_plain
    dtype: string
  - name: text_html
    dtype: string
  - name: author
    dtype: string
  - name: negative_votes
    dtype: int32
  - name: positive_votes
    dtype: int32
  - name: quality
    dtype: int8
  - name: views
    dtype: uint64
  - name: votes
    dtype: int32
  - name: approved_answer
    dtype: string
  - name: timestamp
    dtype: uint64
  - name: tags
    sequence: string
  - name: answers
    sequence:
    - name: id
      dtype: string
    - name: id2
      dtype: int64
    - name: text_plain
      dtype: string
    - name: text_html
      dtype: string
    - name: author
      dtype: string
    - name: negative_votes
      dtype: int32
    - name: positive_votes
      dtype: int32
    - name: votes
      dtype: int32
    - name: quality
      dtype: int8
    - name: views
      dtype: uint64
    - name: reposts
      dtype: int32
    - name: timestamp
      dtype: uint64
  splits:
  - name: train
    num_bytes: 5468460217
    num_examples: 1297670
  download_size: 1130317937
  dataset_size: 5468460217
---

Based on https://huggingface.co/datasets/its5Q/yandex-q, parsed full.jsonl.gz
