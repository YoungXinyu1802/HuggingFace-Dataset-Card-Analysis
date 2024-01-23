---
pretty_name: '`beir/quora/test`'
viewer: false
source_datasets: ['irds/beir_quora']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/quora/test`

The `beir/quora/test` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/quora/test).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=10,000
 - `qrels`: (relevance assessments); count=15,675

 - For `docs`, use [`irds/beir_quora`](https://huggingface.co/datasets/irds/beir_quora)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_quora_test', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_quora_test', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Thakur2021Beir,
  title = "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models",
  author = "Thakur, Nandan and Reimers, Nils and Rücklé, Andreas and Srivastava, Abhishek and Gurevych, Iryna", 
  journal= "arXiv preprint arXiv:2104.08663",
  month = "4",
  year = "2021",
  url = "https://arxiv.org/abs/2104.08663",
}
```
