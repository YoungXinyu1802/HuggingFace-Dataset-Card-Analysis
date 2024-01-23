---
pretty_name: '`beir/fiqa/test`'
viewer: false
source_datasets: ['irds/beir_fiqa']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/fiqa/test`

The `beir/fiqa/test` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/fiqa/test).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=648
 - `qrels`: (relevance assessments); count=1,706

 - For `docs`, use [`irds/beir_fiqa`](https://huggingface.co/datasets/irds/beir_fiqa)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_fiqa_test', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_fiqa_test', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Maia2018Fiqa,
  title={WWW'18 Open Challenge: Financial Opinion Mining and Question Answering},
  author={Macedo Maia and S. Handschuh and A. Freitas and Brian Davis and R. McDermott and M. Zarrouk and A. Balahur},
  journal={Companion Proceedings of the The Web Conference 2018},
  year={2018}
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
