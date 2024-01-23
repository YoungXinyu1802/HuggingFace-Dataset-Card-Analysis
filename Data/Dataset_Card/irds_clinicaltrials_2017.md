---
pretty_name: '`clinicaltrials/2017`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2017`

The `clinicaltrials/2017` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2017).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=241,006


This dataset is used by: [`clinicaltrials_2017_trec-pm-2017`](https://huggingface.co/datasets/irds/clinicaltrials_2017_trec-pm-2017), [`clinicaltrials_2017_trec-pm-2018`](https://huggingface.co/datasets/irds/clinicaltrials_2017_trec-pm-2018)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/clinicaltrials_2017', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'condition': ..., 'summary': ..., 'detailed_description': ..., 'eligibility': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.
