---
language:
- en
multilinguality:
- monolingual
task_categories:
- text-generation
task_ids: []
tags:
- story-generation
dataset_info:
  features:
  - name: summary
    dtype: string
  - name: story
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 385345341
    num_examples: 427223
  download_size: 213423683
  dataset_size: 385345341
size_categories:
- 100K<n<1M
---
# Story generation

## Dataset Description

- **Homepage:** https://laion.ai/

### Dataset Summary

This dataset contains summaries and stories from [RUCAIBox/Story-Generation](https://huggingface.co/datasets/RUCAIBox/Story-Generation) dataset.

## Dataset Structure

### Data Fields

- `summary`: The summary of the story
- `story`: The story