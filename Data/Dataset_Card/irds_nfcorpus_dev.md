---
pretty_name: '`nfcorpus/dev`'
viewer: false
source_datasets: ['irds/nfcorpus']
task_categories:
- text-retrieval
---

# Dataset Card for `nfcorpus/dev`

The `nfcorpus/dev` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nfcorpus#nfcorpus/dev).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=325
 - `qrels`: (relevance assessments); count=14,589

 - For `docs`, use [`irds/nfcorpus`](https://huggingface.co/datasets/irds/nfcorpus)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/nfcorpus_dev', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'all': ...}

qrels = load_dataset('irds/nfcorpus_dev', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

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
