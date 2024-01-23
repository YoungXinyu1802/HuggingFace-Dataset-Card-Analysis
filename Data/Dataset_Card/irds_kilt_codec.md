---
pretty_name: '`kilt/codec`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `kilt/codec`

The `kilt/codec` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/kilt#kilt/codec).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=42
 - `qrels`: (relevance assessments); count=11,323


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/kilt_codec', 'queries')
for record in queries:
    record # {'query_id': ..., 'query': ..., 'domain': ..., 'guidelines': ...}

qrels = load_dataset('irds/kilt_codec', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{mackie2022codec,
   title={CODEC: Complex Document and Entity Collection},
   author={Mackie, Iain and Owoicho, Paul and Gemmell, Carlos and Fischer, Sophie and MacAvaney, Sean and Dalton, Jeffery},
   booktitle={Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
   year={2022}
}
```
