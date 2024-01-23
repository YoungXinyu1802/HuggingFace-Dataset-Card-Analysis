---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: demonstration
    dtype: string
  splits:
  - name: train
    num_bytes: 34540085.04363476
    num_examples: 65499
  download_size: 0
  dataset_size: 34540085.04363476
license: mit
pretty_name: Helpful Raw Anthropic
tags:
- human-feedback
---
# Dataset Card for "helpful-raw-anthropic"

This is a dataset derived from Anthropic's [HH-RLHF data](https://huggingface.co/datasets/Anthropic/hh-rlhf) of instructions and model-generated demonstrations. We combined training splits from the following two subsets:

* `helpful-base`
* `helpful-online`

To convert the multi-turn dialogues into `(instruction, demonstration)` pairs, just the first response from the Assistant was included. This heuristic captures the most obvious answers, but overlooks more complex questions where multiple turns were required to get a helpful response. Some additional filtering is likely required (e.g. defining a minimun length or computing ROUGE-L scores with the instruction/demonstration).