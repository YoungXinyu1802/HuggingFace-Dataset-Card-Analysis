---
pretty_name: '`trec-robust04/fold5`'
viewer: false
source_datasets: ['irds/trec-robust04']
task_categories:
- text-retrieval
---

# Dataset Card for `trec-robust04/fold5`

The `trec-robust04/fold5` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-robust04#trec-robust04/fold5).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=63,841

 - For `docs`, use [`irds/trec-robust04`](https://huggingface.co/datasets/irds/trec-robust04)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-robust04_fold5', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/trec-robust04_fold5', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

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
@inproceedings{Huston2014ACO,
  title={A Comparison of Retrieval Models using Term Dependencies},
  author={Samuel Huston and W. Bruce Croft},
  booktitle={CIKM},
  year={2014}
}
```
