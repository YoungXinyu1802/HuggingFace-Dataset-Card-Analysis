---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-MS^2
- extended|other-Cochrane
task_categories:
- summarization
- text2text-generation
paperswithcode_id: multi-document-summarization
pretty_name: MSLR Shared Task
---

This is a copy of the [MS^2](https://huggingface.co/datasets/allenai/mslr2022) dataset, except the input source documents of its `train`, `validation` and `test` splits have been replaced by a __dense__ retriever. The retrieval pipeline used:

- __query__: The `background` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits. A document is the concatenation of the `title` and `abstract`.
- __retriever__: [`facebook/contriever-msmarco`](https://huggingface.co/facebook/contriever-msmarco) via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"max"`, i.e. the number of documents retrieved, `k`, is set as the maximum number of documents seen across examples in this dataset, in this case `k==17`

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.4764 | 0.2395 | 0.2271 | 0.2418 |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.4364 | 0.2125 | 0.2131 | 0.2074 |

Retrieval results on the `test` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.4481 | 0.2224 | 0.2254 | 0.2100 |