---
pretty_name: '`nfcorpus/dev/video`'
viewer: false
source_datasets: ['irds/nfcorpus']
task_categories:
- text-retrieval
---

# Dataset Card for `nfcorpus/dev/video`

The `nfcorpus/dev/video` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nfcorpus#nfcorpus/dev/video).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=102
 - `qrels`: (relevance assessments); count=3,068

 - For `docs`, use [`irds/nfcorpus`](https://huggingface.co/datasets/irds/nfcorpus)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/nfcorpus_dev_video', 'queries')
for record in queries:
    record # {'query_id': ..., 'title': ..., 'desc': ...}

qrels = load_dataset('irds/nfcorpus_dev_video', 'qrels')
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
