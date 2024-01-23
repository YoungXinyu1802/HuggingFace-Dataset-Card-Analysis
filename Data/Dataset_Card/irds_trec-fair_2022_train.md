---
pretty_name: '`trec-fair/2022/train`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `trec-fair/2022/train`

The `trec-fair/2022/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/trec-fair#trec-fair/2022/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=2,088,306


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/trec-fair_2022_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ..., 'url': ...}

qrels = load_dataset('irds/trec-fair_2022_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
