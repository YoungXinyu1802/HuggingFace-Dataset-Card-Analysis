---
pretty_name: '`clinicaltrials/2019`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2019`

The `clinicaltrials/2019` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2019).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=306,238


This dataset is used by: [`clinicaltrials_2019_trec-pm-2019`](https://huggingface.co/datasets/irds/clinicaltrials_2019_trec-pm-2019)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clinicaltrials_2019', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'condition': ..., 'summary': ..., 'detailed_description': ..., 'eligibility': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
