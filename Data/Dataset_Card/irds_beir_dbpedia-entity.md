---
pretty_name: '`beir/dbpedia-entity`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `beir/dbpedia-entity`

The `beir/dbpedia-entity` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/dbpedia-entity).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=4,635,922
 - `queries` (i.e., topics); count=467


This dataset is used by: [`beir_dbpedia-entity_dev`](https://huggingface.co/datasets/irds/beir_dbpedia-entity_dev), [`beir_dbpedia-entity_test`](https://huggingface.co/datasets/irds/beir_dbpedia-entity_test)


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/beir_dbpedia-entity', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'title': ..., 'url': ...}

queries = load_dataset('irds/beir_dbpedia-entity', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Hasibi2017DBpediaEntityVA,
  title={DBpedia-Entity v2: A Test Collection for Entity Search},
  author={Faegheh Hasibi and Fedor Nikolaev and Chenyan Xiong and K. Balog and S. E. Bratsberg and Alexander Kotov and J. Callan},
  journal={Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  year={2017}
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
