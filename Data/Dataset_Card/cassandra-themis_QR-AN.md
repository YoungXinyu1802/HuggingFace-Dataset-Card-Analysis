---
language:
- fr
size_categories: 10K<n<100K
task_categories:
- summarization
- text-classification
- text-generation
task_ids:
- multi-class-classification
- topic-classification
tags:
- conditional-text-generation
---

**QR-AN Dataset: a classification and generation dataset of french Parliament questions-answers.** 

This is a dataset for theme/topic classification, made of questions and answers from https://www2.assemblee-nationale.fr/recherche/resultats_questions . \

It contains 188 unbalanced classes, 80k questions-answers divided into 3 splits: train (60k), val (10k) and test (10k). \

Can be used for generation with 'qran_generation'
This dataset is compatible with the [`run_summarization.py`](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script from Transformers if you add this line to the `summarization_name_mapping` variable:
```python
"ccdv/cass-summarization": ("question", "answer")
```

Compatible with [run_glue.py](https://github.com/huggingface/transformers/tree/master/examples/pytorch/text-classification) script:
```
export MODEL_NAME=camembert-base
export MAX_SEQ_LENGTH=512

python run_glue.py \
  --model_name_or_path $MODEL_NAME \
  --dataset_name cassandra-themis/QR-AN  \
  --do_train \
  --do_eval \
  --max_seq_length $MAX_SEQ_LENGTH \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --learning_rate 2e-5 \
  --num_train_epochs 1 \
  --max_eval_samples 500 \
  --output_dir tmp/QR-AN
```