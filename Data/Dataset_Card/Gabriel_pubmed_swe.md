---
language:
- sv
license:
- other
size_categories:
- 10K<n<100K
source_datasets:
- https://github.com/huggingface/datasets/tree/master/datasets/pubmed
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---


# Dataset Card for Swedish pubmed Dataset
The Swedish pubmed dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.

## Dataset Summary
Read about the full details at original English version: https://huggingface.co/datasets/pubmed

### Data Fields
- `document`: a string containing the body of the paper
- `summary`: a string containing the abstract of the paper

### Data Splits
The Swedish pubmed dataset follows the same splits as the original English version and has 1 splits: _train_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         |  90,000                                    |
