---
pretty_name: '`clueweb12/b13/trec-misinfo-2019`'
viewer: false
source_datasets: ['irds/clueweb12_b13']
task_categories:
- text-retrieval
---

# Dataset Card for `clueweb12/b13/trec-misinfo-2019`

The `clueweb12/b13/trec-misinfo-2019` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/clueweb12#clueweb12/b13/trec-misinfo-2019).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=51
 - `qrels`: (relevance assessments); count=22,859

 - For `docs`, use [`irds/clueweb12_b13`](https://huggingface.co/datasets/irds/clueweb12_b13)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/clueweb12_b13_trec-misinfo-2019', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'cochranedoi': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/clueweb12_b13_trec-misinfo-2019', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'effectiveness': ..., 'redibility': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Abualsaud2019TrecDecision,
  title={Overview of the TREC 2019 Decision Track},
  author={Mustafa Abualsaud and Christina Lioma and Maria Maistro and Mark D. Smucker and Guido Zuccon},
  booktitle={TREC},
  year={2019}
}
```
