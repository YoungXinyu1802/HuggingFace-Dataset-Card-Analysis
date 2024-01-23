---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
paperswithcode_id: multi-xscience
pretty_name: Multi-XScience
---

This is a copy of the [Multi-XScience](https://huggingface.co/datasets/multi_x_science_sum) dataset, except the input source documents of its `test` split have been replaced by a __sparse__ retriever. The retrieval pipeline used:

- __query__: The `related_work` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits
- __retriever__: BM25 via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"mean"`, i.e. the number of documents retrieved, `k`, is set as the mean number of documents seen across examples in this dataset, in this case `k==4`

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.5482 | 0.2243 | 0.1578 | 0.2689 |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.5476 | 0.2209 | 0.1592 | 0.2650 |

Retrieval results on the `test` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.548 | 0.2272 | 0.1611 | 0.2704 |