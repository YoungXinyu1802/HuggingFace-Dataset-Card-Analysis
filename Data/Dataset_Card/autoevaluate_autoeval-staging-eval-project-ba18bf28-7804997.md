---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- xtreme
eval_info:
  task: entity_extraction
  model: zhiguoxu/xlm-roberta-base-finetuned-token-clasify
  metrics: []
  dataset_name: xtreme
  dataset_config: PAN-X.en
  dataset_split: validation
  col_mapping:
    tokens: tokens
    tags: ner_tags
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Token Classification
* Model: zhiguoxu/xlm-roberta-base-finetuned-token-clasify
* Dataset: xtreme

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@lewtun](https://huggingface.co/lewtun) for evaluating this model.