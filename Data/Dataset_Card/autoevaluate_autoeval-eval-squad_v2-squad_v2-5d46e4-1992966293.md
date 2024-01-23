---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- squad_v2
eval_info:
  task: extractive_question_answering
  model: deepset/electra-base-squad2
  metrics: ['accuracy', 'bleu', 'precision', 'recall', 'rouge']
  dataset_name: squad_v2
  dataset_config: squad_v2
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
* Model: deepset/electra-base-squad2
* Dataset: squad_v2
* Config: squad_v2
* Split: validation

To run new evaluation jobs, visit Hugging Face's [automatic model evaluator](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@anchal](https://huggingface.co/anchal) for evaluating this model.