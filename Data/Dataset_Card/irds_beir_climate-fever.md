---
pretty_name: '`beir/climate-fever`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/climate-fever`

The `beir/climate-fever` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/climate-fever).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=5,416,593
 - `queries` (i.e., topics); count=1,535
 - `qrels`: (relevance assessments); count=4,681


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_climate-fever', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ...}

queries = load_dataset('irds/beir_climate-fever', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_climate-fever', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Diggelmann2020CLIMATEFEVERAD,
  title={CLIMATE-FEVER: A Dataset for Verification of Real-World Climate Claims},
  author={T. Diggelmann and Jordan L. Boyd-Graber and Jannis Bulian and Massimiliano Ciaramita and Markus Leippold},
  journal={ArXiv},
  year={2020},
  volume={abs/2012.00614}
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
