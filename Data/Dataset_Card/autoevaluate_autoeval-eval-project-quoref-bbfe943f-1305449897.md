---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- quoref
eval_info:
  task: extractive_question_answering
  model: nbroad/rob-base-gc1
  metrics: []
  dataset_name: quoref
  dataset_config: default
  dataset_split: validation
  col_mapping:
    context: context
    question: question
    answers-text: answers.text
    answers-answer_start: answers.answer_start
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Question Answering
* Model: nbroad/rob-base-gc1
* Dataset: quoref
* Config: default
* Split: validation

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@nbroad](https://huggingface.co/nbroad) for evaluating this model.