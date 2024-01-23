---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: source
    dtype: string
  - name: Rationale
    dtype: string
  - name: annotated_formula
    dtype: string
  - name: linear_formula
    dtype: string
  splits:
  - name: train
    num_bytes: 1114848
    num_examples: 2880
  download_size: 543796
  dataset_size: 1114848
---
# Dataset Card for "minimath"
The objective of `minimath` is to evaluate the mathematical capability of language model in a quick while diverse setting.  
The dataset is composed of sampling from the below dataset:  
https://huggingface.co/datasets/math_dataset  
https://huggingface.co/datasets/math_qa  
https://huggingface.co/datasets/competition_math  
https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_math_jsonl  
https://huggingface.co/datasets/qwedsacf/grade-school-math-instructions  



[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)