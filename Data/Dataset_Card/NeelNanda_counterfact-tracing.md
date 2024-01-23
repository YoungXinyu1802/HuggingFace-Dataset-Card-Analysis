---
dataset_info:
  features:
  - name: relation
    dtype: string
  - name: relation_prefix
    dtype: string
  - name: relation_suffix
    dtype: string
  - name: prompt
    dtype: string
  - name: relation_id
    dtype: string
  - name: target_false_id
    dtype: string
  - name: target_true_id
    dtype: string
  - name: target_true
    dtype: string
  - name: target_false
    dtype: string
  - name: subject
    dtype: string
  splits:
  - name: train
    num_bytes: 3400668
    num_examples: 21919
  download_size: 1109314
  dataset_size: 3400668
---
# Dataset Card for "counterfact-tracing"

This is adapted from the counterfact dataset from the excellent [ROME paper](https://rome.baulab.info/) from David Bau and Kevin Meng.

This is a dataset of 21919 factual relations, formatted as `data["prompt"]==f"{data['relation_prefix']}{data['subject']}{data['relation_suffix']}"`. Each has two responses `data["target_true"]` and `data["target_false"]` which is intended to go immediately after the prompt.

The dataset was originally designed for memory editing in models. I made this for a research project doing mechanistic interpretability of how models recall factual knowledge, building on their causal tracing technique, and so stripped their data down to the information relevant to causal tracing. I also prepended spaces where relevant so that the subject and targets can be properly tokenized as is (spaces are always prepended to targets, and are prepended to subjects unless the subject is at the start of a sentence). 

Each fact has both a true and false target. I recommend measuring the logit *difference* between the true and false target (at least, if it's a single token target!), so as to control for eg the parts of the model which identify that it's supposed to be giving a fact of this type at all. (Idea inspired by the excellent [Interpretability In the Wild](https://arxiv.org/abs/2211.00593) paper). 