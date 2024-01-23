---
license: apache-2.0
---

# Dataset Card for Dataset Name

## Dataset Description

- **Repository: [Self-Instruct](https://github.com/yizhongw/self-instruct)** 
- **Paper: [Self-Instruct: Aligning Language Model with Self Generated Instructions](https://arxiv.org/abs/2212.10560)** 

### Dataset Summary

This dataset is a copy of yizhongw's data from the github above, note this was created on 24th Jan 2023.

## Dataset Structure
GPT3-finetuning format (prompt + completion)

### Data Fields

Prompt

"Task: [Instruction] Output:"

Completion

"[Answer]<|endoftext|>"


### Data Splits

No splits

## Dataset Creation

### Curation Rationale

Effeciently create a large dataset by using GPT3 to generate the data

### Annotations

The dataset was made and annotated by GPT3


### Dataset Curators

yizhongw

### Licensing Information

Apache 2.0

### Citation Information

I am not the creator of this dataset, please see the GitHub link above.
