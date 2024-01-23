---
pretty_name: '`clueweb12`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12`

The `clueweb12` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=733,019,372


This dataset is used by: [`clueweb12_touche-2020-task-2`](https://huggingface.co/datasets/irds/clueweb12_touche-2020-task-2), [`clueweb12_touche-2021-task-2`](https://huggingface.co/datasets/irds/clueweb12_touche-2021-task-2)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clueweb12', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'date': ..., 'http_headers': ..., 'body': ..., 'body_content_type': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
