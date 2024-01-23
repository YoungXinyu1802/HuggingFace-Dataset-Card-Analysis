---
pretty_name: '`disks45/nocr/trec8`'
viewer: false
source_datasets: ['irds/disks45_nocr']
task_categories:
- text-retrieval
---

# Dataset Card for `disks45/nocr/trec8`

The `disks45/nocr/trec8` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/disks45#disks45/nocr/trec8).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=50
 - `qrels`: (relevance assessments); count=86,830

 - For `docs`, use [`irds/disks45_nocr`](https://huggingface.co/datasets/irds/disks45_nocr)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/disks45_nocr_trec8', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/disks45_nocr_trec8', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@misc{Voorhees1996Disks45,
  title = {NIST TREC Disks 4 and 5: Retrieval Test Collections Document Set},
  author = {Ellen M. Voorhees},
  doi = {10.18434/t47g6m},
  year = {1996},
  publisher = {National Institute of Standards and Technology}
}
@inproceedings{Voorhees1999Trec8,
  title = {Overview of the Eight Text Retrieval Conference (TREC-8)},
  author = {Ellen M. Voorhees and Donna Harman},
  year = {1999},
  booktitle = {TREC}
}
```
