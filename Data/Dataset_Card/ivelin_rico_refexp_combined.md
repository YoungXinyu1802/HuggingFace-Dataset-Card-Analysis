---
license: cc
task_categories:
- question-answering
language:
- en
tags:
- ui refexp
pretty_name: UI RefExp Combined
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: image
    dtype: image
  - name: image_id
    dtype: string
  - name: prompt
    dtype: string
  - name: target_bounding_box
    struct:
    - name: xmax
      dtype: float64
    - name: xmin
      dtype: float64
    - name: ymax
      dtype: float64
    - name: ymin
      dtype: float64
  splits:
  - name: train
    num_bytes: 42127199077.08
    num_examples: 390084
  - name: validation
    num_bytes: 409042403.17
    num_examples: 3191
  - name: test
    num_bytes: 456349755.528
    num_examples: 3912
  download_size: 27184189035
  dataset_size: 42992591235.778
---
# Dataset Card for "rico_refexp_combined"

This dataset combines the crowdsourced RICO RefExp prompts from the [UIBert dataset](https://huggingface.co/datasets/ivelin/rico_sca_refexp_synthetic) and the synthetically generated prompts from the [seq2act dataset](https://huggingface.co/datasets/ivelin/rico_sca_refexp_synthetic).