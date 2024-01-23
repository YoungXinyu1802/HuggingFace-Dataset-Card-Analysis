---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- deepset/germanquad
eval_info:
  task: extractive_question_answering
  model: deepset/gelectra-base-germanquad
  metrics: []
  dataset_name: deepset/germanquad
  dataset_config: plain_text
  dataset_split: test
  col_mapping:
    context: context
    question: question
    answers-text: answers.text
    answers-answer_start: answers.answer_start
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Question Answering
* Model: deepset/gelectra-base-germanquad
* Dataset: deepset/germanquad
* Config: plain_text
* Split: test

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@sjlree](https://huggingface.co/sjlree) for evaluating this model.