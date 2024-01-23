---
pretty_name: '`nfcorpus/train/nontopic`'
viewer: false
source_datasets: ['irds/nfcorpus']
task_categories:
- text-retrieval
---

# Dataset Card for `nfcorpus/train/nontopic`

The `nfcorpus/train/nontopic` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nfcorpus#nfcorpus/train/nontopic).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=1,141
 - `qrels`: (relevance assessments); count=37,383

 - For `docs`, use [`irds/nfcorpus`](https://huggingface.co/datasets/irds/nfcorpus)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/nfcorpus_train_nontopic', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/nfcorpus_train_nontopic', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Boteva2016Nfcorpus,
  title="A Full-Text Learning to Rank Dataset for Medical Information Retrieval",
  author = "Vera Boteva and Demian Gholipour and Artem Sokolov and Stefan Riezler",
  booktitle = "Proceedings of the European Conference on Information Retrieval ({ECIR})",
  location = "Padova, Italy",
  publisher = "Springer",
  year = 2016
}
```
