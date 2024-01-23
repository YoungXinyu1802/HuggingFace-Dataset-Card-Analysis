---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
language:
- code
license:
- mit
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
pretty_name: DocPrompting-CoNaLa
tags:
- code-generation
- doc retrieval
- retrieval augmented generation
---

## Dataset Description
- **Repository:** https://github.com/shuyanzhou/docprompting
- **Paper:** [DocPrompting: Generating Code by Retrieving the Docs](https://arxiv.org/pdf/2207.05987.pdf)

### Dataset Summary
This is the natural language to bash generation dataset we harvested from the English subset of [`tldr`](https://github.com/tldr-pages/tldr)
We split the dataset by bash commands. Every command in the dev and test set is held out from the training set.

### Supported Tasks and Leaderboards
This dataset is used to evaluate code generations.

### Languages
English - Bash

## Dataset Structure
```python
dataset = load_dataset("neulab/tldr")
DatasetDict({
    train: Dataset({
        features: ['question_id', 'nl', 'cmd', 'oracle_man', 'cmd_name', 'tldr_cmd_name', 'manual_exist', 'matching_info'],
        num_rows: 6414
    })
    test: Dataset({
        features: ['question_id', 'nl', 'cmd', 'oracle_man', 'cmd_name', 'tldr_cmd_name', 'manual_exist', 'matching_info'],
        num_rows: 928
    })
    validation: Dataset({
        features: ['question_id', 'nl', 'cmd', 'oracle_man', 'cmd_name', 'tldr_cmd_name', 'manual_exist', 'matching_info'],
        num_rows: 1845
    })
})

code_docs = load_dataset("neulab/docprompting-conala", "docs")
DatasetDict({
    train: Dataset({
        features: ['doc_id', 'doc_content'],
        num_rows: 439064
    })
})
```

### Data Fields
train/dev/test:
- nl: The natural language intent
- cmd: The reference code snippet
- question_id: the unique id of a question
- oracle_man: The `doc_id` of the functions used in the reference code snippet. The corresponding contents are in `doc` split
- cmd_name: the bash command of this code snippet
- tldr_cmd_name: the bash command used in tldr github repo. The `cmd_name` and `tldr_cmd_name` can be different due to naming difference
- manual_exist: whether the manual exists in https://manned.org
- matching_info: each code snippets have multiple tokens, this is the detailed reference doc matching on each token.
 

docs:
- doc_id: the id of a doc
- doc_content: the content of the doc

## Dataset Creation
The dataset was curated from [`tldr`](https://github.com/tldr-pages/tldr). 
The project aims to provide frequent usage of bash commands with natural language intents. 
For more details, please check the repo.

### Citation Information

```
@article{zhou2022doccoder,
  title={DocCoder: Generating Code by Retrieving and Reading Docs},
  author={Zhou, Shuyan and Alon, Uri and Xu, Frank F and Jiang, Zhengbao and Neubig, Graham},
  journal={arXiv preprint arXiv:2207.05987},
  year={2022}
}
``` 