---
pretty_name: '`disks45/nocr`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `disks45/nocr`

The `disks45/nocr` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/disks45#disks45/nocr).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=528,155


This dataset is used by: [`disks45_nocr_trec-robust-2004`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004), [`disks45_nocr_trec-robust-2004_fold1`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004_fold1), [`disks45_nocr_trec-robust-2004_fold2`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004_fold2), [`disks45_nocr_trec-robust-2004_fold3`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004_fold3), [`disks45_nocr_trec-robust-2004_fold4`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004_fold4), [`disks45_nocr_trec-robust-2004_fold5`](https://huggingface.co/datasets/irds/disks45_nocr_trec-robust-2004_fold5), [`disks45_nocr_trec7`](https://huggingface.co/datasets/irds/disks45_nocr_trec7), [`disks45_nocr_trec8`](https://huggingface.co/datasets/irds/disks45_nocr_trec8)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/disks45_nocr', 'docs')
for record in docs:
    record # {'doc_id': ..., 'title': ..., 'body': ..., 'marked_up_doc': ...}

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
```
