---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- autoevaluate/zero-shot-classification-sample
eval_info:
  task: text_zero_shot_classification
  model: mathemakitten/opt-125m
  metrics: []
  dataset_name: autoevaluate/zero-shot-classification-sample
  dataset_config: autoevaluate--zero-shot-classification-sample
  dataset_split: test
  col_mapping:
    text: text
    classes: classes
    target: target
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Zero-Shot Text Classification
* Model: mathemakitten/opt-125m
* Dataset: autoevaluate/zero-shot-classification-sample
* Config: autoevaluate--zero-shot-classification-sample
* Split: test

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@mathemakitten](https://huggingface.co/mathemakitten) for evaluating this model.