---
dataset_info:
  features:
  - name: INSTRUCTION
    dtype: string
  - name: RESPONSE
    dtype: string
  - name: SOURCE
    dtype: string
  splits:
  - name: train
    num_bytes: 7600684
    num_examples: 4747
  download_size: 3325663
  dataset_size: 7600684
---
# Dataset Card for Recipes dialogue

Derrived from the Kaggle dataset [Recipes from Tasty](https://www.kaggle.com/datasets/zeeenb/recipes-from-tasty), we turn the recipe ingredients and instructions into chat dialogue using a preset list of user prompt templates.

Dataset license: CC0: Public Domain.