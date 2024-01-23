---
pretty_name: '`clueweb09/ja`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb09/ja`

The `clueweb09/ja` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb09#clueweb09/ja).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=67,337,717


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clueweb09_ja', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'date': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
