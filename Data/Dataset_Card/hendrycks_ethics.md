---
license: mit
language: en
dataset_info:
- config_name: default
  features:
  - name: label
    dtype: int64
  - name: input
    dtype: string
- config_name: commonsense
  features:
  - name: label
    dtype: int32
  - name: input
    dtype: string
  splits:
  - name: train
    num_bytes: 14429921
    num_examples: 13910
  - name: validation
    num_bytes: 3148616
    num_examples: 3885
  - name: test
    num_bytes: 3863068
    num_examples: 3964
  download_size: 21625153
  dataset_size: 21441605
- config_name: deontology
  features:
  - name: label
    dtype: int32
  - name: scenario
    dtype: string
  - name: excuse
    dtype: string
  splits:
  - name: train
    num_bytes: 1854277
    num_examples: 18164
  - name: validation
    num_bytes: 369318
    num_examples: 3596
  - name: test
    num_bytes: 359268
    num_examples: 3536
  download_size: 2384007
  dataset_size: 2582863
- config_name: justice
  features:
  - name: label
    dtype: int32
  - name: scenario
    dtype: string
  splits:
  - name: train
    num_bytes: 2423889
    num_examples: 21791
  - name: validation
    num_bytes: 297935
    num_examples: 2704
  - name: test
    num_bytes: 228008
    num_examples: 2052
  download_size: 2837375
  dataset_size: 2949832
- config_name: utilitarianism
  features:
  - name: baseline
    dtype: string
  - name: less_pleasant
    dtype: string
  splits:
  - name: train
    num_bytes: 2186713
    num_examples: 13737
  - name: validation
    num_bytes: 730391
    num_examples: 4807
  - name: test
    num_bytes: 668429
    num_examples: 4271
  download_size: 3466564
  dataset_size: 3585533
- config_name: virtue
  features:
  - name: label
    dtype: int32
  - name: scenario
    dtype: string
  splits:
  - name: train
    num_bytes: 2605021
    num_examples: 28245
  - name: validation
    num_bytes: 467254
    num_examples: 4975
  - name: test
    num_bytes: 452491
    num_examples: 4780
  download_size: 3364070
  dataset_size: 3524766
tags:
- AI Alignment
---

# Dataset Card for ETHICS

This is the data from [Aligning AI With Shared Human Values](https://arxiv.org/pdf/2008.02275) by Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch,  Jerry Li, Dawn Song, and Jacob Steinhardt, published at ICLR 2021.
For more information, see the [Github Repo](https://github.com/hendrycks/ethics).

## Dataset Summary

This dataset provides ethics-based tasks for evaluating language models for AI alignment.

## Loading Data

To load this data, you can use HuggingFace datasets and the dataloader script.
```
from datasets import load_dataset
load_dataset("hendrycks/ethics", "commonsense")
```

Where `commonsense` is one of the following sections: commonsense, deontology, justice, utilitarianism, and virtue.

### Citation Information
```
@article{hendrycks2021ethics,
  title={Aligning AI With Shared Human Values},
  author={Dan Hendrycks and Collin Burns and Steven Basart and Andrew Critch and Jerry Li and Dawn Song and Jacob Steinhardt},
  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2021}
}
```
