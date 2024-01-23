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
    num_bytes: 4564472
    num_examples: 20864
  - name: test
    num_bytes: 1025142
    num_examples: 4636
  - name: validation
    num_bytes: 510546
    num_examples: 2318
  download_size: 3891711
  dataset_size: 6100160
---
# 人民日报命名实体识别数据集

字段说明

+ `text`: 文本

+ `entities`: 文本中包含的实体

  + `id`: 实体 `id`

  + `entity`: 实体对应的字符串

  + `start_offset`: 实体开始位置

  + `end_offset`: 实体结束位置的下一位

  + `label`: 实体对应的开始位置
  