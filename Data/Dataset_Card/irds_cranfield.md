---
pretty_name: '`cranfield`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `cranfield`

The `cranfield` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/cranfield#cranfield).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,400
 - `queries` (i.e., topics); count=225
 - `qrels`: (relevance assessments); count=1,837


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/cranfield', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'text': ..., 'author': ..., 'bib': ...}

queries = load_dataset('irds/cranfield', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/cranfield', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
