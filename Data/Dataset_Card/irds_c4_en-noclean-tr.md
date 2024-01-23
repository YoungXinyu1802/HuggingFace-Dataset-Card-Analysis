---
pretty_name: '`c4/en-noclean-tr`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `c4/en-noclean-tr`

The `c4/en-noclean-tr` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/c4#c4/en-noclean-tr).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=1,063,805,381


This dataset is used by: [`c4_en-noclean-tr_trec-misinfo-2021`](https://huggingface.co/datasets/irds/c4_en-noclean-tr_trec-misinfo-2021)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/c4_en-noclean-tr', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'url': ..., 'timestamp': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
