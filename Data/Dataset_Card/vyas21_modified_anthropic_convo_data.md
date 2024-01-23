---
dataset_info:
  features:
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: human_speaker
    dtype: string
  - name: assistant_speaker
    dtype: string
  splits:
  - name: train
    num_bytes: 370789375
    num_examples: 160800
  - name: test
    num_bytes: 19894559
    num_examples: 8552
  download_size: 223189497
  dataset_size: 390683934
task_categories:
- conversational
tags:
- conversation
- dialogue
- anthropic
pretty_name: modified_anthropic_convo_data
---
# Dataset name: "modified_anthropic_convo_data"

# Dataset Card for Conversational AI Bot


## Dataset Description

- **Homepage:** https://huggingface.co/datasets/Anthropic/hh-rlhf

### Dataset Summary

- This dataset is the augmented version of the same dataset found here https://huggingface.co/datasets/Anthropic/hh-rlhf
- Two new columns have been added called ***human_speaker*** and ***assistant_speaker*** to make it easier to directly use the data for a causal langauage modeling task
- Currently only one pair of conversations have been picked, the dataset will be updated soon

### Contributions

Thanks to https://huggingface.co/datasets/Anthropic/hh-rlhf for adding this dataset.