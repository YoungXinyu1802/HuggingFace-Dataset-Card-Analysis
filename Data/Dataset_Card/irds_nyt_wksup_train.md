---
pretty_name: '`nyt/wksup/train`'
viewer: false
source_datasets: ['irds/nyt']
task_categories:
- text-retrieval
---

# Dataset Card for `nyt/wksup/train`

The `nyt/wksup/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nyt#nyt/wksup/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=1,863,657
 - `qrels`: (relevance assessments); count=1,863,657

 - For `docs`, use [`irds/nyt`](https://huggingface.co/datasets/irds/nyt)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/nyt_wksup_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/nyt_wksup_train', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{MacAvaney2019Wksup,
  author = {MacAvaney, Sean and Yates, Andrew and Hui, Kai and Frieder, Ophir},
  title = {Content-Based Weak Supervision for Ad-Hoc Re-Ranking},
  booktitle = {SIGIR},
  year = {2019}
}
@article{Sandhaus2008Nyt,
  title={The new york times annotated corpus},
  author={Sandhaus, Evan},
  journal={Linguistic Data Consortium, Philadelphia},
  volume={6},
  number={12},
  pages={e26752},
  year={2008}
}
```
