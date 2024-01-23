---
pretty_name: SQuAD
license: apache-2.0
language:
- en
dataset_info:
  features:
  - name: word
    dtype: string
  - name: icon
    dtype: string
  config_name: svg_icons
  splits:
  - name: train
    num_bytes: 240641
    num_examples: 22
  download_size: 0
  dataset_size: 240641
tags:
- icons
- svgs
size_categories:
- 100M<n<1B
---
# svg_icons
## Dataset Description

- **Homepage:[text_to_icon.kmoz.dev](https://text_to_icon.kmoz.dev)** 
- **Repository: [@KM8Oz/text_to_icon](https://github.com/KM8Oz/text_to_icon)** 

### Dataset Summary

This dataset card aims to be classify svgs icons intos images/label set

## Dataset Structure
   - dataset_info:
   - features:
     - name: word
       - dtype: string
     - name: icon
       - dtype: string