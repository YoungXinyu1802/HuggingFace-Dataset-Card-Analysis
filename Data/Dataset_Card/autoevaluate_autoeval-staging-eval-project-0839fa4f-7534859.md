---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- ag_news
eval_info:
  task: multi_class_classification
  model: nateraw/bert-base-uncased-ag-news
  metrics: []
  dataset_name: ag_news
  dataset_config: default
  dataset_split: test
  col_mapping:
    text: text
    target: label
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Multi-class Text Classification
* Model: nateraw/bert-base-uncased-ag-news
* Dataset: ag_news

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@lewtun](https://huggingface.co/lewtun) for evaluating this model.