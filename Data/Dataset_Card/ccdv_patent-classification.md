---
language: en
task_categories:
- text-classification
tags:
- long context
task_ids:
- multi-class-classification
- topic-classification
size_categories: 10K<n<100K
---

**Patent Classification: a classification of Patents and abstracts (9 classes).** 

This dataset is intended for long context classification (non abstract documents are longer that 512 tokens). \
Data are sampled from "BIGPATENT: A Large-Scale Dataset for Abstractive and Coherent Summarization." by Eva Sharma, Chen Li and Lu Wang 
 * See: https://aclanthology.org/P19-1212.pdf 
 * See: https://evasharma.github.io/bigpatent/

It contains 9 unbalanced classes, 35k Patents and abstracts divided into 3 splits: train (25k), val (5k) and test (5k). 

**Note that documents are uncased and space separated (by authors)**

Compatible with [run_glue.py](https://github.com/huggingface/transformers/tree/master/examples/pytorch/text-classification) script:
```
export MODEL_NAME=roberta-base
export MAX_SEQ_LENGTH=512

python run_glue.py \
  --model_name_or_path $MODEL_NAME \
  --dataset_name ccdv/patent-classification  \
  --do_train \
  --do_eval \
  --max_seq_length $MAX_SEQ_LENGTH \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --learning_rate 2e-5 \
  --num_train_epochs 1 \
  --max_eval_samples 500 \
  --output_dir tmp/patent
```