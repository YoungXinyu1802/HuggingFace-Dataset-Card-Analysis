---
type: predictions
tags:
- autotrain
- evaluation
datasets:
- adversarial_qa
eval_info:
  task: extractive_question_answering
  model: osanseviero/distilbert-base-uncased-finetuned-squad-d5716d28
  dataset_name: adversarial_qa
  dataset_config: adversarialQA
  dataset_split: train
  col_mapping:
    context: context
    question: question
    answers-text: answers.text
    answers-answer_start: answers.answer_start
---
# Dataset Card for AutoTrain Evaluator

This repository contains model predictions generated by [AutoTrain](https://huggingface.co/autotrain) for the following task and dataset:

* Task: Question Answering
* Model: osanseviero/distilbert-base-uncased-finetuned-squad-d5716d28
* Dataset: adversarial_qa

To run new evaluation jobs, visit Hugging Face's [automatic evaluation service](https://huggingface.co/spaces/autoevaluate/model-evaluator).

## Contributions

Thanks to [@osanseviero](https://huggingface.co/osanseviero) for evaluating this model.