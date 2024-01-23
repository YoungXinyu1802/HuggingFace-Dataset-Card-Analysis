---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- cnn_dailymail
eval_info:
  task: summarization
  model: sysresearch101/t5-large-finetuned-xsum-cnn
  metrics: []
  dataset_name: cnn_dailymail
  dataset_config: 3.0.0
  dataset_split: train
  col_mapping:
    text: article
    target: highlights
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Summarization
* Model: sysresearch101/t5-large-finetuned-xsum-cnn
* Dataset: cnn_dailymail
* Config: 3.0.0
* Split: train

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@sysresearch101](https://huggingface.co/sysresearch101) for evaluating this model.