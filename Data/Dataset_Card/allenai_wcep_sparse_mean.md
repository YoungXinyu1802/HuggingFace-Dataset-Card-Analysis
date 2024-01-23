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

This is a copy of the [WCEP-10](https://huggingface.co/datasets/ccdv/WCEP-10) dataset, except the input source documents of its `test` split have been replaced by a __sparse__ retriever. The retrieval pipeline used:

- __query__: The `summary` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits
- __retriever__: BM25 via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"mean"`, i.e. the number of documents retrieved, `k`, is set as the mean number of documents seen across examples in this dataset, in this case `k==9`

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8753 | 0.6443 | 0.6196 | 0.6237 |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8706 | 0.6280 | 0.6260 | 0.5989 |

Retrieval results on the `test` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8836 | 0.6658 | 0.6601 | 0.6388 |