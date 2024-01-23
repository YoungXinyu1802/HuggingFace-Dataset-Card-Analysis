---
pretty_name: '`istella22/test/fold3`'
viewer: false
source_datasets: ['irds/istella22']
task_categories:
- text-retrieval
---

# Dataset Card for `istella22/test/fold3`

The `istella22/test/fold3` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/istella22#istella22/test/fold3).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=440
 - `qrels`: (relevance assessments); count=2,197

 - For `docs`, use [`irds/istella22`](https://huggingface.co/datasets/irds/istella22)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/istella22_test_fold3', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/istella22_test_fold3', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.