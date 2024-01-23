---
pretty_name: '`c4/en-noclean-tr/trec-misinfo-2021`'
viewer: false
source_datasets: ['irds/c4_en-noclean-tr']
task_categories:
- text-retrieval
---

# Dataset Card for `c4/en-noclean-tr/trec-misinfo-2021`

The `c4/en-noclean-tr/trec-misinfo-2021` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/c4#c4/en-noclean-tr/trec-misinfo-2021).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50

 - For `docs`, use [`irds/c4_en-noclean-tr`](https://huggingface.co/datasets/irds/c4_en-noclean-tr)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/c4_en-noclean-tr_trec-misinfo-2021', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ..., 'description': ..., 'narrative': ..., 'disclaimer': ..., 'stance': ..., 'evidence': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
