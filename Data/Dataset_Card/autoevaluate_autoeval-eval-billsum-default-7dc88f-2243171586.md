---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- billsum
eval_info:
  task: summarization
  model: Artifact-AI/led_large_16384_billsum_summarization
  metrics: []
  dataset_name: billsum
  dataset_config: default
  dataset_split: test
  col_mapping:
    text: text
    target: summary
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Summarization
* Model: Artifact-AI/led_large_16384_billsum_summarization
* Dataset: billsum
* Config: default
* Split: test

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@Artifact-AI](https://huggingface.co/Artifact-AI) for evaluating this model.