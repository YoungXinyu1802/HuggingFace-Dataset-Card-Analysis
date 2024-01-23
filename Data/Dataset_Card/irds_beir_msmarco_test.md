---
pretty_name: '`beir/msmarco/test`'
viewer: false
source_datasets: ['irds/beir_msmarco']
task_categories:
- text-retrieval
---

# Dataset Card for `beir/msmarco/test`

The `beir/msmarco/test` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/beir#beir/msmarco/test).

# Data

This dataset provides:
 - `queries` (i.e., topics); count=43
 - `qrels`: (relevance assessments); count=9,260

 - For `docs`, use [`irds/beir_msmarco`](https://huggingface.co/datasets/irds/beir_msmarco)

## Usage

```python
from datasets import load_dataset

queries = load_dataset('irds/beir_msmarco_test', 'queries')
for record in queries:
    record # {'query_id': ..., 'text': ...}

qrels = load_dataset('irds/beir_msmarco_test', 'qrels')
for record in qrels:
    record # {'query_id': ..., 'doc_id': ..., 'relevance': ..., 'iteration': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@inproceedings{Craswell2019TrecDl,
  title={Overview of the TREC 2019 deep learning track},
  author={Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos and Ellen Voorhees},
  booktitle={TREC 2019},
  year={2019}
}
@inproceedings{Bajaj2016Msmarco,
  title={MS MARCO: A Human Generated MAchine Reading COmprehension Dataset},
  author={Payal Bajaj, Daniel Campos, Nick Craswell, Li Deng, Jianfeng Gao, Xiaodong Liu, Rangan Majumder, Andrew McNamara, Bhaskar Mitra, Tri Nguyen, Mir Rosenberg, Xia Song, Alina Stoica, Saurabh Tiwary, Tong Wang},
  booktitle={InCoCo@NIPS},
  year={2016}
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
