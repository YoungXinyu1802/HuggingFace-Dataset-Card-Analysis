---
pretty_name: '`wapo/v3/trec-news-2020`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `wapo/v3/trec-news-2020`

The `wapo/v3/trec-news-2020` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/wapo#wapo/v3/trec-news-2020).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=17,764


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/wapo_v3_trec-news-2020', 'queries')
for record in queries:
    record # {'query_id': ..., 'doc_id': ..., 'url': ...}

qrels = load_dataset('irds/wapo_v3_trec-news-2020', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
