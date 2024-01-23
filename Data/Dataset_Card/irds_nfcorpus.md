---
pretty_name: '`nfcorpus`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `nfcorpus`

The `nfcorpus` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/nfcorpus#nfcorpus).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=5,371


This dataset is used by: [`nfcorpus_dev`](https://huggingface.co/datasets/irds/nfcorpus_dev), [`nfcorpus_dev_nontopic`](https://huggingface.co/datasets/irds/nfcorpus_dev_nontopic), [`nfcorpus_dev_video`](https://huggingface.co/datasets/irds/nfcorpus_dev_video), [`nfcorpus_test`](https://huggingface.co/datasets/irds/nfcorpus_test), [`nfcorpus_test_nontopic`](https://huggingface.co/datasets/irds/nfcorpus_test_nontopic), [`nfcorpus_test_video`](https://huggingface.co/datasets/irds/nfcorpus_test_video), [`nfcorpus_train`](https://huggingface.co/datasets/irds/nfcorpus_train), [`nfcorpus_train_nontopic`](https://huggingface.co/datasets/irds/nfcorpus_train_nontopic), [`nfcorpus_train_video`](https://huggingface.co/datasets/irds/nfcorpus_train_video)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/nfcorpus', 'docs')
for record in docs:
    record # {'doc_id': ..., 'url': ..., 'title': ..., 'abstract': ...}

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
