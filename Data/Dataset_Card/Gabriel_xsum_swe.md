---
language:
- sv
license:
- mit
size_categories:
- 100K<n<1M
source_datasets:
- https://github.com/huggingface/datasets/tree/master/datasets/xsum
task_categories:
- summarization
- text2text-generation
task_ids: []
tags:
- conditional-text-generation
---

# Dataset Card for Swedish Xsum Dataset
The Swedish xsum dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.
## Dataset Summary
Read about the full details at original English version: https://huggingface.co/datasets/xsum

### Data Fields
- `id`: a string containing the heximal formated SHA1 hash of the url where the story was retrieved from
- `document`: a string containing the body of the news article 
- `summary`: a string containing the summary of the article as written by the article author

### Data Splits
The Swedish xsum dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 204,045                                    |
| Validation    | 11,332                                      |
| Test          | 11,334                                     |
