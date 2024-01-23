---
dataset_info:
  features:
  - name: nltk_tokens
    sequence: string
  - name: iob_tags
    sequence: string
  - name: input_ids
    sequence: int32
  - name: token_type_ids
    sequence: int8
  - name: attention_mask
    sequence: int8
  - name: labels
    sequence: int64
  splits:
  - name: train
    num_bytes: 2040036
    num_examples: 600
  - name: val
    num_bytes: 662190
    num_examples: 200
  download_size: 353747
  dataset_size: 2702226
---
# Dataset Card for "FoodBase"

Dataset for FoodBase corpus introduced in [this paper](https://academic.oup.com/database/article/doi/10.1093/database/baz121/5611291).

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)