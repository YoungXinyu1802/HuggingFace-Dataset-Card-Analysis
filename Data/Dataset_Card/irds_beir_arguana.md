---
pretty_name: '`beir/arguana`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/arguana`

The `beir/arguana` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/arguana).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=8,674
 - `queries` (i.e., topics); count=1,406
 - `qrels`: (relevance assessments); count=1,406


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_arguana', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ...}

queries = load_dataset('irds/beir_arguana', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_arguana', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Wachsmuth2018Arguana,
  author = "Wachsmuth, Henning and Syed, Shahbaz and Stein, Benno",
  title = "Retrieval of the Best Counterargument without Prior Topic Knowledge",
  booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  location = "Melbourne, Australia",
  pages = "241--251",
  url = "http://aclweb.org/anthology/P18-1023"
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
