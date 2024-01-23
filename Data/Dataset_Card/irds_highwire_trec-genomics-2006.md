---
pretty_name: '`highwire/trec-genomics-2006`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `highwire/trec-genomics-2006`

The `highwire/trec-genomics-2006` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/highwire#highwire/trec-genomics-2006).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=28
 - `qrels`: (relevance assessments); count=27,999


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/highwire_trec-genomics-2006', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/highwire_trec-genomics-2006', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'start': ..., 'length': ..., 'relevance': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Hersh2006TrecGenomics,
  title={TREC 2006 Genomics Track Overview},
  author={William Hersh and Aaron M. Cohen and Phoebe Roberts and Hari Krishna Rekapalli},
  booktitle={TREC},
  year={2006}
}
```
