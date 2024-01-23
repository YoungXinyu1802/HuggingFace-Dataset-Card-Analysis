---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- acronym_identification
eval_info:
  task: entity_extraction
  model: lewtun/autotrain-acronym-identification-7324788
  metrics: ['angelina-wang/directional_bias_amplification']
  dataset_name: acronym_identification
  dataset_config: default
  dataset_split: validation
  col_mapping:
    tokens: tokens
    tags: labels
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Token Classification
* Model: lewtun/autotrain-acronym-identification-7324788
* Dataset: acronym_identification
* Config: default
* Split: validation

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@wandb.init(project=PROJECT](https://huggingface.co/wandb.init(project=PROJECT) for evaluating this model.