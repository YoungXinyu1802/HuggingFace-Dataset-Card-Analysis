---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: question_id
    dtype: int64
  - name: question_body
    dtype: string
  - name: question_score
    dtype: int64
  - name: question_date
    dtype: string
  - name: answer_id
    dtype: int64
  - name: answer_body
    dtype: string
  - name: answer_score
    dtype: int64
  - name: answer_date
    dtype: string
  - name: tags
    sequence: string
  splits:
  - name: train
    num_bytes: 2142466142
    num_examples: 987122
  download_size: 829547986
  dataset_size: 2142466142
task_categories:
- question-answering
language:
- en
size_categories:
- 100K<n<1M
---
# Dataset Card for "stackoverflow_python"

[More InComing](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


### Dataset Summary

This dataset comes originally from [kaggle](https://www.kaggle.com/stackoverflow/pythonquestions). 
It was originally split into three tables (CSV files) (Questions, Answers, and Tags)
now merged into a single table. Each row corresponds to a pair (question-answer) and 
their associated tags. This might be useful for open-domain question-answering tasks. 

## Additional information

### License

All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.