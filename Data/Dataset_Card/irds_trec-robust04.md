---
pretty_name: '`trec-robust04`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-robust04`

The `trec-robust04` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-robust04#trec-robust04).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=528,155
 - `queries` (i.e., topics); count=250
 - `qrels`: (relevance assessments); count=311,410


This dataset is used by: [`trec-robust04_fold1`](https://huggingface.co/datasets/irds/trec-robust04_fold1), [`trec-robust04_fold2`](https://huggingface.co/datasets/irds/trec-robust04_fold2), [`trec-robust04_fold3`](https://huggingface.co/datasets/irds/trec-robust04_fold3), [`trec-robust04_fold4`](https://huggingface.co/datasets/irds/trec-robust04_fold4), [`trec-robust04_fold5`](https://huggingface.co/datasets/irds/trec-robust04_fold5)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/trec-robust04', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'marked_up_doc': ...}

queries = load_dataset('irds/trec-robust04', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/trec-robust04', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Voorhees2004Robust,
  title={Overview of the TREC 2004 Robust Retrieval Track},
  author={Ellen Voorhees},
  booktitle={TREC},
  year={2004}
}
```
