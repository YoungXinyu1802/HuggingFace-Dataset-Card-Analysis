---
language:
- sv
license:
- mit
size_categories:
- 1M<n<3M
source_datasets:
- https://github.com/huggingface/datasets/tree/master/datasets/gigaword
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# Dataset Card for Swedish Gigaword Dataset
The Swedish gigaword dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.

## Dataset Summary
Read about the full details at original English version: https://huggingface.co/datasets/gigaword

### Data Fields
- `document`: a string containing the shorter body
- `summary`: a string containing the summary of the body

### Data Splits
The Swedish gigaword dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         |  3,700,301                                    |
| Validation    | 189,650                                      |
| Test          | 1,951                                     |

