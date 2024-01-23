---
license: apache-2.0
dataset_info:
- config_name: instruction_tuning
  features:
  - name: text
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 29975565
    num_examples: 41685
  - name: test
    num_bytes: 3298059
    num_examples: 4632
  download_size: 18425612
  dataset_size: 33273624
- config_name: reward_modelling
  features:
  - name: text
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 25274204
    num_examples: 41685
  - name: test
    num_bytes: 2777314
    num_examples: 4632
  download_size: 15636566
  dataset_size: 28051518
- config_name: ppo
  features:
  - name: prompt
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 50787070
    num_examples: 83371
  - name: test
    num_bytes: 5715727
    num_examples: 9264
  download_size: 31461165
  dataset_size: 56502797
- config_name: reward_modeling
  features:
  - name: prompt
    dtype: string
  - name: meta
    struct:
    - name: source
      dtype: string
    - name: config
      dtype: string
  splits:
  - name: train
    num_bytes: 25274204
    num_examples: 41685
  - name: test
    num_bytes: 2777314
    num_examples: 4632
  download_size: 15636838
  dataset_size: 28051518
task_categories:
- conversational
- text-generation
language:
- en
tags:
- human-feedback
- instruct
- reward-modeling
pretty_name: Instruct Me
---

# Dataset card for Instruct Me

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** Lewis Tunstall

### Dataset summary

Instruct Me is a dataset of prompts and instruction dialogues between a human user and AI assistant. The prompts are derived from (prompt, completion) pairs in the [Helpful Instructions dataset](https://huggingface.co/datasets/HuggingFaceH4/helpful_instructions). The goal is to train a language model to that is "chatty" and can answer the kind of questions or tasks a human user might instruct an AI assistant to perform.

### Supported Tasks and Leaderboard

We provide 3 configs that can be used for training RLHF models:

#### instruction_tuning

Single-turn user/bot dialogues for instruction tuning.

#### reward_modeling

Prompts to generate model completions and collect human preference data

#### ppo

Prompts to generate model completions for optimization of the instruction-tuned model with techniques like PPO.

### Changelog

* March 6, 2023: `v1.1.0` release. Changed the `text` columns for the `reward_modeling` and `ppo` configs to `prompt` for consistency with our dataset schemas elsewhere.
* March 5, 2023: `v1.0.0` release.