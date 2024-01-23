---
pretty_name: '`beir/quora`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/quora`

The `beir/quora` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/quora).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=522,931
 - `queries` (i.e., topics); count=15,000


This dataset is used by: [`beir_quora_dev`](https://huggingface.co/datasets/irds/beir_quora_dev), [`beir_quora_test`](https://huggingface.co/datasets/irds/beir_quora_test)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_quora', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ...}

queries = load_dataset('irds/beir_quora', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

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
