---
license: mit
---
train-eval-index:
- config: default
  task: token-classification
  task_id: entity_extraction
  splits:
    eval_split: test
  col_mapping:
    tokens: tokens
    labels: tags