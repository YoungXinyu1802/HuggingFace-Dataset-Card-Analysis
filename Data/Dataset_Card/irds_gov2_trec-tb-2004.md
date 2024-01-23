---
pretty_name: '`gov2/trec-tb-2004`'
viewer: false
source_datasets: ['irds/gov2']
task_categories:
- text-retrieval
---

# Dataset Card for `gov2/trec-tb-2004`

The `gov2/trec-tb-2004` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/gov2#gov2/trec-tb-2004).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=58,077

 - For `docs`, use [`irds/gov2`](https://huggingface.co/datasets/irds/gov2)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/gov2_trec-tb-2004', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/gov2_trec-tb-2004', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Clarke2004TrecTerabyte,
  title={Overview of the TREC 2004 Terabyte Track},
  author={Charles Clarke and Nick Craswell and Ian Soboroff},
  booktitle={TREC},
  year={2004}
}
```
