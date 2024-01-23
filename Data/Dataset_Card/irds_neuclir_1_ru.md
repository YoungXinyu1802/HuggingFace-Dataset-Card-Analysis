---
pretty_name: '`neuclir/1/ru`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `neuclir/1/ru`

The `neuclir/1/ru` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neuclir#neuclir/1/ru).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=4,627,543


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/neuclir_1_ru', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'text': ..., 'url': ..., 'time': ..., 'cc_file': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
