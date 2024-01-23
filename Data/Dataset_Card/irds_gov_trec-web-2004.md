---
pretty_name: '`gov/trec-web-2004`'
viewer: false
source_datasets: ['irds/gov']
task_categories:
- text-retrieval
---

# Dataset Card for `gov/trec-web-2004`

The `gov/trec-web-2004` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/gov#gov/trec-web-2004).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=225
 - `qrels`: (relevance assessments); count=88,566

 - For `docs`, use [`irds/gov`](https://huggingface.co/datasets/irds/gov)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/gov_trec-web-2004', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/gov_trec-web-2004', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Craswell2004TrecWeb,
  title={Overview of the TREC-2004 Web Track},
  author={Nick Craswell and David Hawking},
  booktitle={TREC},
  year={2004}
}
```
