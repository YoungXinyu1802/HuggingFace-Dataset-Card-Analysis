---
pretty_name: '`beir/webis-touche2020/v2`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/webis-touche2020/v2`

The `beir/webis-touche2020/v2` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/webis-touche2020/v2).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=382,545
 - `queries` (i.e., topics); count=49
 - `qrels`: (relevance assessments); count=2,214


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_webis-touche2020_v2', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ..., 'stance': ..., 'url': ...}

queries = load_dataset('irds/beir_webis-touche2020_v2', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ..., 'description': ..., 'narrative': ...}

qrels = load_dataset('irds/beir_webis-touche2020_v2', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Bondarenko2020Tuche,
  title={Overview of Touch{\'e} 2020: Argument Retrieval},
  author={Alexander Bondarenko and Maik Fr{\"o}be and Meriem Beloucif and Lukas Gienapp and Yamen Ajjour and Alexander Panchenko and Christian Biemann and Benno Stein and Henning Wachsmuth and Martin Potthast and Matthias Hagen},
  booktitle={CLEF},
  year={2020}
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
