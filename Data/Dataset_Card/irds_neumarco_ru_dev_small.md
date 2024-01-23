---
pretty_name: '`neumarco/ru/dev/small`'
viewer: false
source_datasets: ['irds/neumarco_ru']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/ru/dev/small`

The `neumarco/ru/dev/small` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/ru/dev/small).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=6,980
 - `qrels`: (relevance assessments); count=7,437

 - For `docs`, use [`irds/neumarco_ru`](https://huggingface.co/datasets/irds/neumarco_ru)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_ru_dev_small', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/neumarco_ru_dev_small', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
