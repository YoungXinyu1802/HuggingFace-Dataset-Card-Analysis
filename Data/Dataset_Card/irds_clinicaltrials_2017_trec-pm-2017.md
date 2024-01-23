---
pretty_name: '`clinicaltrials/2017/trec-pm-2017`'
viewer: false
source_datasets: ['irds/clinicaltrials_2017']
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2017/trec-pm-2017`

The `clinicaltrials/2017/trec-pm-2017` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2017/trec-pm-2017).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=30
 - `qrels`: (relevance assessments); count=13,019

 - For `docs`, use [`irds/clinicaltrials_2017`](https://huggingface.co/datasets/irds/clinicaltrials_2017)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clinicaltrials_2017_trec-pm-2017', 'queries')
for record in queries:
    record # {'query_id': ..., 'disease': ..., 'gene': ..., 'demographic': ..., 'other': ...}

qrels = load_dataset('irds/clinicaltrials_2017_trec-pm-2017', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Roberts2017TrecPm,
  title={Overview of the TREC 2017 Precision Medicine Track},
  author={Kirk Roberts and Dina Demner-Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant},
  booktitle={TREC},
  year={2017}
}
```
