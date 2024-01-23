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

This is a copy of the [Cochrane](https://huggingface.co/datasets/allenai/mslr2022) dataset, except the input source documents of its `validation` split have been replaced by a __sparse__ retriever. The retrieval pipeline used:

- __query__: The `target` field of each example
- __corpus__: The union of all documents in the `train`, `validation` and `test` splits. A document is the concatenation of the `title` and `abstract`.
- __retriever__: BM25 via [PyTerrier](https://pyterrier.readthedocs.io/en/latest/) with default settings
- __top-k strategy__: `"oracle"`, i.e. the number of documents retrieved, `k`, is set as the original number of input documents for each example

Retrieval results on the `train` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.7014 | 0.3841 | 0.3841 | 0.3841 |

Retrieval results on the `validation` set:

| Recall@100 | Rprec | Precision@k | Recall@k |
| ----------- | ----------- | ----------- | ----------- |
| 0.7226 | 0.4023 | 0.4023 | 0.4023 |

Retrieval results on the `test` set:

N/A. Test set is blind so we do not have any queries.