---
pretty_name: '`beir/nfcorpus`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/nfcorpus`

The `beir/nfcorpus` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/nfcorpus).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=3,633
 - `queries` (i.e., topics); count=3,237


This dataset is used by: [`beir_nfcorpus_dev`](https://huggingface.co/datasets/irds/beir_nfcorpus_dev), [`beir_nfcorpus_test`](https://huggingface.co/datasets/irds/beir_nfcorpus_test), [`beir_nfcorpus_train`](https://huggingface.co/datasets/irds/beir_nfcorpus_train)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_nfcorpus', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ..., 'url': ...}

queries = load_dataset('irds/beir_nfcorpus', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ..., 'url': ...}

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
@article{Thakur2021Beir,
  title = "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models",
  author = "Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna", 
  journal= "arXiv preprint arXiv:2104.08663",
  month = "4",
  year = "2021",
  url = "https://arxiv.org/abs/2104.08663",
}
```
