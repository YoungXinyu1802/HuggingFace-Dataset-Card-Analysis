---
pretty_name: '`clinicaltrials/2017/trec-pm-2018`'
viewer: false
source_datasets: ['irds/clinicaltrials_2017']
task_categories:
- text-retrieval
---

# Dataset Card for `clinicaltrials/2017/trec-pm-2018`

The `clinicaltrials/2017/trec-pm-2018` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clinicaltrials#clinicaltrials/2017/trec-pm-2018).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=14,188

 - For `docs`, use [`irds/clinicaltrials_2017`](https://huggingface.co/datasets/irds/clinicaltrials_2017)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clinicaltrials_2017_trec-pm-2018', 'queries')
for record in queries:
    record # {'query_id': ..., 'disease': ..., 'gene': ..., 'demographic': ...}

qrels = load_dataset('irds/clinicaltrials_2017_trec-pm-2018', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Roberts2018TrecPm,
  title={Overview of the TREC 2018 Precision Medicine Track},
  author={Kirk Roberts and Dina Demner-Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar},
  booktitle={TREC},
  year={2018}
}
```
