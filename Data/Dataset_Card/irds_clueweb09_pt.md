---
pretty_name: '`clueweb09/pt`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb09/pt`

The `clueweb09/pt` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb09#clueweb09/pt).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=37,578,858


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clueweb09_pt', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'date': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
