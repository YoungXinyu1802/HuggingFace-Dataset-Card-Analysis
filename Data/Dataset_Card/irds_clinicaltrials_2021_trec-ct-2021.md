---
pretty_name: '`clinicaltrials/2021/trec-ct-2021`'
viewer: false
source_datasets: ['irds/clinicaltrials_2021']
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2021/trec-ct-2021`

The `clinicaltrials/2021/trec-ct-2021` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2021/trec-ct-2021).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=75
 - `qrels`: (relevance assessments); count=35,832

 - For `docs`, use [`irds/clinicaltrials_2021`](https://huggingface.co/datasets/irds/clinicaltrials_2021)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clinicaltrials_2021_trec-ct-2021', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/clinicaltrials_2021_trec-ct-2021', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
