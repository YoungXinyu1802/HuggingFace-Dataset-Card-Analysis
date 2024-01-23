---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- pn_summary
eval_info:
  task: summarization
  model: google/pegasus-large
  metrics: []
  dataset_name: pn_summary
  dataset_config: 1.0.0
  dataset_split: train
  col_mapping:
    text: article
    target: summary
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Summarization
* Model: google/pegasus-large
* Dataset: pn_summary
* Config: 1.0.0
* Split: train

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@marsraker09](https://huggingface.co/marsraker09) for evaluating this model.