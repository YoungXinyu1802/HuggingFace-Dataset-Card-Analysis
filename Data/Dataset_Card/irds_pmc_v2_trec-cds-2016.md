---
pretty_name: '`pmc/v2/trec-cds-2016`'
viewer: false
source_datasets: ['irds/pmc_v2']
task_categories:
- text-retrieval
---

# Dataset Card for `pmc/v2/trec-cds-2016`

The `pmc/v2/trec-cds-2016` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/pmc#pmc/v2/trec-cds-2016).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=30
 - `qrels`: (relevance assessments); count=37,707

 - For `docs`, use [`irds/pmc_v2`](https://huggingface.co/datasets/irds/pmc_v2)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/pmc_v2_trec-cds-2016', 'queries')
for record in queries:
    record # {'query_id': ..., 'type': ..., 'note': ..., 'description': ..., 'summary': ...}

qrels = load_dataset('irds/pmc_v2_trec-cds-2016', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Roberts2016TrecCds,
  title={Overview of the TREC 2016 Clinical Decision Support Track},
  author={Kirk Roberts and Dina Demner-Fushman and Ellen M. Voorhees and William R. Hersh},
  booktitle={TREC},
  year={2016}
}
```
