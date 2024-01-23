---
pretty_name: '`pmc/v1/trec-cds-2015`'
viewer: false
source_datasets: ['irds/pmc_v1']
task_categories:
- text-retrieval
---

# Dataset Card for `pmc/v1/trec-cds-2015`

The `pmc/v1/trec-cds-2015` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/pmc#pmc/v1/trec-cds-2015).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=30
 - `qrels`: (relevance assessments); count=37,807

 - For `docs`, use [`irds/pmc_v1`](https://huggingface.co/datasets/irds/pmc_v1)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/pmc_v1_trec-cds-2015', 'queries')
for record in queries:
    record # {'query_id': ..., 'type': ..., 'description': ..., 'summary': ...}

qrels = load_dataset('irds/pmc_v1_trec-cds-2015', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Roberts2015TrecCds,
  title={Overview of the TREC 2015 Clinical Decision Support Track},
  author={Kirk Roberts and Matthew S. Simpson and Ellen Voorhees and William R. Hersh},
  booktitle={TREC},
  year={2015}
}
```
