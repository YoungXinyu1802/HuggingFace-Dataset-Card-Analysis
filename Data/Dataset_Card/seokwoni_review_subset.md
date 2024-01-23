
dataset_info:
  - features:
    - name: labels
      - dtype: class_label
         - '0': Negative
         - '1': Positive
    - name: Review
      - dtype: string
---
splits: 
  - name: train
    - num_examples: 15000
    - Positive : 50%
    - Negative : 50%
  - name: test
    - num_examples: 1000
    - Positive : 87.7%
    - Negative : 17.3%
    - The ratio of positive and negative data is the same as the ratio of the original data.
---
task_categories:
- text-classification

# Dataset Card for "review_subset"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)