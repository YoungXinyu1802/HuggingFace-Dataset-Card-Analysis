---
language:
- sv
license:
- cc-by-nc-4.0
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

# Dataset Card for Swedish Citesum Dataset
The Swedish citesum dataset has only been machine-translated to improve downstream fine-tuning on Swedish summarization tasks.

## Dataset Summary
Read about the full details at original English version: https://huggingface.co/datasets/citesum

### Paper
https://arxiv.org/abs/2205.06207

### Authors
Yuning Mao, Ming Zhong, Jiawei Han
University of Illinois Urbana-Champaign
{yuningm2, mingz5, hanj}@illinois.edu

## Data details
- src (string): source text. long description of paper
- tgt (string): target text. tldr of paper
- paper_id (string): unique id for the paper
- title (string): title of the paper
- discipline (dict): 
  - venue (string): Where the paper was published (conference)
  - journal (string): Journal in which the paper was published
  - mag_field_of_study (list[str]): scientific fields that the paper falls under.


### Data Splits
The Swedish xsum dataset follows the same splits as the original English version and has 3 splits: _train_, _validation_, and _test_.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 83,304                                   |
| Validation    | 4,721                                      |
| Test          | 4,921                                     |
