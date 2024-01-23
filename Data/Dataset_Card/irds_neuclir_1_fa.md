---
pretty_name: '`neuclir/1/fa`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `neuclir/1/fa`

The `neuclir/1/fa` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neuclir#neuclir/1/fa).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=2,232,016


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/neuclir_1_fa', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'text': ..., 'url': ..., 'time': ..., 'cc_file': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
