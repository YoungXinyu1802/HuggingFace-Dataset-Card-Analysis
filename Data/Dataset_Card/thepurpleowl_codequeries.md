---
annotations_creators:
- expert-generated
language:
- code
language_creators:
- found
multilinguality:
- monolingual
pretty_name: codequeries
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- neural modeling of code
- code question answering
- code semantic understanding
task_categories:
- question-answering
task_ids:
- extractive-qa
license:
- apache-2.0
---

# Dataset Card for CodeQueries

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [How to use](#how-to-use)
  - [Data Splits and Data Fields](#data-splits-and-data-fields)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [Data](https://huggingface.co/datasets/thepurpleowl/codequeries)
- **Repository:** [Code](https://github.com/thepurpleowl/codequeries-benchmark)
- **Paper:** [Learning to Answer Semantic Queries over Code](https://arxiv.org/abs/2209.08372)

### Dataset Summary

CodeQueries is a dataset to evaluate the ability of neural networks to answer semantic queries over code. Given a query and code, a model is expected to identify answer and supporting-fact spans in the code for the query. This is extractive question-answering over code, for questions with a large scope (entire files) and complexity including both single- and multi-hop reasoning. See the [paper]() for more details.

### Supported Tasks and Leaderboards

Extractive question answering for code, semantic understanding of code.

### Languages

The dataset contains code context from `python` files.

## Dataset Structure

### How to Use
The dataset can be directly used with the huggingface datasets package. You can load and iterate through the dataset for the proposed five settings with the following two lines of code:
```python
import datasets

# in addition to `twostep`, the other supported settings are <ideal/file_ideal/prefix>.
ds = datasets.load_dataset("thepurpleowl/codequeries", "twostep", split=datasets.Split.TEST)
print(next(iter(ds)))

#OUTPUT:
{'query_name': 'Unused import',
 'code_file_path': 'rcbops/glance-buildpackage/glance/tests/unit/test_db.py',
 'context_block': {'content': '# vim: tabstop=4 shiftwidth=4 softtabstop=4\n\n# Copyright 2010-2011 OpenStack, LLC\ ...',
                    'metadata': 'root',
                    'header': "['module', '___EOS___']",
                    'index': 0},
 'answer_spans': [{'span': 'from glance.common import context',
                   'start_line': 19,
                   'start_column': 0,
                   'end_line': 19,
                   'end_column': 33}
                 ],
 'supporting_fact_spans': [],
 'example_type': 1,
 'single_hop': False,
 'subtokenized_input_sequence': ['[CLS]_', 'Un', 'used_', 'import_', '[SEP]_', 'module_', '\\u\\u\\uEOS\\u\\u\\u_', '#', ' ', 'vim', ':', ...],
 'label_sequence': [4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...],
 'relevance_label': 1
}
```

### Data Splits and Data Fields
Detailed information on the data splits for proposed settings can be found in the paper.

In general, data splits in all the proposed settings have examples with the following fields -
```
  - query_name (query name to uniquely identify the query)
  - code_file_path (relative source file path w.r.t. ETH Py150 corpus)
  - context_blocks (code blocks as context with metadata)  [`prefix` setting doesn't have this field and `twostep` has `context_block`]
  - answer_spans (answer spans with metadata)
  - supporting_fact_spans (supporting-fact spans with metadata)
  - example_type (1(positive)) or 0(negative)) example type)
  - single_hop (True or False - for query type)
  - subtokenized_input_sequence (example subtokens)  [`prefix` setting has the corresponding token ids]
  - label_sequence (example subtoken labels)
  - relevance_label (0 (not relevant) or 1 (relevant) - relevance label of a block)   [only `twostep` setting has this field]
```


## Dataset Creation

The dataset is created using [ETH Py150 Open dataset](https://github.com/google-research-datasets/eth_py150_open) as source for code contexts. To get semantic queries and corresponding answer/supporting-fact spans in ETH Py150 Open corpus files, CodeQL was used.


## Additional Information
### Licensing Information

The source code repositories used for preparing CodeQueries are based on the [ETH Py150 Open dataset](https://github.com/google-research-datasets/eth_py150_open) and are redistributable under the respective licenses. A Huggingface dataset for ETH Py150 Open is available [here](https://huggingface.co/datasets/eth_py150_open). The labeling prepared and provided by us as part of CodeQueries is released under the Apache-2.0 license.

### Citation Information

```
@misc{https://doi.org/10.48550/arxiv.2209.08372,
  doi = {10.48550/ARXIV.2209.08372},  
  url = {https://arxiv.org/abs/2209.08372},  
  author = {Sahu, Surya Prakash and Mandal, Madhurima and Bharadwaj, Shikhar and Kanade, Aditya and Maniatis, Petros and Shevade, Shirish},  
  keywords = {Software Engineering (cs.SE), Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},  
  title = {Learning to Answer Semantic Queries over Code},  
  publisher = {arXiv},  
  year = {2022},  
  copyright = {Creative Commons Attribution 4.0 International}
}

```
