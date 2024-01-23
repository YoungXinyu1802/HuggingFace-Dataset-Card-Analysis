---
pretty_name: '`pmc/v2`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `pmc/v2`

The `pmc/v2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/pmc#pmc/v2).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,255,260


This dataset is used by: [`pmc_v2_trec-cds-2016`](https://huggingface.co/datasets/irds/pmc_v2_trec-cds-2016)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/pmc_v2', 'docs')
for record in docs:
    record # {'doc_id': ..., 'journal': ..., 'title': ..., 'abstract': ..., 'body': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
