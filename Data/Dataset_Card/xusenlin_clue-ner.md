---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: entities
    list:
    - name: id
      dtype: int64
    - name: entity
      dtype: string
    - name: start_offset
      dtype: int64
    - name: end_offset
      dtype: int64
    - name: label
      dtype: string
  splits:
  - name: train
    num_bytes: 2443356
    num_examples: 10748
  - name: test
    num_bytes: 154492
    num_examples: 1345
  - name: validation
    num_bytes: 309106
    num_examples: 1343
  download_size: 1658426
  dataset_size: 2906954
language:
- zh
tags:
- named entity recognition
- clue
license: apache-2.0
---

# CLUE-NER 命名实体识别数据集

字段说明

+ `text`: 文本

+ `entities`: 文本中包含的实体

  + `id`: 实体 `id`

  + `entity`: 实体对应的字符串

  + `start_offset`: 实体开始位置

  + `end_offset`: 实体结束位置的下一位

  + `label`: 实体对应的开始位置
  