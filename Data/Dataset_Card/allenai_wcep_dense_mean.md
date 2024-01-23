---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- other
multilinguality:
- monolingual
pretty_name: WCEP-10
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- summarization
task_ids:
- news-articles-summarization
paperswithcode_id: wcep
train-eval-index:
- config: default
  task: summarization
  task_id: summarization
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    document: text
    summary: target
  metrics:
    - type: rouge
      name: Rouge
---

This is a copy of the [WCEP-10](https://huggingface.co/datasets/ccdv/WCEP-10) dataset, except the input source documents of its `train`, `validation, and `test` splits have been have been replaced by a __dense__ retriever. The retrieval pipeline used:

- __query__: The `summary` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits
- __retriever__: [`facebook/contriever-msmarco`](https://huggingface.co/facebook/contriever-msmarco) via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"max"`, i.e. the number of documents retrieved, `k`, is set as the maximum number of documents seen across examples in this dataset, in this case `k==9`

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8590 | 0.6490 | 0.6239 | 0.6271 |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8578 | 0.6326 | 0.6301 | 0.6031 |

Retrieval results on the `test` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8678 | 0.6631 | 0.6564 | 0.6338 |