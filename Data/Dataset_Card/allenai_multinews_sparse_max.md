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
pretty_name: Multi-News
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids:
- news-articles-summarization
paperswithcode_id: multi-news
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

This is a copy of the [Multi-News](https://huggingface.co/datasets/multi_news) dataset, except the input source documents of its `test` split have been replaced by a __sparse__ retriever. The retrieval pipeline used:

- __query__: The `summary` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits
- __retriever__: BM25 via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"max"`, i.e. the number of documents retrieved, `k`, is set as the maximum number of documents seen across examples in this dataset, in this case `k==10`

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8793 | 0.7460 | 0.2213 | 0.8264  |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8748 | 0.7453 | 0.2173 | 0.8232 |

Retrieval results on the `test` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8775 | 0.7480 | 0.2187 | 0.8250 |