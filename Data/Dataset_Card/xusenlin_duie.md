---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: spo_list
    list:
    - name: predicate
      dtype: string
    - name: object_type
      dtype: string
    - name: subject_type
      dtype: string
    - name: object
      dtype: string
    - name: subject
      dtype: string
  splits:
  - name: train
    num_bytes: 51849478
    num_examples: 172983
  - name: validation
    num_bytes: 6512116
    num_examples: 21626
  download_size: 32568292
  dataset_size: 58361594
---
# DuIE 关系抽取数据集

字段说明

+ `text`: 文本

+ `spo_list`: 文本中包含的关系三元组

  + `subject`: 头实体（主语）

  + `subject_type`: 头实体（主语）的类型

  + `object`: 尾实体（主语）

  + `object_type`: 尾实体（主语）的类型

  + `predicate`: 关系
 