---
source_datasets:
- multi_nli
task_categories:
- text-classification
task_ids:
- text-scoring
- semantic-similarity-scoring
---

## Dataset Description

This dataset provides easier accessibility to the original [MNLI dataset](https://huggingface.co/datasets/multi_nli).

We randomly choose 10% of the original `validation_matched` split and use it as the validation split.
The remaining 90% are used for the test split.
The train split remains unchanged.