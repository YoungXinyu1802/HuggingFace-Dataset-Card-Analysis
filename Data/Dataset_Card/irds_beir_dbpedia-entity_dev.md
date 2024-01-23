---
pretty_name: '`beir/dbpedia-entity/dev`'
viewer: false
source_datasets: ['irds/beir_dbpedia-entity']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/dbpedia-entity/dev`

The `beir/dbpedia-entity/dev` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/dbpedia-entity/dev).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=67
 - `qrels`: (relevance assessments); count=5,673

 - For `docs`, use [`irds/beir_dbpedia-entity`](https://huggingface.co/datasets/irds/beir_dbpedia-entity)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_dbpedia-entity_dev', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_dbpedia-entity_dev', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

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
