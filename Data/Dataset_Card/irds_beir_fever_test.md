---
pretty_name: '`beir/fever/test`'
viewer: false
source_datasets: ['irds/beir_fever']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/fever/test`

The `beir/fever/test` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/fever/test).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=6,666
 - `qrels`: (relevance assessments); count=7,937

 - For `docs`, use [`irds/beir_fever`](https://huggingface.co/datasets/irds/beir_fever)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_fever_test', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_fever_test', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Thorne2018Fever,
    title = "{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification",
    author = "Thorne, James  and
      Vlachos, Andreas  and
      Christodoulopoulos, Christos  and
      Mittal, Arpit",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N18-1074",
    doi = "10.18653/v1/N18-1074",
    pages = "809--819"
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
