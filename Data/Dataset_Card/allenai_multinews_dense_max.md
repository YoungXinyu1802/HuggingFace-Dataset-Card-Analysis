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

This is a copy of the [Multi-News](https://huggingface.co/datasets/multi_news) dataset, except the input source documents of its `test` split have been replaced by a __dense__ retriever. The retrieval pipeline used:

- __query__: The `summary` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits
- __retriever__: [`facebook/contriever-msmarco`](https://huggingface.co/facebook/contriever-msmarco) via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"max"`, i.e. the number of documents retrieved, `k`, is set as the maximum number of documents seen across examples in this dataset, in this case `k==10`

Retrieval results on the `train` set:

 Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8661 | 0.6867 | 0.2118 | 0.7966 |

Retrieval results on the `validation` set:

 Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8626 | 0.6859 | 0.2083 | 0.7949 |

Retrieval results on the `test` set:

 Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.8625 | 0.6927 | 0.2096 | 0.7971 |