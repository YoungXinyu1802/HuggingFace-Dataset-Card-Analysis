---
pretty_name: '`neumarco/fa/train`'
viewer: false
source_datasets: ['irds/neumarco_fa']
task_categories:
- text-retrieval
---

# Dataset Card for `neumarco/fa/train`

The `neumarco/fa/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/neumarco#neumarco/fa/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=808,731
 - `qrels`: (relevance assessments); count=532,761
 - `docpairs`; count=269,919,004

 - For `docs`, use [`irds/neumarco_fa`](https://huggingface.co/datasets/irds/neumarco_fa)

This dataset is used by: [`neumarco_fa_train_judged`](https://huggingface.co/datasets/irds/neumarco_fa_train_judged)


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/neumarco_fa_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/neumarco_fa_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

docpairs = load_dataset('irds/neumarco_fa_train', 'docpairs')
for record in docpairs:
    record # {'query_id': ..., 'doc_id_a': ..., 'doc_id_b': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
