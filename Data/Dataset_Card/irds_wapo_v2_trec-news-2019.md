---
pretty_name: '`wapo/v2/trec-news-2019`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `wapo/v2/trec-news-2019`

The `wapo/v2/trec-news-2019` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/wapo#wapo/v2/trec-news-2019).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=60
 - `qrels`: (relevance assessments); count=15,655


## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/wapo_v2_trec-news-2019', 'queries')
for record in queries:
    record # {'query_id': ..., 'doc_id': ..., 'url': ...}

qrels = load_dataset('irds/wapo_v2_trec-news-2019', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Soboroff2019News,
  title={TREC 2019 News Track Overview},
  author={Ian Soboroff and Shudong Huang and Donna Harman},
  booktitle={TREC},
  year={2019}
}
```
