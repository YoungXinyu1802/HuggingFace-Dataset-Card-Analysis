---
pretty_name: '`clinicaltrials/2019/trec-pm-2019`'
viewer: false
source_datasets: ['irds/clinicaltrials_2019']
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2019/trec-pm-2019`

The `clinicaltrials/2019/trec-pm-2019` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2019/trec-pm-2019).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=40
 - `qrels`: (relevance assessments); count=12,996

 - For `docs`, use [`irds/clinicaltrials_2019`](https://huggingface.co/datasets/irds/clinicaltrials_2019)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clinicaltrials_2019_trec-pm-2019', 'queries')
for record in queries:
    record # {'query_id': ..., 'disease': ..., 'gene': ..., 'demographic': ...}

qrels = load_dataset('irds/clinicaltrials_2019_trec-pm-2019', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Roberts2019TrecPm,
  title={Overview of the TREC 2019 Precision Medicine Track},
  author={Kirk Roberts and Dina Demner-Fushman and Ellen Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant and Funda Meric-Bernstam},
  booktitle={TREC},
  year={2019}
}
```
