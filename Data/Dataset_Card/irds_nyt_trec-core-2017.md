---
pretty_name: '`nyt/trec-core-2017`'
viewer: false
source_datasets: ['irds/nyt']
task_categories:
- text-retrieval
---

# Dataset Card for `nyt/trec-core-2017`

The `nyt/trec-core-2017` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nyt#nyt/trec-core-2017).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=30,030

 - For `docs`, use [`irds/nyt`](https://huggingface.co/datasets/irds/nyt)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/nyt_trec-core-2017', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/nyt_trec-core-2017', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Allan2017TrecCore,
  author = {James Allan and Donna Harman and Evangelos Kanoulas and Dan Li and Christophe Van Gysel and Ellen Vorhees},
  title = {TREC 2017 Common Core Track Overview},
  booktitle = {TREC},
  year = {2017}
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
