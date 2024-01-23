---
language:
- sv
license:
- cc-by-sa-3.0
size_categories:
- 10K<n<100K
source_datasets:
- https://github.com/morningmoni/CiteSu
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# Dataset Card for Swedish Wiki_lingua Dataset
The Swedish wiki_lingua dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.

## Dataset Summary
Read about the full details at original Multilingual version: https://huggingface.co/datasets/wiki_lingua

### Data details
- gem_id: the id for the data instance. 
- gem_id_parent: the id for the data instance.
- Document: a string containing the document body.
- Summary: a string containing the summary of the body.

### Data Splits
The Swedish wiki_lingua dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 95,516                                      |
| Validation    | 27,489                                      |
| Test          | 13,340                                      |

