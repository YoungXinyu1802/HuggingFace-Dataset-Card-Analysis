---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- instruct
- human-feedback
pretty_name: Helpful Instructions
dataset_info:
- config_name: self_instruct
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 24378246
    num_examples: 82612
  download_size: 12589487
  dataset_size: 24378246
- config_name: super_natural_instructions
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 43352923
    num_examples: 50000
  download_size: 22605900
  dataset_size: 43352923
- config_name: prompt_source
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 59843768
    num_examples: 52657
  download_size: 23607134
  dataset_size: 59843768
- config_name: all
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 127574937
    num_examples: 185269
  download_size: 58901460
  dataset_size: 127574937
---

# Dataset Card for Helpful Instructions

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact: Lewis Tunstall**

### Dataset Summary

Helpful Instructions is a dataset of `(instruction, completion)` pairs that are derived from public datasets. As the name suggests, it focuses on instructions that are "helpful", i.e. the kind of questions or tasks a human user might instruct an AI assistant to perform. You can load the dataset as follows:

```python
from datasets import load_dataset

# Load all subsets
helpful_instructions = load_dataset("HuggingFaceH4/helpful_instructions", name="all")

# Load a single subset
helpful_instructions_subset = load_dataset("HuggingFaceH4/helpful_instructions", name="self_instruct")
```


### Supported Tasks and Leaderboards

This dataset can be used to fine-tune pretrained language models to follow instructions.

### Changelog

* March 5, 2023: `v1.0.0` release, with subsets from `HuggingFaceH4/self_instruct` (`self_instruct`, `super_natural_instructions`, `prompt_source`)