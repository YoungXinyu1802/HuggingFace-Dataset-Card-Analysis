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
This is the re-split of [CoNaLa](https://conala-corpus.github.io/) dataset. 
For each code snippet in the dev and test set, at least one function is held out from the training set. 
This split aims at testing a code generation model's capacity in generating *unseen* functions
We further make sure that examples from the same StackOverflow post (same `question_id` before `-`) are in the same split. 

### Supported Tasks and Leaderboards
This dataset is used to evaluate code generations.

### Languages
English - Python code.

## Dataset Structure
```python
dataset = load_dataset("neulab/docpromting-conala")
DatasetDict({
    train: Dataset({
        features: ['nl', 'cmd', 'question_id', 'cmd_name', 'oracle_man', 'canonical_cmd'],
        num_rows: 2135
    })
    test: Dataset({
        features: ['nl', 'cmd', 'question_id', 'cmd_name', 'oracle_man', 'canonical_cmd'],
        num_rows: 543
    })
    validation: Dataset({
        features: ['nl', 'cmd', 'question_id', 'cmd_name', 'oracle_man', 'canonical_cmd'],
        num_rows: 201
    })
})
})

code_docs = load_dataset("neulab/docprompting-conala", "docs")
DatasetDict({
    train: Dataset({
        features: ['doc_id', 'doc_content'],
        num_rows: 34003
    })
})
```

### Data Fields
train/dev/test:
- nl: The natural language intent
- cmd: The reference code snippet
- question_id: `x-y`where `x` is the StackOverflow post ID
- oracle_man: The `doc_id` of the functions used in the reference code snippet. The corresponding contents are in `doc` split
- canonical_cmd: The canonical version reference code snippet
 

docs:
- doc_id: the id of a doc
- doc_content: the content of the doc

## Dataset Creation
The dataset was crawled from Stack Overflow, automatically filtered, then curated by annotators. For more details, please refer to the original [paper](https://arxiv.org/pdf/1805.08949.pdf)

### Citation Information

```
@article{zhou2022doccoder,
  title={DocCoder: Generating Code by Retrieving and Reading Docs},
  author={Zhou, Shuyan and Alon, Uri and Xu, Frank F and JIang, Zhengbao and Neubig, Graham},
  journal={arXiv preprint arXiv:2207.05987},
  year={2022}
}
``` 