---
pretty_name: '`vaswani`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `vaswani`

The `vaswani` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/vaswani#vaswani).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=11,429
 - `queries` (i.e., topics); count=93
 - `qrels`: (relevance assessments); count=2,083


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/vaswani', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

queries = load_dataset('irds/vaswani', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/vaswani', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
