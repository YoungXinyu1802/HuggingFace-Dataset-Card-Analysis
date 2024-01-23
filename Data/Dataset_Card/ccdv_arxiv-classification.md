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

**Arxiv Classification: a classification of Arxiv Papers (11 classes).** 

This dataset is intended for long context classification (documents have all > 4k tokens). \
Copied from "Long Document Classification From Local Word Glimpses via Recurrent Attention Learning"
```
@ARTICLE{8675939,
  author={He, Jun and Wang, Liqun and Liu, Liu and Feng, Jiao and Wu, Hao},
  journal={IEEE Access}, 
  title={Long Document Classification From Local Word Glimpses via Recurrent Attention Learning}, 
  year={2019},
  volume={7},
  number={},
  pages={40707-40718},
  doi={10.1109/ACCESS.2019.2907992}
  }
```
 * See: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8675939 
 * See: https://github.com/LiqunW/Long-document-dataset 

It contains 11 slightly unbalanced classes, 33k Arxiv Papers divided into 3 splits: train (28k), val (2.5k) and test (2.5k). 

2 configs:
  * default
  * no_ref, removes references to the class inside the document (eg: [cs.LG] -> [])

Compatible with [run_glue.py](https://github.com/huggingface/transformers/tree/master/examples/pytorch/text-classification) script:
```
export MODEL_NAME=roberta-base
export MAX_SEQ_LENGTH=512

python run_glue.py \
  --model_name_or_path $MODEL_NAME \
  --dataset_name ccdv/arxiv-classification  \
  --do_train \
  --do_eval \
  --max_seq_length $MAX_SEQ_LENGTH \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --learning_rate 2e-5 \
  --num_train_epochs 1 \
  --max_eval_samples 500 \
  --output_dir tmp/arxiv
```