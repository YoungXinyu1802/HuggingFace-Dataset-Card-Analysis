---
pretty_name: '`beir/nfcorpus/train`'
viewer: false
source_datasets: ['irds/beir_nfcorpus']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/nfcorpus/train`

The `beir/nfcorpus/train` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/nfcorpus/train).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=2,590
 - `qrels`: (relevance assessments); count=110,575

 - For `docs`, use [`irds/beir_nfcorpus`](https://huggingface.co/datasets/irds/beir_nfcorpus)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_nfcorpus_train', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_nfcorpus_train', 'qrels')
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
@article{Thakur2021Beir,
  title = "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models",
  author = "Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna", 
  journal= "arXiv preprint arXiv:2104.08663",
  month = "4",
  year = "2021",
  url = "https://arxiv.org/abs/2104.08663",
}
```
